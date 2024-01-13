import qrcode
import os
import random
import requests
import json

from simple_bitcoin_wallet.scripts import consts




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
        try:
            # Проверяем, в тестнете или нет
            if consts.__testnet__ is True:
                url = "https://mempool.space/testnet/api/v1/fees/recommended"
            else:
                url = "https://mempool.space/api/v1/fees/recommended"
            r = requests.get(url, timeout=3)
            if r.status_code != 200:
                return False # сервис недоступен
            r = r.json()
            fast, standard, slow = r["fastestFee"], r["halfHourFee"], r["economyFee"]

            return fast, standard, slow
        except requests.exceptions.Timeout:
            print("Timeout Blockchain Explorer")
            return False


    """Расчет размера транзации (приблизительного) и комиссии по нему"""
    def calc_fee(self, inputs, outs = 2, sat_byte = 1):
        return (inputs * 148 + outs * 34 + 10) * sat_byte

    """Получить текущую тему приложения"""
    def get_theme_option(self):
        jsonconfig = {}
        with open(consts.__json_config_file__, 'r') as file:
            jsonconfig = json.load(file)
            file.close()
        return jsonconfig["ui_theme"]

    """Изменить текущую тему приложения"""
    def change_theme_option(self, option):
        with open(consts.__json_config_file__, 'r') as file:
            jsonconfig = json.load(file)
            file.close()
        with open(consts.__json_config_file__, 'w') as file:
            jsonconfig["ui_theme"] = option
            json.dump(jsonconfig, file)
            file.close()


