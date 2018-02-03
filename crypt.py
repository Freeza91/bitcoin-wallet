#encoding=utf-8

import sys
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

class Prpcrypt():
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC

    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        length = 16
        count = len(text)
        add = length - (count % length)
        text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        return b2a_hex(self.ciphertext)

    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip('\0')

if __name__ == '__main__':
    args = sys.argv
    words = args[1]
    priv_key = args[2]
    direction = args[3]

    crypt = Prpcrypt(priv_key[:16])

    if direction == '1':
        print "encrypt data is: ---->>>>> "
        print crypt.encrypt(words)
    else:
        print "decrypt data is: ---->>>>> "
        print crypt.decrypt(words)

"""
python crypt.py 'your help words' 'your priv key' direction
"""


