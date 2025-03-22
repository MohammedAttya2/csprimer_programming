def verify(digits):
    digits = [int(i) for i in digits]
    sum = digits.pop()
    i = 0
    for d in digits[::-1]:
        muliplier = 2 - (i % 2)
        x = int(d) * muliplier
        sum += x + x // 10
        i += 1

    return sum % 10 == 0

assert verify('17893729974')
assert not verify('17893729973')
