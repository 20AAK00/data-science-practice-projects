# Calculate the average temperature for each city in a csv file
# The csv file structure is: city, temperature, unit (F for Fahrenheit / C for Celsius)

# Read files
dataFile = open('city-temp.csv', 'r')

# A dict with keys as city names and values as list of two values
# The first value in the list is the count of records related to city
# And the second value of the list is sum of temperatures recorded in that city
data = {}

# Get every line of file and split it on comma
for record in dataFile:
    cityName, temperature, unit = record.rstrip('\n').split(',')
    
    # Convert temperature from str to float
    temperature = float(temperature)

    # If the city has not been stored yet, store it
    if not (data.__contains__(cityName)):
        data[cityName] = [0, 0]

    # If unit is Celsius, change it to Fahrenheit
    if unit == 'C':
        temperature = (temperature * 1.8) + 32

    # Increment the count by 1
    data[cityName][0] += 1
    # Increment the sum
    data[cityName][1] += temperature

print('Average Temperatures:')

# Print each city's average temperature
for city in data:
    print(f'\t{city}: {"{0:.2f}".format(data[city][1] / data[city][0])}')

# Close files
dataFile.close()
