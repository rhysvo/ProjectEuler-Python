for x in range(1, 1000):
    for y in range(x, 1000):
        z = 1000 - x - y
        if z > 0:
            if x*x + y*y == z*z:
                print(x*y*z)


