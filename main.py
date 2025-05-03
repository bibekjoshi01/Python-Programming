if __name__ == '__main__':
    print('Hello')

    li1 = [1, 2, 3]
    li2 = li1.copy()
    li3 = li1[:]
    li4 = list(li1)
    li2[0] = 3
    print(li1)