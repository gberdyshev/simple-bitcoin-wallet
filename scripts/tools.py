import qrcode
import os
import random
import requests

from scripts import consts

class Tools(object):

    """Генерация qr-кода, используется для генерации qr адреса"""
    def qrcode_generator(self, content):
        img = qrcode.make(content)
        path = f"{consts.__temp_path__}qr_{content}.png"
        img.save(path)
        return path

    def get_strong_entropy(self):
        return os.urandom(16) \
    + str(random.randrange(2**256))

    """Актуальная комиссия в блокчейне тестнета"""
    def get_actual_fee(self):
        r = requests.get("https://testnet.bitcoinexplorer.org/api/mempool/fees")
        if r.status_code != 200:
            return False # сервис недоступен
        r = r.json()
        fast, standard, slow = r["nextBlock"], r["30min"], r["1day"]

        return fast, standard, slow


    """Расчет размера транзации (приблизительного) и комиссии по нему"""
    def calc_fee(self, inputs, outs = 2, sat_byte = 1):
        return (inputs * 148 + outs * 34 + 10) * sat_byte
