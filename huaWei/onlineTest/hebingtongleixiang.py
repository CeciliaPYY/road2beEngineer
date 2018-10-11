def heBingBiaoDaShi(exp):
    fSplit = exp.split("+")
    sSplit = []
    for fS in fSplit:
        fS_index = fSplit.index(fS)
        if '-' in fS and fS[0] != '-':
            sSplit.append(fS.split('-')[0])
            for f in fS.split('-')[1:]:
                sSplit.append("-"+f)
            fSplit.pop(fS_index)

    for sS in sSplit:
        fSplit.append(sS)
    
    zhishu = []
    for fS in fSplit:
        zhishu.append(int(fS.split("^")[-1]))

    mici = dict.fromkeys([i for i in range(max(zhishu)+1)])
    for fS in fSplit:
        mici[int(fS[-1])] = 0
    for fS in fSplit:
        mici[int(fS[-1])] += int(fS.split("X")[0])

    mici = {k:v for k, v in mici.items() if v != None}
    mici = sorted(mici.items(), key = lambda x: x[0], reverse = True)

    xishu_list = []
    for k, v in mici:
        if v > 0:
            xishu_list.append("+{}X^{}".format(v,k))
        elif v == 0:
            continue
        else:
            xishu_list.append("{}X^{}".format(v,k))
        
    finalList = ''.join(xishu_list)

    if finalList[0] == '+':
        return finalList[1:]
    else:
        return finalList

if __name__ == "__main__":
    a = raw_input()
    if a == '':
        print('0')
    else:
        print(heBingBiaoDaShi(a))
    
