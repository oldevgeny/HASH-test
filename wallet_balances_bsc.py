import argparse
import json
import logging
from typing import Tuple

from contract import BSCContract
from settings import ABI

logger = logging.getLogger(__name__)


def get_parsed_args() -> Tuple[str, str]:
    parser = argparse.ArgumentParser(description='Key_Value storage')

    parser.add_argument('--wallet', action="store", dest="wallet", help="Добавить значение адреса кошелька.")
    parser.add_argument('--token', action="store", dest="token", help="Добавить значение адреса токена.")

    args = parser.parse_args()
    return args.wallet, args.token


if __name__ == '__main__':
    parsed_args: Tuple[str, str] = get_parsed_args()

    if not all(parsed_args):
        logger.error(f"Отсутствует хотя бы один из параметров: --wallet, --token.")
        raise SystemExit

    wallet, token = parsed_args

    abi = json.loads(ABI)

    contract = BSCContract(address=token, ABI=abi)

    symbol = contract.get_contract_symbol()
    name = contract.get_contract_name()
    decimals = contract.get_contract_decimals()

    balance = contract.get_balance_by_wallet_address(wallet=wallet)
    quantity = balance / 10 ** decimals

    print(f"""
    Wallet: {wallet},
    Token: {name},
    Quantity: {quantity} {symbol}.
    """)
