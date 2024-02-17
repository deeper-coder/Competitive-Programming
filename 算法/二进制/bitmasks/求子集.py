# 获取集合tot的所有子集，包括空集和它本身
def get_subset(tot):
    sub = tot
    res = [tot]
    while sub:
        sub = (sub - 1) & tot
        res.append(sub)
    return res