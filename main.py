import math
import sys
import re

# Current path position:
g_posR = 0  # row position
g_posC = 0  # column position

# Current path direction:
g_dirR = 0  # row direction
g_dirC = 0  # column direction

# Current path borders:
g_borderL = 0  # left column
g_borderT = 0  # top row
g_borderR = 0  # right column
g_borderB = 0  # bottom row

grid = []  # holds matrix

# done
def fillTableForEncrypt(letters, totalRows, totalCols):
    """ creates an array to hold the plaintext and appends extra character """
    # creates a matrix using the text length divided by the total columns
    for number_of_rows in range(math.ceil(len(letters) / totalCols)):
        rows = []  # holds cipher text
        for index in range(totalCols): 
            if number_of_rows * totalCols + index < len(letters):
                rows.append(letters[number_of_rows * totalCols + index])
            else:
                # appends a - character if the matrix has empty spaces
                rows.append('-')
        grid.append(rows)  # appends newly formed matrix to grid

    return grid  # returns newly formed grid

#done 
def fillTableForDecrypt(letters, totalRows, totalCols, pathtype):
    """creates decryption matrix using the ciphertext"""
    global g_posR, g_posC  # current row position and and current column position
    newGrid = []  # holds decrypted grid

    # creates a matrix using the ciphertext length and total columns
    for number_of_rows in range(math.ceil(len(letters) / totalCols)):
        rows = []  # holds a decrypted text
        for index in range(totalCols):
            # appends cipher text to grid
            if number_of_rows * totalCols + index < len(letters):
                rows.append(letters[number_of_rows * totalCols + index])
            else:
                # appends a - character if the matrix has empty spaces
                rows.append('-') 
        newGrid.append(rows)  # appends newly formed matrix to grid

    initPathParameters(pathtype, totalRows, totalCols)  # sets the position of the row and column
    pos = 0  # position in the grid
    while pos < totalRows * totalCols:  # writes newly formed grid
        # using row position and grid position we create the new matrix
        newGrid[g_posR][g_posC] = letters[pos]
        # this function allow use to read the matrix based on the chosen path
        makeOneStep(pathtype)
        pos += 1  # increments by to add letters
    return newGrid  # returns newly formed grid holding the decrypted text

#done
def readCipherText(grid, totalRows, totalCols, pathtype):
    """reads the newly created cipher text"""
    initPathParameters(pathtype, totalRows, totalCols)  # sets the starting, direction, and path for the grid
    global g_posR, g_posC  # row position and column position
    cipher_text = ""  # holds created cipher text
    # appends the cipher text from the grid
    while len(cipher_text) < totalRows * totalCols:
        cipher_text += grid[g_posR][g_posC]
        print(g_posR,g_posC)
        makeOneStep(pathtype)  # moves position in the grid
    return cipher_text  # returns new created encrypted text

# done
def readPlainText(decryptedGrid, totalRows, totalCols):
    plain_text = "" # holds decryped text 
    for index in range(totalRows): # loops through rows number
        for element in range(totalCols): # loops through column number
            plain_text += str(decryptedGrid[index][element]) # appends characters from grid
    return plain_text # returns decrypted text

# done 
def initPathParameters(pathtype, totalRows, totalCols):
    global g_posR, g_posC, g_borderL, g_borderT, g_borderR, g_borderB, g_dirR, g_dirC
    g_posR = 0  # current row position
    g_posC = totalCols - 1  # current column position

    g_borderL = 0  # left side of the grid
    g_borderT = 0  # top side of the grid
    g_borderR = totalCols - 1  # right side of the grid
    g_borderB = totalRows - 1  # bottom side of the grid

    if pathtype == "clockwise":
        g_dirR = 1  # sets starting direction for the row
        g_dirC = 0  # sets starting direction for the column
    elif pathtype == "anticlockwise":
        g_dirR = 0 # sets starting direction for the row
        g_dirC = -1 # sets starting direction for the column

