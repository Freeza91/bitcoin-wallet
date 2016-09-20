# -*- coding: utf-8 -*-

from bitcoin.bci import unspent
from bitcoin.transaction import mktx, deserialize

from decimal import Decimal

def covert_satoshis(amount):
    return int(Decimal(amount) * 10000 * 10000)

def select_outputs(unspent_list, value, fee):
    # 如果是空的话认为是失败了。
    if not unspent_list: return None, 0
    # 分割成两个列表。

    min_value = value + fee
    lessers = [utxo for utxo in unspent_list if utxo['value'] < min_value]
    greaters = [utxo for utxo in unspent_list if utxo['value'] >= min_value]
    if greaters:
        # 非空。寻找最小的greater。
        min_greater = min(greaters, key=lambda greaters: greaters['value'])
        change = min_greater['value'] - min_value
        return [min_greater], change
    # 没有找到greaters。重新尝试若干更小的。
    # 从大到小排序。我们需要尽可能地使用最小的输入量。
    key_func = lambda utxo: utxo['value']
    lessers.sort(key=key_func, reverse=True)
    result = []
    accum = 0
    for utxo in lessers:
        result.append(utxo)
        accum += utxo['value']
        if accum >= min_value:
            change = accum - min_value
            return result, change
        # 没有找到。
    return None, 0

def build_tx_params(target_addr, value, change_addr, change_value):
    return [{'address' : target_addr, 'value' : value}, {'address': change_addr, 'value': change_value}]

def trade(sender_addr, target_addr, value, fee=0.0002):
    # unspent_outputs = unspent(sender_addr)
    unspent_outputs = unspent(sender_addr)
    satoshis_value = covert_satoshis(value)
    satoshis_fee = covert_satoshis(fee)
    inputs, change = select_outputs(unspent_outputs, satoshis_value, satoshis_fee)
    if inputs:
        outputs = build_tx_params(target_addr, satoshis_value, sender_addr, change)
        tx = mktx(inputs, outputs)
        print "构建的建议信息是："
        print "由%s --->>> %s转账%sBTC, 手续费为%sBTC" %(sender_addr, target_addr, value, fee)
        print "-----" * 30
        print tx
        print "#####" * 30
        print deserialize(tx)
        print "*****" * 30

if __name__ == "__main__" :
    import sys
    args = sys.argv
    if len(args) <= 3:
        print '参数不够'
    elif len(args) == 4:
        trade(args[1], args[2], args[3])
    else:
        trade(args[1], args[2], args[3], args[4])

# demo1
"""
python tx.py 18cBEMRxXHqzWWCxZNtU91F5sbUNKhL5PX 1Mhh8Aem3kXM3E6rizfDof67dYiY9C4wBy 100


python tx.py 18cBEMRxXHqzWWCxZNtU91F5sbUNKhL5PX 1Mhh8Aem3kXM3E6rizfDof67dYiY9C4wBy 100 0.0001

"""

# demo2

"""

trade('18cBEMRxXHqzWWCxZNtU91F5sbUNKhL5PX', '1Mhh8Aem3kXM3E6rizfDof67dYiY9C4wBy', 100)


trade('18cBEMRxXHqzWWCxZNtU91F5sbUNKhL5PX', '1Mhh8Aem3kXM3E6rizfDof67dYiY9C4wBy', 100, 0.002)

"""
