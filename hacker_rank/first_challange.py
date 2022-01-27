
# FUnction to calculate pairs of socks
def sock_marchent(socks):
    pair_of_socks = []
    length = 0
    for pairs in socks:
        if pairs in pair_of_socks: pair_of_socks.remove(pairs); length += 1
        else: pair_of_socks.append(pairs)
    return length
            

if __name__ == "__main__":
    socks = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    socks_2 = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
    print(sock_marchent(socks_2))