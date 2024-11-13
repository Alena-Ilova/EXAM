def is_power(n, base):
    if base <= 1:
          return n == 1

    while n > 1:
        if n % base != 0:
            return False
        n //= base 
    return n == 1

print(is_power(16, 2))
print(is_power(12, 2))
print(is_power(100000, 10))
print(is_power(990, 9))