# done
def makeOneStep(pathtype):
    """moves position in grid"""
    # position, direction, and border values that determine movement through the grid
    global g_posR, g_posC, g_borderL, g_borderT, g_borderR, g_borderB, g_dirR, g_dirC

    # determines if we will move a position in a row 
    if g_posR + g_dirR >= g_borderT and g_posR + g_dirR <= g_borderB:
        g_posR += g_dirR  # increments position in a row
    else: 
        if g_dirR == 1: 
            if pathtype == "clockwise":  # moves down the grid
                # theses values are used to move down a column
                g_dirR = 0 # sets to top row 
                g_dirC = -1 # moves down column
                g_borderR -= 1 # decrements by 1 to move down the right side column
            elif pathtype == "anticlockwise": 
                # sets values to move down the left side
                g_dirR = 0  # sets to top row 
                g_dirC = 1  # moves up column
                g_borderL += 1 # increments to move down the column
        elif g_dirR == -1:
            # reads up left side column
            if pathtype == "clockwise":
                g_dirR = 0 # sets to top row
                g_dirC = 1 # moves up column
                g_borderL += 1 # increments by one to read up the grid 
            # reads down the middle of the grid
            elif pathtype == "anticlockwise":
                g_dirR = 0 # set to top row
                g_dirC = -1 # moves down column
                g_borderR -= 1 # decrements by 1 to move down

    # checks the position within a column and determines next position 
    if g_posC + g_dirC >= g_borderL and g_posC + g_dirC <= g_borderR:
        g_posC += g_dirC 
    else:
        if g_dirC == 1: # checks fir current direction
            if pathtype == "clockwise":  
                 # moves right on the top row
                g_dirR = 1 # sets to middle row
                g_dirC = 0 # sets to 
                g_borderT += 1 # increments by one to move right 
            elif pathtype == "anticlockwise":
                # moves down middle column
                g_dirR = -1 # decrement to move down the rows
                g_dirC = 0 # sets to first column 
                g_borderB -= 1 
        else:
            if pathtype == "clockwise": 
                # moves down middle column
                g_dirR = -1 # decrement to move down the rows
                g_dirC = 0 # sets to first column
                g_borderB -= 1 # reads bottom border
            elif pathtype == "anticlockwise":
                # moves down middle column
                g_dirR = 1 # sets to second row
                g_dirC = 0 # sets to first column 
                g_borderT += 1 # reads top row


        g_posR += g_dirR # increment to add new row position

# done
def menuCheck(questions):
    """checks input from user and repeats questions if a error is encountered"""
    values = ""  # holds user input
    while True:
        user_input = input(questions)
        user_input = user_input.replace(" ", "")  # removes spaces
        if len(user_input) == 0 or user_input == "1" or user_input == "0":  # checks for no input o correct route size
            print("Error! No input detected or insufficient route size. ")
        # if only letters are entered or special characters
        elif re.match("^[A-Za-z0-9_-]*$", user_input):
            values = user_input  # assigns text from user input
            break  # stops question loop
    return values  # returns user input

