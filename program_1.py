# Program #1: Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers,
# then converts that distance to miles.  The conversion formula is as follows:
# Miles = kilometers x 0.6214.
# The conversion must be done as a function with input and output.

def kilometer_conversion(kilometers):
    # Write a program that converts kilometers temperatures to miles temperatures. 
    # The formula is as follows: F = (9/5)C + 32
    # The program should ask the user to enter a temperature in kilometers, then display the temperature converted to miles.

    # Calculate the miles equivalent.
    miles = 0.0
    miles = kilometers * 0.6214
    # Return the variable to the calling function
    return miles

if __name__ == '__main__':
    kilometers = 0.0
    miles = 0.0
    print('in main')
    # Get the kilometers temperature.
    kilometers = float(input("Enter the distance in kilometers: "))

    # Call kilometer_conversion
    miles = kilometer_conversion(kilometers)
    # Display the miles
    print ("The distance is", miles, "miles.")




