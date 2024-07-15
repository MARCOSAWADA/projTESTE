def trianlateral(num):
    num -= 1
    for i in range(num + 2):
        print("*" * i)

    for i in range(num):
        print("*" * (num - i))

trianlateral(4)