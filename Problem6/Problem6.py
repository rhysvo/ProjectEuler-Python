
n = 0
for x in range(1, 101):
    n += (x * x)

m = 0
for x in range(1, 101):
    m += x
m = m * m

print(m-n)