listA = [[1,2,3],
        [4,5,6],
        [7,8,9]]

def CCw (listA):
    for i in range(len(listA)):
        if i == 0:
            tambah = 2
            for j in range(len(listA[i])):
                temp = int(listA[i][j])
                temp += tambah
                listA[i][j] = temp
                tambah += 2
        elif i == 1:
            tambah = -2
            for j in range(len(listA[i])):
                temp = int(listA[i][j])
                temp += tambah
                listA[i][j] = temp
                tambah += 2
        elif i == 2:
            tambah = -6
            for j in range(len(listA[i])):
                temp = int(listA[i][j])
                temp += tambah
                listA[i][j] = temp
                tambah += 2
    return listA

# [[3, 6, 9],
# [2, 5, 8],
# [1, 4, 7]]

print (CCw(listA))