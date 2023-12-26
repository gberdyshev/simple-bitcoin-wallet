import qrcode
import os
import random

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



