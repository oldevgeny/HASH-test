# class AbstractContract is a template for any 
# EVM based contract and initializing with contract address and ABI.
# Address and ABI can be found on blockchain explorer such as https://etherscan.io

import logging
from abc import ABC

from web3 import Web3

from exceptions import ProviderInitException
from settings import BSC

logger = logging.getLogger(__name__)


class AbstractContract(ABC):
    provider = None

    def __init__(self, address: str, ABI: str):

        if self.provider is not None:
            w3 = Web3(Web3.HTTPProvider(self.provider))
        else:
            raise ProviderInitException

        try:
            self.contract = w3.eth.contract(address, abi=ABI)
        except Exception as e:
            logger.error(f'{e} in contract {address}')

    @property
    def address(self):
        return self.contract.address

    @property
    def abi(self):
        return self.contract.abi

    def get_functions_list(self) -> list:
        return self.contract.all_functions()


class BSCContract(AbstractContract):
    provider = BSC

    def get_balance_by_wallet_address(self, wallet):
        return self.contract.functions.balanceOf(wallet).call()

    def get_contract_symbol(self):
        return self.contract.functions.symbol().call()

    def get_contract_name(self):
        return self.contract.functions.name().call()

    def get_contract_decimals(self):
        return self.contract.functions.decimals().call()
