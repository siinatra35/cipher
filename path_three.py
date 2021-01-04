
import math
E = ""
D = ""


def storage(num_rows):
    # arr = []
    # pos = 0
    # while pos < num_rows:
    #     arr[pos] = []
    #     pos += 1
    arr = [0 for i in range(num_rows)]

    return arr

# def fill_Table_Encrypt(letters, ROWS, COLS):
#     pos = 0
#     amount = storage(ROWS)
#     pathType = "clockwise"
#     # pathParams(pathType, ROWS, COLs)
#     r = 0 
#     c = 0
#     for i in range(ROWS):
#         for j in range(COLS):
#             character = "X"
#             if pos < len(letters):
#                 character = letters[pos]
#                 amount[i].append(character)

#     return amount


def pathParams(path, rowNumber, colNumber):
    g_posR = 0
    g_posC = colNumber - 1
    g_borderL = 0
    g_borderT = 0
    g_borderR = colNumber - 1
    g_borderB = rowNumber - 1

    if path == "clockwise":
        g_dirR = 1
        g_dirC = 0
    else:
        g_dirR = 0
        g_dirC = -1


def main():
    E = "DAVIDMARTNACUNA"
    route_size = 3
    totalCols = route_size
    totalRows = len(E) / totalCols
    print(len(E))
    
    if totalRows != math.ceil(totalRows):
        totalRows = math.floor(totalRows) + 1
    #s = storage(totalRows)
    #print(s)

  #  fill_Table_Encrypt(E , totalRows, totalCols)



if __name__ == "__main__":
    main()
    



