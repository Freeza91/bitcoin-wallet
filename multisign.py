from bitcoin import *

priv1 = 'xx1'
pub1 = privtopub(priv1)
priv2 = 'xx2'
pub2 = privtopub(priv2)
priv3 = 'xx3'
pub3 = privtopub(priv3)

script = mk_multisig_script([pub1, pub2, pub3], 2, 3)
addr = scriptaddr(script)
print addr

ins = [{'output': '5c99c1633f5aacd138ed646a86d08d05a48fc3471a55dca7bd943ddf165cf4ed:0', 'value': 1030000}]
outs = [{'value': 1020000, 'address': '1GwaiEyCE3gwFcf9o9borxRqFb5XqxK17h'}]

tx = mktx(ins, outs)
print deserialize(tx)

sig1_0_0 = multisign(tx, 0, script, priv1)
sig2_0_0 = multisign(tx, 0, script, priv2)
sig3_0_0 = multisign(tx, 0, script, priv3)

# 有顺序限制
# tx = apply_multisignatures(tx, 0, script, [sig1_0_0, sig2_0_0])
# tx = apply_multisignatures(tx, 0, script, [sig2_0_0, sig3_0_0])
print tx
print pushtx(tx)
