def print_by_five_power_table(height):
    """
    Prints a table with as many rows and columns as variable height dictates,
    with each field being the number on the leftmost column to the power of
    the number column it is in. The function also ensures that each function
    is spaced out by giving each number 3 spaces, and if the number exceeds
    3 digits, whatever space is left in the field it bleeds into will be
    skipped over so it starts out in the same position as the one above it
    should.
    :param height: height and number of columns in the table
    :return: none
    """
    for x in range(1, height + 1):
        for y in range(1, height + 1):
            result_int = x ** y
            separation = 3
            length = len(str(result_int))
            if length % 3 == 0:
                separation = "   "
            elif length % 3 == 1:
                separation = "  "
            elif length % 3 == 2:
                separation = " "
            print(result_int, end=separation)
            if y == height:
                print("")


def main():
    """
    Just some sample behavior. Feel free to try your own!

    :return: none
    """
    test_height = 10
    if test_height == "":
        test_height = 5
    print_by_five_power_table(test_height)

# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
