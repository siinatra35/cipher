import math

import path_one
import path_two
import path_three
grid = []

"""
route size 3 can handle 5,6, and 10 with errors happening at 7, 8, 9
route size 4 can handle 10 - 20 , errors start at 21 and up
route size 5 can handle 16 - 21
"""


def main():

    
    plain_text = input("text that will be encrypted: ")
    step_size = int(input("Route size: "))
    characters = len(plain_text)
    print('Word length:', characters)

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
    print("path three")
    path_three.encrypt(grid)


if __name__ == "__main__":
    main()
