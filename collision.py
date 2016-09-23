
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
    time.sleep(1)
    try:
        utxo = unspent(addr)
        if utxo:
            record(priv)
    except Exception as e:
        time.sleep(10)

