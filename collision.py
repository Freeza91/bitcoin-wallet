
from bitcoin.main import random_key, privtoaddr, sum
from bitcoin.bci import unspent
import time

def record(priv):
    print "find this lucky!"
    with open('priv.txt', 'a') as _file:
        _file.writelines(priv + "\n")

while True:
    priv = random_key()
    addr = privtoaddr(priv)
    utxo = unspent(addr)
    if utxo:
        time.sleep(5)
        record(priv)

