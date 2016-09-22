# -*- coding: utf-8 -*-

from bitcoin.transaction import deserialize, txhash
from bitcoin.bci import pushtx
from decimal import Decimal

def covert_btc(amount):
    return Decimal(amount) / 100000000

def show_transfer_info(sign_tx):
    deserialize_tx = deserialize(sign_tx)
    outs = deserialize_tx['outs']
    inps = deserialize_tx['ins']
    outs_sum = reduce(lambda x,y: x['value'] + y['value'], outs)
    inps_sum = reduce(lambda x,y: x['value'] + y['value'], inps)
    change_sum = outs_sum - inps_sum

    print "此次转账一览表(含找零和手续费):"
    print "----" * 30
    print "| %10s | %10s | %10s |" %('总输入', '花费(含找零)', '手续费')
    print "| %10s |" % covert_btc(inps_sum), covert_btc(outs_sum), covert_btc(change_sum)
    print "-------" * 10

def ask_user():
    return None

def check_user(sign_tx):
    # show_transfer_info(sign_tx)
    answer = ask_user()
    if answer == 'yes':
        return True
    else:
        return False

def show_url(tx):
    tx_hash = txhash(tx)
    url = 'http://qukuai.com/tx/' + tx_hash
    print "your can visit %s to see" %url

def broadcast(sign_tx):
    # if check_user(sign_tx):
    pushtx(sign_tx)
    show_url(sign_tx)

if __name__ == "__main__":
    import sys
    args = sys.argv
    broadcast(args[1])

# demo
"""

python broadcast.py 01000000025e46552eb977f908fa8b3ee9d2943a8fa6d96c3b768a5f250ce485acd8c7f797000000008b483045022100dd29d89a28451febb990fb1dafa21245b105140083ced315ebcdea187572b3990220713f2e554f384d29d7abfedf39f0eb92afba0ef46f374e49d43a728a0ff6046e01410420f34c2786b4bae593e22596631b025f3ff46e200fc1d4b52ef49bbdc2ed00b26c584b7e32523fb01be2294a1f8a5eb0cf71a203cc034ced46ea92a8df16c6e9ffffffff71d1abe4352100d4d837ca96c1a16947b5444f0f3e0bc645c430f704bb06c84c0100000000ffffffff01905f0100000000001976a9143ec6c3ed8dfc3ceabcc1cbdb0c5aef4e2d02873c88ac00000000

python broadcast.py 0100000008ff042f0457a99613ed034f5e9e7cef893eb1b8a6ef251a038d531fccdc9664ea000000008a47304402202f51dbe3115b4fcac507cb25feb67713549c6dd3c12ef31d1ebf55ba1926c476022023cc29847fdbf19820746255979a6efc9f7667ac54f59fd7048bf69b4ed694a501410420f34c2786b4bae593e22596631b025f3ff46e200fc1d4b52ef49bbdc2ed00b26c584b7e32523fb01be2294a1f8a5eb0cf71a203cc034ced46ea92a8df16c6e9ffffffff84c5ebfa6fc3f270f86733f0ea070da5232f4a35f161ce987ab807dcb9f881b5000000008b483045022100dcfdc15ba33ab439ccc46bd92097fe57101e9fe0f7b1aabd738257843e5d5a570220306b6edbe3f8e096a2fac23e29db582e4058b0fd1bba650a4add52faca33b16001410420f34c2786b4bae593e22596631b025f3ff46e200fc1d4b52ef49bbdc2ed00b26c584b7e32523fb01be2294a1f8a5eb0cf71a203cc034ced46ea92a8df16c6e9ffffffffe1653f145f430703fd05829e6e03913bbc3f55ccf068a49f80a36685bf530972000000008b4830450221008bed2155eed50140dac923f464496428dae2f98d1df533e4bcabc5632f6831fd022033307b01c7f0c1848371862059c37c36002351356df7f9ea7befd4cae615617b01410420f34c2786b4bae593e22596631b025f3ff46e200fc1d4b52ef49bbdc2ed00b26c584b7e32523fb01be2294a1f8a5eb0cf71a203cc034ced46ea92a8df16c6e9fffffffffd7c16da449588224fc40f9e75a12857183bee594df47e4600725d35ee34bfb7000000008b4830450221009f3b6bffcd3fb26e8590db6ffa6ec7ddb23044c2b21aa7b48e2571c1ca9ff58702206fdab144be7cf4eb0ddff372d0f4e1243bfee142bff2402fdc69847e1fee702501410420f34c2786b4bae593e22596631b025f3ff46e200fc1d4b52ef49bbdc2ed00b26c584b7e32523fb01be2294a1f8a5eb0cf71a203cc034ced46ea92a8df16c6e9fffffffffd9fdcffca7f3345949ab01d131eb5362b890bece8abd1b88a16632555f72e1b000000008b4830450221008d8263d33b6e8c0775460302024bdf26931d124aaae87e6526dfa74483680afc02206cfe8adca35f9feab36994b330e94e49c85689a51648624563e7482860dd6fe001410420f34c2786b4bae593e22596631b025f3ff46e200fc1d4b52ef49bbdc2ed00b26c584b7e32523fb01be2294a1f8a5eb0cf71a203cc034ced46ea92a8df16c6e9ffffffffa8b85b635371ce42131f67a9ba0201cc711db5ef9f1ae3e26c957e851d772c96000000008a4730440220704926f7662626f2d3e97703e275116f9ba75b10469aa75ac1b58683ef0d9f40022022d78dfd9214eb7d99f676511327fdbfa93818e10ddf2abd97c5706a018aa5b401410420f34c2786b4bae593e22596631b025f3ff46e200fc1d4b52ef49bbdc2ed00b26c584b7e32523fb01be2294a1f8a5eb0cf71a203cc034ced46ea92a8df16c6e9ffffffff473ca23e17d805c5434ab4e2e694a44d046e0a2e41b42dfa6b70a9b908f0ece0000000008b4830450221008d0a970e14fcdbc9d6146112927ab4d40f04b1afda4a24d5703a93f625adb1b0022001e6343877fcdfdc72b29f4e21fe3519d73c02c0d360654d8a6a0cc8aeeded6a01410420f34c2786b4bae593e22596631b025f3ff46e200fc1d4b52ef49bbdc2ed00b26c584b7e32523fb01be2294a1f8a5eb0cf71a203cc034ced46ea92a8df16c6e9ffffffffa4b1ed0b747587884af16eed29af9bd29639f7d640a1827661499f9c68ecea22000000008b483045022100a18bbd447ce3f8fa7e15b7c36f26f31f49284d1000906d9f738ba5946f4cddca02207b07bdb0df91b9d31675d3367e65602e753e08607cef183668e9ef3be71c183001410420f34c2786b4bae593e22596631b025f3ff46e200fc1d4b52ef49bbdc2ed00b26c584b7e32523fb01be2294a1f8a5eb0cf71a203cc034ced46ea92a8df16c6e9ffffffff0200e40b54020000001976a914e314a5c994280c29b3123e5af2c5f0bd5fe6d3b388ac8b1f9c22000000001976a914536ffa992491508dca0354e52f32a3a7a679a53a88ac00000000
"""
