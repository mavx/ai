from __future__ import print_function # Python 2/3 compatibility
import random

# Define squares
def play():
    win = [
        set([1, 2, 3]),
        set([4, 5, 6]),
        set([7, 8, 9]),
        set([1, 5, 9]),
        set([1, 4, 7]),
        set([2, 5, 8]),
        set([3, 6, 9]),
        set([3, 5, 7])
    ]
    options = list(range(1,10))
    p1 = []
    p2 = []

    while len(options) > 0:
        # print(options)
        x = random.choice(options)
        p1.append(x)
        options.remove(x)

        if len(p1) > 2:
            if any(set(s).issubset(p1) for s in win):
                # combo, result = [p1, p2], 1
                result = [p1, p2, 1]
                break

        if len(options) > 0:
            y = random.choice(options)
            p2.append(y)
            options.remove(y)

            if len(p2) > 2:
                if any(set(s).issubset(p2) for s in win):
                    result = [p1, p2, -1]
                    break
        else:
            result = [p1, p2, 0]
            break

    return result


def main():
    sample = []
    x = 0
    while x < 100:
        sample.append(play())
        x += 1
    
    for s in sample:
        print(s)


if __name__ == '__main__':
    main()
