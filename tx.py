# -*- coding: utf-8 -*-

from bitcoin import unspent, mktx
from decimal import Decimal

def covert_satoshis(amount):
    return int(Decimal(amount) * 10000 * 10000)

def select_outputs(unspent_list, value, fee):
    # 如果是空的话认为是失败了。
    if not unspent_list: return None, 0
    # 分割成两个列表。
    min_value = covert_satoshis(value) + covert_satoshis(fee)
    lessers = [utxo for utxo in unspent_list if utxo.value < min_value]
    greaters = [utxo for utxo in unspent_list if utxo.value >= min_value]
    key_func = lambda utxo: utxo.value
    if greaters:
        # 非空。寻找最小的greater。
        min_greater = min(greaters)
        change = min_greater.value - min_value
        return [min_greater], change
    # 没有找到greaters。重新尝试若干更小的。
    # 从大到小排序。我们需要尽可能地使用最小的输入量。
    lessers.sort(key=key_func, reverse=True)
    result = []
    accum = 0
    for utxo in lessers:
        result.append(utxo)
        accum += utxo.value
        if accum >= min_value:
            change = accum - min_value
            return result, change
        # 没有找到。
    return None, 0

def build_tx_params(inputs, target_addr, change_addr, value, change_value):
    outputs = [{'address' : target_value, 'value' : value}, {'address': change_addr, 'value': change_value}]

def trade(sender_addr, target_addr, value, fee=0.0002):
    # unspent_outputs = unspent(sender_addr)
    unspent_outputs = unspent(sender_addr)
    inputs_list, change = select_outputs(unspent_outputs, value, fee)
    if inputs_list:
        inputs, outputs = build_tx_params(inputs_list, target_addr, value, change)
        tx = mktx(inputs, outputs)
        print "tx is : ---->>>"
        print "-----" * 30
        print tx
        print "tx hash is: ----->>>>"
        print "-----" * 30
        print tx_hash(tx)

# if __name__ == "__main__" :
#     import sys
#     args = sys.argv
#     if len(args) < 3:
#         print '参数不够'
#     elif len(args) == 3:
#         trade(args[0], args[1], args[2])
#     else:
#         trade(args[0], args[1], args[2], args[3])

trade('18cBEMRxXHqzWWCxZNtU91F5sbUNKhL5PX', '1Mhh8Aem3kXM3E6rizfDof67dYiY9C4wBy', 100)
