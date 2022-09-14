if 1:  
   my_int=int(input("Line:\t"))
   c, spc, nl, res, mt = chr(42), chr(32), chr(10), '', ''
   for i in range(my_int-1, -1, -1):
        a, b = (my_int - (i+1))*spc, c + i*spc
        res += a + 2*b + c + a + (nl if i else mt)
        print(res + nl + (2*my_int + 1)*c + nl + res[::-1])


