def verify(digits):
    sum = 0
    digits = [int(i) for i in digits]
    first = digits.pop()
    i = 0
    for d in digits[::-1]:
        muliplier = 1
        if i % 2 == 0:
            muliplier = 2
        x = int(d) * muliplier
        if x > 9:
            x -= 9
        sum += x
        i += 1

    return first == ((10 - (sum % 10)) % 10)

print(verify('17893729974'))
