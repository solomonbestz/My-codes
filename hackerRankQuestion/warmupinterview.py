def jumpingOnClouds(c):
    count = 0
    i = 0
    while i < len(c) - 1:
        if c[i + 2] == 1 or i + 2 >= len(c):
            i += 1
            count += 1 
        else:
            i += 2
            count += 1
    return count

if __name__=='__main__':
    c = [0, 1, 0, 0, 0, 1, 0]

    print(jumpingOnClouds(c))