# done
def grouping(plain_text, totalCols):
    """creates matrix from the plaintext that is used to encrypt and decrypt"""
    if len(plain_text) % totalCols == 0:  # checks if there are extra spaces
        return [plain_text[rows*totalCols:rows*totalCols+totalCols] for rows in range(len(plain_text)//totalCols)]
    else:  # adds a column if there is a remainder
        return [plain_text[rows*totalCols:rows*totalCols+totalCols] for rows in range(len(plain_text)//totalCols+1)]


def topToBottom(plaintext, route_size, decrypt=False):
    """Encrypts/Decrypts from top to bottom"""
    while len(plaintext) % route_size != 0: # appends a - charater of there is extra spaces 
        plaintext += "-"

    if decrypt == False: # encryption process
        grid = grouping(plaintext, route_size) # receives newly formed grid
        encrypted_text = "" # holds encrypted text
        pos = 0 # position in grid
        while pos < route_size: # repeats the step through of the grid based on the route size
            rows = [] # holds encrypted grid
            for index in grid: # reads top to bottom
                rows.append(index[pos]) # appends characters from grid
            if pos % 2 == 1: # checks for new column
                rows.reverse() # revese reading pattern to read bottom to top
            encrypted_text += "".join(rows) # appends newly encrypted text
            pos += 1 # appends by one to shift postions
        return encrypted_text # returns newly encrypted text to main

    if decrypt == True: # decryption process
        size = len(plaintext) // route_size # gets size of text
        grid = grouping(plaintext, size) # receives grid from grouping function
        decrypted_text = "" # holds decrypted text
        for passthru in range(size): # loops through grid 
            for pos, letters in enumerate(grid): # gets position and letters
                if pos % 2 == 0: 
                    # reads characters from grid
                    char = letters[0] # assigns character
                    grid[pos] = letters[1:] # reads first characters
                if pos % 2 == 1: # shifts column
                    char = letters[-1] # reads last character
                    grid[pos] = letters[:-1] # reads in a reverse pattern
                decrypted_text += char # append read character

        return decrypted_text # returns decrypted text back to main


def main():
    # question that asks for the preferred path types
    pathOptions = """Please select the desired route path.^[1]. clockwise\n[2]. anticlockwise\n[3]. Spiraling inside out\n[4]. Top-to-Bottom\n\n>>> """
    # question that asks for the route size number
    routeSizeChoice = "\nPlease enter a route size above 1: "
    # question that asks for the text that will be encrypted/decrypted
    getPlaintext = "Please enter the desired text for encryption/decryption: "

    # sets path type based on user input 
    while True:
        choice = input(pathOptions) # getting users choice for pathtype 
        if choice == "1": # clockwise path 
            pathtype = "clockwise" # set path type to clockwise
            break 
        elif choice == "2": # counter clockwise path 
            pathtype = "anticlockwise"  # set counterclockwise path 
            break
        elif choice == "3": # inside out path 
            pathtype = "clockwise" # sets clockwise path 
            break
        elif choice == "4": # top to bottom path
            pathtype = "Top-to-Bottom" # sets top to bottom path
            break
        else:
            # prints error if 1-4 choices are not entered 
            print('Invalid input: Please enter one of the choices listed above.\n')

    try:
        # catches any input error or any incorrect value assignment from the menuCheck function
        route_size = menuCheck(routeSizeChoice) # assigns the route size that the user entered
        totalCols = int(route_size) # assigns total columns 
    except Exception as e: # checks for errors for value assignment
        # if there are any errors then a error message is printed
        # notifying the user and rerunning menuCheck function
        print("A errors has occurred: ",e) 
        print("Rerunning program.........")
        route_size = menuCheck(routeSizeChoice) 

    plain_text = menuCheck(getPlaintext)  # assigns the word that the user entered
    totalRows = len(plain_text) / totalCols # assigns rows based on text length and route size
 
    if totalRows != math.floor(totalRows): # adds a extra row 
        totalRows = math.floor(totalRows) + 1 # adds 1 to totalRows if any extra spaces
    elif type(totalRows) is float:  # if rows is a decimal value
        totalRows = len(plain_text) // totalCols # rounds to the nearest whole number

    new_grid = [] # holds the grid containing the plaintext characters 

    if choice == "1" or choice == "2" or choice == "3": # checks for 1,2,3 
        # calls the fillTaleForEncrypt to create the grid out of the plantext characters
        # calls the readCipherText to read the grid in the chosen path and return the ciphertext
        grid = fillTableForEncrypt(plain_text, totalRows, totalCols) 
        encryptedText = readCipherText(grid, totalRows, totalCols, pathtype)
        # fillTableForDecrypt is called to create a grid out the cipher text
        # readPlainText reads the decrypted text 
        new_grid = fillTableForDecrypt(encryptedText, totalRows, totalCols, pathtype)
        decryptedText = readPlainText(new_grid, totalRows, totalCols)
    elif choice == "4": # checks if user chooses 4 the top to bottom is printed
        encryptedText = topToBottom(plain_text, totalCols)
        decryptedText = topToBottom(encryptedText, totalCols, decrypt=True)

    # prints the 1,2,4 results 
    if choice == "1" or choice == "2" or choice == "4":
        print("Encrypted Text: ", encryptedText)
        print("Decrypted Text: ", decryptedText)
    else: # if the user selects 3 then we simulate the inside out pattern by reversing the results
        print("Encrypted Text: ", encryptedText[::-1])
        print("Decrypted Text: ", decryptedText[::1])

# runs main function
if __name__ == "__main__":
    main()
