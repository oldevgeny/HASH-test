## ТЗ:

Скрипт, который по адресу кошелька и адресу контракта токена BEP20 возвращает баланс этого токена на этом кошельке.

Пример кошелька:
https://bscscan.com/address/0xc36e54d8313d76168c823bf44cb72e46020dbf73

Пример токена:
https://bscscan.com/address/0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d

#### Пример работы скрипта:

```
python3 wallet_balances_bsc.py --wallet=0xc36E54d8313d76168c823BF44cB72e46020DbF73 --token=0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d
```

#### Output:

```
 11.6
```

## Установка:

```
python3.9 -m venv venv
source venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```
