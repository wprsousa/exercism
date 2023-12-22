def square(number):
    index = 0
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")

    for _ in range(number):
        if index == 0:
            index += 1
            continue
        if index == 1:
            index += 1
            continue
        index *= 2
    return index


def total():
    total_chess = square(64)

    return (total_chess * 2) - 1


