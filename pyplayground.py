
def add(*args):
    res = 0
    for x in args:
        res += x
    return res

if __name__ == '__main__':
    print(add(1, 2, 3, 4, 5))
