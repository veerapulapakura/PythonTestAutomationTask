
file_path_in = '/Users/veerapulapakura/Desktop/car_inputV4.txt'
file_path_out = '/Users/veerapulapakura/Desktop/car_inputV4.txt'
try:
    with open(file_path_in, 'r') as infile, open(file_path_out, 'w') as outfile:
        for line in infile:  # Read each line from the input file
            print(line)
            outfile.write(line)  # Write the line to the output file

except FileNotFoundError:
    print(f"Error: The file at {file_path_in} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Ensure the browser is closed
    #context.driver.quit()
    print("kk")
