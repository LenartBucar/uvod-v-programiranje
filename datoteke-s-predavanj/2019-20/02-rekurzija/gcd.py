def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

#  m         n   m % n
#  |         |     |
#  v         v     v
# 256 = 0 * 720 + 256
# 720 = 2 * 256 + 208
# 256 = 1 * 208 +  48
# 208 = 4 *  48 +  16
#  48 = 3 *  16 +   0
#  16 = 0 *  0  +  16
#  ^
#  |
# gcd(m, n)
