import math

import path_one
import path_two
grid = []


def main():

    plain_text = input("text that will be encrypted: ")
    step_size = int(input("Route size: "))
    characters = len(plain_text)
    print('Word length:' ,characters)

    for number_of_rows in range(math.ceil(len(plain_text) / step_size)):
        rows = []
        for j in range(step_size):
            if number_of_rows * step_size + j < len(plain_text):
                rows.append(plain_text[number_of_rows * step_size + j])
            else:
                rows.append('-')
        grid.append(rows)

    # grid representation 
    print('-------------------')
    for i in grid:
        print(i)

    print('-------------')
    print('path one')
    cipher_text = path_one.encrypt(grid)
    print(cipher_text)
    decrypted_text = path_one.decrypt(cipher_text, step_size)
    print(decrypted_text)
    print('-------------')
    
    print('path two')
    test = path_two.encrypt(grid)
    print(test)
    d = path_two.decrypt(test, step_size)
    print(d)
    print('-------------')
    



if __name__ == "__main__":
    main()
