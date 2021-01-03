import math
 
# counter clock wise cipher 
 
def encrypt(grid):
    encrypted_text = ""
    grid_width = len(grid[0])
    grid_height = len(grid)
    
    # Here "i" denotes the depth we're into the matrix
    # Here we read the normal matrix in a spiral form starting from top right corner
    for i in range(2):

        # Going down left side
        for j in range(i, grid_height - i - 1):
            encrypted_text += grid[j][i]

        # Going right bottom side
        for j in range(i, grid_width - i - 1):
            encrypted_text += grid[grid_height - i - 1][j]

        # Going up right side
        for j in range(grid_height - i - 1, i, -1):
            encrypted_text += grid[j][grid_width - i -1]

        # Going left top side
        for j in range(grid_width - i - 1, i,-1):
            encrypted_text += grid[i][j]

    return encrypted_text

def decrypt(cipher_text, route_size):
    
    idx = 0
    plain_text = ""
    grid_width = route_size
    grid_height = math.ceil(len(cipher_text) / route_size)
    plain_text_matrix = [[0 for i in range(grid_width)] for j in range(grid_height)]

    for i in range(2):

        for j in range(i, grid_height - i - 1):
            plain_text_matrix[j][i] = cipher_text[idx]
            idx += 1

        for j in range(i, grid_width - i - 1):
            plain_text_matrix[grid_height - i -1][j] = cipher_text[idx]
            idx += 1

        
        for j in range(grid_height - i-1, i, -1):
            plain_text_matrix[j][grid_width - i -1] = cipher_text[idx]
            idx += 1
        
        for j in range(grid_width - i - 1, i, -1):
            plain_text_matrix[i][j] = cipher_text[idx]
            idx += 1
       
    for i in range(grid_height):
        for j in range(grid_width):
            plain_text += str(plain_text_matrix[i][j])

    return plain_text
    


    
