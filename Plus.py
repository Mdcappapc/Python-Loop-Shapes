def l(t):
    return s1 + c + t + c + s1 + w
n = int(input("Height:\t"))
c, s, w = chr(42), chr(32), chr(10)
sn, s1, s2, cn, c2 = s*n, (n+1)*s, (3*n+2)*s, c*n, (n+2)*c
l1 = c2 + sn + c2 + w
l2 = (n*(c + s2 + c + w))[:-1]
tmp = l(cn) + n*l(sn) + l1
res = tmp + l2 + tmp[::-1]
print(res)