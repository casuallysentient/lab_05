def get_formatted_address_string(address, city, country, name, postal_code):
    """
    Receives the relevant information from main(), formats the string, and returns it.

    :param address: the contact's street address
    :param city: the city the contact lives in
    :param country: the country the contact lives in
    :param name: the contact's name
    :param postal_code: the contact's zip code
    :return: formatted version of the string with all the above information
    """
    if name == "":
        name = "Undisclosed Recipient"
    formatted_string = name + "\n" + address + "\n" + city + ", " + country
    if postal_code != 0:
        formatted_string = formatted_string + "\n" + str(postal_code)
    return formatted_string


def main():
    """
    Passes the relevant information into get_formatted_address_string and then prints the returned formatted string.

    :return: none
    """
    test_name = "Reilly Ford"
    test_address = "101 Johnson St"
    test_city = "Brooklyn, NY"
    test_country = "United States"
    test_postal_code = 11201

    address_string = get_formatted_address_string(address=test_address, city=test_city, country=test_country,
                                                  name=test_name, postal_code=test_postal_code)
    print(address_string)


# DO NOT WRITE CODE BELOW THIS LINE

if __name__ == '__main__':
    main()
