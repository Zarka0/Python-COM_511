def demonstrate_built_in_functions():
    # Example variables of various data types
    num = -10.5
    string = "Hello, World!"
    list_data = [1, 5, 3, 8, 2]
    dictionary = {'a': 1, 'b': 2, 'c': 3}
    boolean = True
    none_value = None

    # Demonstrating the use of abs()
    print("Absolute value of", num, "is:", abs(num))

    # Demonstrating the use of len()
    print("Length of", string, "is:", len(string))
    print("Length of", list_data, "is:", len(list_data))

    # Demonstrating the use of min()
    print("Minimum value in", list_data, "is:", min(list_data))

    # Demonstrating the use of round()
    float_num = 3.14159265359
    print("Rounded value of", float_num, "to 2 decimal places is:", round(float_num, 2))

    # Demonstrating the use of isalnum()
    print("Is 'Hello123' alphanumeric?", 'Hello123'.isalnum())
    print("Is 'Hello@123' alphanumeric?", 'Hello@123'.isalnum())

    # Demonstrating the use of type()
    print("Type of", num, "is:", type(num))
    print("Type of", string, "is:", type(string))
    print("Type of", list_data, "is:", type(list_data))
    print("Type of", dictionary, "is:", type(dictionary))
    print("Type of", boolean, "is:", type(boolean))
    print("Type of", none_value, "is:", type(none_value))


# Calling the function to demonstrate the built-in functions
demonstrate_built_in_functions()