def jumpingOnClouds(c):
    count = 0
    i = 0
    while i < len(c) - 2:
        if c[i + 2] == 0:
            i += 2
        else:
            i += 1
        count += 1

    if i != len(c) - 1:
        count += 1
    return count

if __name__=='__main__':
    c = [0, 1, 0, 0, 0, 1, 0]
    n = [0, 0, 0, 1, 0, 0]

    print(jumpingOnClouds(n))