def toFixed(value, digits):
    """Format a float to a fixed number of decimal places as a string."""
    return "%.*f" % (digits, value)

# PROGRAMMER:   Marlena Fabrick
# PROGRAM NAME: Calculate Daily Rain Average (For Loop + File Output)
# DATE WRITTEN: 2020
#
# PURPOSE: Use a FOR loop to collect a user-specified number of daily
#          rainfall amounts, write all results to an external text file,
#          and display the average rainfall.
#
# VARIABLES (alphabetical):
#   count        - for loop control variable (lcv)
#   dayDate      - stores the name of the day and date of rainfall
#   fileName     - name of the output file entered by the user
#   howMany      - the number of rainfall amounts to be entered
#   outFile      - the file object used for writing output
#   rainfall     - stores a single rainfall amount in inches
#   rainfallAvg  - stores the calculated average rainfall
#   sumRainfall  - running total of all rainfall amounts

# Initialize processed variables
rainfallAvg = 0.0
sumRainfall = 0.0

# Creating an external file to store output
# Define the output file name where the output will be written
fileName = input("Enter the file name where output will be written "
                 "(end with .txt) --> \n").strip()
outFile = open(fileName, "w")

# Write column headings to output file
outFile.write("================================================================\n")
outFile.write("NAME OF DAY & DATE             RAINFALL [INCHES]\n")
outFile.write("================================================================\n")

# Input: number of rainfall entries with validation
print("How many rainfall amounts do you wish to enter?")
while True:
    try:
        howMany = int(input())
        if howMany <= 0:
            print("Please enter a positive whole number greater than zero.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# FOR LOOP to collect each rainfall entry
for count in range(1, howMany + 1):

    # Input: day and date of the rainfall
    print("Enter the Name of the Day and Date of the Rain Fall [e.g. Monday 2-12-20]")
    dayDate = input().strip()

    # Input: actual rainfall amount with validation
    while True:
        print("What is the rainfall amount in inches on " + dayDate +
              "? [enter as a positive value, decimals allowed e.g. 2.58]")
        try:
            rainfall = float(input())
            if rainfall < 0:
                print("Please enter a non-negative value.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Keep a running sum of all rainfalls
    sumRainfall = sumRainfall + rainfall

    # Write the day/date and rainfall to the output file
    outFile.write(format(dayDate, "25s") + " " * 8 + format(rainfall, "10,.2f") + "\n")
    # end for loop

# Calculate and write average rainfall
outFile.write("================================================================\n")
rainfallAvg = sumRainfall / howMany
outFile.write("THE AVERAGE RAINFALL AMOUNT = " + format(rainfallAvg, ",.2f") + " INCHES\n")
outFile.write("================================================================\n")

# Close the external output file
outFile.close()
print("Results written to: " + fileName)

# END PROGRAM
