import json

json_config_file = './scripts/config.json'

def get_json_config():
    jsonconfig = {}
    with open(json_config_file, 'r') as file:
        jsonconfig = json.load(file)
        file.close()
    return jsonconfig


__db_path__ = get_json_config()["data_db_path"]
__wallet_db_path__ = get_json_config()["wallet_db_path"]
__temp_path__ = get_json_config()["temp_path"]
if get_json_config()["currency"] == "btc":
    __currency__ = 10**8
elif get_json_config()["currency"] == "sat":
     __currency__ = 1
__db_folder_path__ = get_json_config()["db_folder"]
__ui_dark_theme__ = """
                    background-color: rgb(53, 51, 51);
                    font: 11pt "Cantarell";
                    color: white;
                    border-color: rgba(216, 151, 50, 246);"""
__ui_light_theme__ = """font: 11pt "Cantarell";"""
