import math
import sys

# Current path position:
g_posR = 0 # row position
g_posC = 0 # column position

# Current path direction:
g_dirR = 0 # row direction 
g_dirC = 0 # column direction 

# Current path borders:
g_borderL = 0 # left column 
g_borderT = 0 # top row
g_borderR = 0 # right column 
g_borderB = 0 # bottom row 

grid = [] # holds matrix 


def fillTableForEncrypt(letters, totalRows, totalCols):

    for i in range(math.ceil(len(letters) / totalCols)):
        rows = []
        for j in range(totalCols):
            if i * totalCols + j < len(letters):
                rows.append(letters[i * totalCols + j])
            else:
                rows.append('-')
        grid.append(rows)
    
   # for i in grid:
   #     print(i)

    return grid


def fillTableForDecrypt(letters, totalRows, totalCols, pathtype):
    """creates decryption matrix"""
    global g_posR, g_posC
    newGrid = []

    for i in range(math.ceil(len(letters) / totalCols)):
        rows = []
        for j in range(totalCols):
            if i * totalCols + j < len(letters):
                rows.append(letters[i * totalCols + j])
            else:
                rows.append('-')
        newGrid.append(rows)

    initPathParameters(pathtype, totalRows, totalCols)
    pos = 0
    while pos < totalRows * totalCols:
        newGrid[g_posR][g_posC] = letters[pos]
        makeOneStep(pathtype)
        pos += 1

    return newGrid


def readCipherText(grid, totalRows, totalCols, pathtype):
    initPathParameters(pathtype, totalRows, totalCols)
    global g_posR, g_posC
    cipher_text = ""

    while len(cipher_text) < totalRows * totalCols:
        cipher_text += grid[g_posR][g_posC]
        makeOneStep(pathtype)

    return cipher_text


def readPlainText(matrix, totalRows, totalCols):
    plain_text = ""
    for i in range(totalRows):
        for j in range(totalCols):
            plain_text += str(matrix[i][j])

    return plain_text


def initPathParameters(pathtype, totalRows, totalCols):
    global g_posR, g_posC, g_borderL, g_borderT, g_borderR, g_borderB, g_dirR, g_dirC
    g_posR = 0 # current row position
    g_posC = totalCols - 1 # current column position

    g_borderL = 0
    g_borderT = 0
    g_borderR = totalCols - 1
    g_borderB = totalRows - 1

    if pathtype == "clockwise":
        g_dirR = 1 
        g_dirC = 0
    elif pathtype == "anticlockwise":
        g_dirR = 0
        g_dirC = -1
   
def makeOneStep(pathtype):
    global g_posR, g_posC, g_borderL, g_borderT, g_borderR, g_borderB, g_dirR, g_dirC

    if g_posR + g_dirR >= g_borderT and g_posR + g_dirR <= g_borderB:
        g_posR += g_dirR # row position
    else:
        if g_dirR == 1:
            if pathtype == "clockwise":
                g_dirR = 0
                g_dirC = -1
                g_borderR -= 1
            elif pathtype == "anticlockwise":
                g_dirR = 0
                g_dirC = 1
                g_borderL += 1
        elif g_dirR == -1:
            if pathtype == "clockwise":
                g_dirR = 0
                g_dirC = 1
                g_borderL += 1
            elif pathtype == "anticlockwise":
                g_dirR = 0
                g_dirC = -1
                g_borderR -= 1


    if g_posC + g_dirC >= g_borderL and g_posC + g_dirC <= g_borderR:
        g_posC += g_dirC # column position
    else:
        if g_dirC == 1:
            if pathtype == "clockwise":
                g_dirR = 1
                g_dirC = 0
                g_borderT += 1
            elif pathtype == "anticlockwise":
                g_dirR = -1
                g_dirC = 0
                g_borderB -= 1
        else:
            if pathtype == "clockwise":
                g_dirR = -1
                g_dirC = 0
                g_borderB -= 1
            elif pathtype == "anticlockwise":
                g_dirR = 1
                g_dirC = 0
                g_borderT += 1

        g_posR += g_dirR


def main():
    ans = True
    additional_Path = ""


    while ans:
        option = input(
            """Please select the desired route path.\n[1]. clockwise\n[2]. anticlockwise\n[3]. Spiraling inside out\n[4]. add Top-to-Bottom\n\n>>> """)
        if option == "1": # clockwise 
            pathtype = "clockwise"
            route_size = int(input("Please enter a route size: "))
            plain_text = input("Please enter the desired text for encryption/decryption: ")
            ans = False
        elif option == "2": # counter clockwise 
            pathtype = "anticlockwise"
            route_size = int(input("Please enter a route size: "))
            plain_text = input("Please enter the desired text for encryption/decryption: ")
            ans = False
        elif option == "3": # spiraling inside out
            pathtype = "clockwise"
            additional_Path = "spiraling"
            route_size = int(input("Please enter a route size: "))
            plain_text = input("Please enter the desired text for encryption/decryption: ")
            ans = False

    totalCols = route_size
    totalRows = len(plain_text) / totalCols

    if totalRows != math.floor(totalRows):
        totalRows = math.floor(totalRows) + 1
    elif type(totalRows) is float:
        totalRows = len(plain_text) // totalCols

    print("Selected path type:" , pathtype)
    print("Total Columns:", totalCols)
    print("Total Rows:", totalRows)

    grid = fillTableForEncrypt(plain_text, totalRows, totalCols)
    encryptedText = readCipherText(grid, totalRows, totalCols, pathtype)
    

    new_grid = []
    if totalRows != math.floor(totalRows):
        print("The length does not match the table dimensions.")
        sys.exit(0)
    else:
        new_grid = fillTableForDecrypt(encryptedText, totalRows, totalCols, pathtype)
        decryptedText = readPlainText(new_grid, totalRows, totalCols)
        if additional_Path == "spiraling":
            print("Encrypted Text: ", encryptedText[::-1])
            print("Decrypted Text: ", decryptedText[::1])
        else:
            print("Encrypted Text: ", encryptedText)
            print("Decrypted Text: ", decryptedText)


if __name__ == "__main__":
    main()
