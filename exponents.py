def details ():
    Description = "Square and Cube of integers."
    Date = "05-16-23"
    print ("\nDescription: {}\nDate: {}".format (Description , Date))
    
details ()

# Open the source file for reading
with open('integers.txt', 'r') as source_file:
    # Create two new files for writing
    with open('double.txt', 'w') as double_file, open('triple.txt', 'w') as triple_file:
        # Iterate over each line in the source file
        