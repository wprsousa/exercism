def equilateral(sides):
    a, b, c = sides[0], sides[1], sides[2]
    if a + b + c != 0:
        if a + b >= c and b + c >= a and a + c >= b:
            if a == b and b == c and c == a:
                return True
            return False
        return False
    return False


def isosceles(sides):
    a, b, c = sides[0], sides[1], sides[2]
    if a + b + c != 0:
        if a + b >= c and b + c >= a and a + c >= b:
            if a == b or b == c or c == a:
                return True
            return False
        return False
    return False


def scalene(sides):
    a, b, c = sides[0], sides[1], sides[2]
    if a + b + c != 0:
        if a + b >= c and b + c >= a and a + c >= b:
            if a != b and b != c and c != a:
                return True
            return False
        return False
    return False
