def raise_to_power(base_num, pow_num):
    if pow_num < 0:
        print('invalid power vale')
        return 0
    result = 1
    for i in range(pow_num):
        result *= base_num
    return result

print(raise_to_power(3, 4))

