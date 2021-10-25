a = int(input('Enter lower range number: '))
b = int(input('Enter upper range number: '))

for x in range(a, b + 1):
    if x > 1:
        for y in range(2, x):
            if (x % y) == 0:
                break
        else:
            print(x)