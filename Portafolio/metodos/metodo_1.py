from timeit import Timer

print(9999**99)

print(Timer("99**99").timeit())


print(Timer('a,b = b,a', 'a=1; b=2').timeit())