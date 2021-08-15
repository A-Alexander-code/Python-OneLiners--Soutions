# The data
l = [3, 6, 14, 16, 33, 55, 56, 89]
x = 56

# The one-liner
bs = lambda l,x, lo, hi: -1 if lo>hi else\
    (lo+hi)//2 if l[(lo+hi)//2] == x else\
    bs(l, x, lo, (lo+hi)//2-1) if l[(l+hi)//2] > x else\
    bs(l,x,(lo+hi)//2+1, hi)

# The result
print(bs(l,x,0,len(l)-1))