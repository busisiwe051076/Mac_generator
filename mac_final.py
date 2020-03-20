def gen_hex():
    for i in range(16**10):
        yield "{:06X}".format(i)
for s in gen_hex():
    pre="70-b3-d5-71-5a"
    m=pre+"-"+s[:2]+"-"+s[2:4]+"-"+s[4:6]
    print(m)
