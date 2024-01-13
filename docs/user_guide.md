# Документация для пользователей

## Установка

### Unix-подобные ОС (Linux, MacOs, *BSD)
1. Получить репозиторий
```
git clone https://github.com/gberdyshev/simple-bitcoin-wallet.git
cd simple-bitcoin-wallet
```

2. Установить зависимости из файла ``req.txt``. Рекомендуется это делать в виртуальном окружении Python ([подробнее про venv](https://docs.python.org/3/library/venv.html)).

```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r req.txt
```
3. Запустить приложение
```
python -m simple_bitcoin_wallet
```
### Windows

В процессе...
