from binary_tree import BinaryTree


def main():
    numbers = BinaryTree(5)

    numbers.insert_left(2, 1)
    numbers.insert_left(4, 2)
    numbers.insert_right(5, 2)

    numbers.insert_right(3, 1)
    numbers.insert_left(6, 3)
    numbers.insert_left(8, 6)
    numbers.insert_right(9, 6)
    numbers.insert_right(7, 3)

    print(numbers.depth(4))

    print('----------------------------------')
    print('----------------------------------')


main()
