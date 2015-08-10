def slices(nstr, n):
    if n > len(nstr) or n = 0:
        raise ValueError
    ran = range(len(nstr) - (n-1))
    return [list(map(int, x)) for x in [nstr[i:i+n] for i in ran]]

