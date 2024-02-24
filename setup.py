from setuptools import setup, find_packages


setup(
    # App name
    # This can be any name as long as only contains letters, numbers, '_' and '-'
    name="simple_bitcoin_wallet",
    # Some information about the app
    # You can write almost anything here
    version="1.0",
    url="https://github.com/gberdyshev/simple-bitcoin-wallet",
    license="GNU GPL V3",
    author="Grigoriy Berdyshev",
    author_email="bga20100@gmail.com",
    description="Simple Deterministic Bitcoin Wallet",
    # Packages in this example is ['gui']
    # We can specify it explicitly, but fortunately we have a special function
    packages=[
        "simple_bitcoin_wallet",
        "simple_bitcoin_wallet.classes",
        "simple_bitcoin_wallet.db",
        "simple_bitcoin_wallet.resources",
        "simple_bitcoin_wallet.scripts",
        "simple_bitcoin_wallet.ui",
    ],
    package_data={
        "simple_bitcoin_wallet": [
            "scripts/config.json",
            "resources/init.sql",
            "ui/form.ui",
            "ui/firstrun_form.ui",
        ]
    },
    # For this example we use external library 'kivy'
    install_requires=["pyside6", "cryptos-witness", "requests", "sqlcipher3", "qrcode", "pyqt6"],
    # Entry point for app
    # By default the startup script is installed in '/usr/local/bin' or something like that in other systems
    # To create startup script in installation dir run './setup.py install --install-scripts .'
    # after that startup script will be created in the installation directory
    # and can be run as './gui_example'
    # But it is recommended to install scripts in a separate directory './setup.py install --install-scripts ./scripts'
    # because in addition to the main scripts dependency scripts can also be installed
    entry_points={
        "gui_scripts": [
            "simple_bitcoin_wallet = simple_bitcoin_wallet:main",
        ],
    },
)
