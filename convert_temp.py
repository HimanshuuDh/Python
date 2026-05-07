def to_celsius(f):
    """
    A utility function that takes fahrenheit temperature as parameter
    and returns the equivalent celsius value
    """
    c = (f - 32) * 5 / 9
    return c


def main():
    temp_file = open('temperatures.txt', 'r')

    # read the first line to make sure file is not completely empty
    line = temp_file.readline()


    while line != '':
        # convert line text from string to float
        fahren = float(line)

        # call the function to do conversion and display result
        celsius = to_celsius(fahren)
        print(celsius)

        # read the next line
        line = temp_file.readline()

    temp_file.close()


main()