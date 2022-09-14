if 1:
    size=int(input("Leg:\t"))
    row, height = "{0}*{1}**\n", 2 * size
    res, spc, usc = "", chr(32), chr(42)
    for i in range(height):
        if i == size:
            res += row.format(size * spc, height * usc)
        else:
            res += row.format((height-i) * spc, i * 2*spc)
    print(res)
