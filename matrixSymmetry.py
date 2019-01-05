def checkSymmetry(matrix):
    horizontal_symmetry = checkHorizontalSymmetry(matrix)
    vertical_symmetry = checkVerticalSymmetry(matrix)
    if(horizontal_symmetry and vertical_symmetry):
        print("horizontal and vertical symmetry")
    elif(horizontal_symmetry):
        print("horizontal symmetry")
    elif(vertical_symmetry):
        print("vertical symmetry")
    else:
        print("no symmetry")

def checkHorizontalSymmetry(matrix):
    #p[ [1,1,1],
    #   [1,1,1],
    #   [1,1,1]]
    length = len(matrix)
    symmetry = True
    for i in range(0,length):
        if(not symmetry):
            break
        for j in range(0,int(length/2)):
            if(matrix[i][j] != matrix[i][length-j-1]):
                symmetry = False
                break
    return symmetry

def checkVerticalSymmetry(matrix):
    length = len(matrix)
    symmetry = True
    for i in range(0,length):
        if(not symmetry):
            break
        for j in range(0,int(length/2)):
            if(matrix[j][i] != matrix[length-j-1][i]):
                symmetry = False
                break
    return symmetry
test_matrix = [[1,1,1],[1,1,1],[4,1,2]]
checkSymmetry(test_matrix)