# Simple Bitcoin Wallet

<div style="text-align: center;">

![Логотип](simple_bitcoin_wallet/resources/logo.png)

**Некастодиальный детерминированный Bitcoin кошелек**
</div>


## Установить:

Документация In progress...

Установить зависимости из req.txt (в виртуальном окружении), запустить mainwindow.py

(На ОС Windows библиотека sqlcipher3 не собирается, вместо нее можно использовать стандартный sqlite3, но шифрование кошелька в этом случае работать не будет)

## Замечание

В рамках этого проекта мною был исправлен некритичный баг в библиотеке cryptos, был создан PR, который на сегодняшний день не принят,
поэтому было принято решение опубликовать форк библиотеки на PyPI (https://pypi.org/project/cryptos-witness/), чтобы была возможность загрузить исправленную версию библиотеки

![Светлая тема](./docs/screenshots/light_theme.png)

![Темная тема](./docs/screenshots/dark_theme.png)
