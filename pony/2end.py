class Arithmetic(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q  

    def __add__(self, r):
        return Arithmetic(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Arithmetic(self.p*r.q-self.q*r.p,self.q*r.q)

    def __mul__(self, r):
        return Arithmetic(self.p*r.p,self.q*r.q)
    
    def __div__(self, r):
        return Arithmetic(self.p*r.q,self.q*r.p)

    def __str__(self):
        if self.p >self.q:
            count = self.q
        else:
            count = self.p
        def f(c):
            num = 0
            for n in range(0,c-1):
                a = self.p/(c-n)
                b = self.q/(c-n)
                if a*(c-n) == self.p and b*(c-n) == self.q:
                    num = 1
                    self.p,self.q = self.p/(c-n),self.q/(c-n)
                    c = c/(c -n)
                    break
            if num == 1:
                return f(c)
            else:
                if self.q == 1:
                    return '%s'%(self.p)
                return '%s/%s'%(self.p,self.q)
        return f(count)




r1 = raw_input()
if not ' ' in r1:
    r1up = r1.split('/')[0]
    r1down = r1.split('/')[-1]
    r1Num = Arithmetic(r1up, r1up)
else:
    r1down = r1.split('/')[-1]
    r1up = abs(int(r1.split(' ')[0]))*int(r1down) + int((r1.split(' ')[-1]).split('/')[0])
    r1Num = Arithmetic(int(r1up), int(r1down))
    
if '-' in r1:
    r1Num = Arithmetic((-1)*int(r1up), int(r1down))
else:
    r1Num = r1Num


signal = raw_input()

r2 = raw_input()
if not ' ' in r2:
    r2up = r2.split('/')[0]
    r2down = r2.split('/')[-1]
    r2Num = Arithmetic(int(r2up), int(r2down))
else:
    r2down = r2.split('/')[-1]
    r2up = abs(int(r2.split(' ')[0]))*int(r2down) + int((r2.split(' ')[-1]).split('/')[0])
    r2Num = Arithmetic(int(r2up), int(r2down))
    
if '-' in r2:
    r2Num = Arithmetic((-1)*int(r2up), int(r2down))
else:
    r2Num = r2Num

if '+' == signal:
    result = str(r1Num + r2Num)
if '-' == signal:
    result = str(r1Num - r2Num)
if '*' == signal:
    result = str(r1Num * r2Num)
if '/' == signal:
    result = str(r1Num / r2Num)

fenzi = abs(int(result.split('/')[0]))
fenmu = int(result.split('/')[-1])
zhengshu = fenzi // fenmu
zhenfenzi = fenzi - zhengshu * fenmu
for i in range(1, min(fenmu, zhenfenzi)):
    if fenmu%i == 0 and zhenfenzi%i == 0:
        zhenfenzi = zhenfenzi/i
        fenmu = fenmu/i
if not '-' in result.split('/')[0]:
    if zhengshu > 0:
        print(str(zhengshu) + ' ' + str(zhenfenzi)+'/'+str(fenmu))
    else:
        print(str(zhenfenzi)+'/'+str(fenmu))
else:
    if zhengshu > 0:
        print('-' + str(zhengshu) + ' ' + str(zhenfenzi)+'/'+str(fenmu))
    else:
        print('-' + str(zhenfenzi)+'/'+str(fenmu))


