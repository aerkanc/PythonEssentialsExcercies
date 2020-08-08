def fibonacci(n):
    if n < 0:
        raise Exception("n 0 dan büyük olmalıdır")
    if n in [0, 1]:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(0, 35):
    print("%d. fibonacci : %d" % (i, fibonacci(i)))
