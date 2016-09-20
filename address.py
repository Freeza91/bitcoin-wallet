# -*- coding: utf-8 -*-

from bitcoin.transaction import privkey_to_address

# my address: 1JYDAbfNCC7UdSWh2VSbCWHEWnchurHsbc

if __name__ == "__main__":
    import sys
    args = sys.argv
    privkey = args[1]

    print "privkey is: ", privkey
    print 'address is : ', privkey_to_address(privkey)


