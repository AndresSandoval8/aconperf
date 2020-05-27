def closed_tube(a, n, l):
    remainder = (n / 2 - int(n / 2)) * 2
    print(remainder)
    if remainder is 1:
        print("WARNING: Harmonic input to closed tube function should be an odd integer!")

    frequency = n * a / (4 * l)
    return frequency


def open_tube(a, n, l):
    frequency = n * a / (2 * l)
    return frequency

