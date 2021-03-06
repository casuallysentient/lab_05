def is_password_valid(test_password):
    """
    Accepts a password and tests to make sure that it meets all the
    qualifications to be a valid password.

    :param test_password: the password to be tested for its validity
    :return: boolean for whether or not the password is valid
    """
    length = len(test_password)
    if length >= 8:
        num_lower = 0
        num_upper = 0
        num_numbers = 0
        num_chars = 0
        for x in range(length):
            if test_password[x].islower():
                num_lower += 1
            elif test_password[x].isupper():
                num_upper += 1
            elif test_password[x].isnumeric():
                num_numbers += 1
            elif test_password[x] == "!" or test_password[x] == "@" or test_password[x] == "!" or test_password[x] == "#" or test_password[x] == "$":
                num_chars += 1
        if num_lower >= 2 and num_upper >= 2 and num_numbers >= 1 and num_chars >= 1:
            return True
    return False


def main():
    """
    Passes the password to be tested into is_password_valid,
    receives a boolean value back, and prints the appropriate
    message to inform the user of their password's validity.

    :return: none
    """
    test_password = "NAit1ppp!"

    if is_password_valid(test_password):
        print("This is a valid password!")
    else:
        print("This is not a valid password!")

# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
