def details ():
    Description = "Square and Cube of integers."
    Date = "05-16-23"
    print ("\nDescription: {}\nDate: {}".format (Description , Date))
    
details ()

# Open the source file for reading
with open('integers.txt', 'r') as source_file:
    # Create two new files for writing