import json

__json_config_file__ = 'simple_bitcoin_wallet/scripts/config.json'

def get_json_config():
    jsonconfig = {}
    with open(__json_config_file__, 'r') as file:
        jsonconfig = json.load(file)
        file.close()
    return jsonconfig

jsonconfig = get_json_config()
__db_path__ = jsonconfig["data_db_path"]
__wallet_db_path__ = jsonconfig["wallet_db_path"]
__temp_path__ = jsonconfig["temp_path"]
__db_folder_path__ = jsonconfig["db_folder"]
__ui_dark_theme__ = """
                    background-color: rgb(53, 51, 51);
                    font: 11pt "Cantarell";
                    color: white;
                    border-color: rgba(216, 151, 50, 246);"""
                    
__ui_light_theme__ = """font: 11pt "Cantarell";"""

__repository__ = "https://github.com/gberdyshev/simple-bitcoin-wallet"
__docs__ = "https://github.com/gberdyshev/simple-bitcoin-wallet/blob/main/docs/user_guide.md"
__author__ = "https://github.com/gberdyshev"

if jsonconfig["currency"] == "btc":
    __currency__ = 10**8
elif jsonconfig["currency"] == "sat":
     __currency__ = 1

if jsonconfig["network"] == "testnet":
    __testnet__ = True
elif jsonconfig["network"] == "mainnet":
    __testnet__ = False
