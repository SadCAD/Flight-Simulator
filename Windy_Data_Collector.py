"""
This calculator is designed to quickly import wind data from Windy.com to csv for the flight simulator. The process to do this is outlined below:
1. Find the "Input Variables" section of this script and update all values
2. For the list "Windy Values" you will need to open windy.com
3. In windy.com, seach your launch site (see helpful coords below)
4. Zoom in as far as you can on this location
5. Keep track of the dot at the center of your screen (it will disappear in a moment and you need to remember this location)
6. Close the weather bar on the bottom of the screen
7. Click on the location mentioned in step 5
8. Record this data point in the form [altitude agl (m), wind speed (km/h), rough wind angle clockwise from north (deg)]
9. Use the "Alititude" option on the right of your screen to find the wind at the next highest altitude
10. Repeat spet 8 and 9 until you have data to a high enough elevation for your flight
11. Make sure your Windy_Values list is in ascending altitude order. Your final list should look something like this:
Windy_Values = [
    [0, 16, 95],
    [100, 25, 90],
    [600, 24, 92],
    [750, 35, 80],
    [900, 34, 70],
    [1500, 36, 50],
    [2000, 42, 60],
    [3000, 57, 75],
    [4200, 63, 75],
    [5500, 63, 75],
    [7000, 74, 60],
    [9000, 79, 75]
]
12. Run this script
13. [optional] find the output "Air_Data.csv". Make a copy and save it to the file "Historic_Wind_Data".
14. [optional] Rename the copy to include the date, time, and location of observation
15. [optional] To use this historic data, simply open the historic csv, copy all the data, and paste it into "Air_Data.csv"


Helpful coords:
Launch Canada Basic pad: 47.989111, -81.853389
"""
import math
import csv

#Input Variables
Surface_Level_ASL = 381 #height of launch site in m
Windy_Values = [
    [0, 16, 95],
    [100, 25, 90],
    [600, 24, 92],
    [750, 35, 80],
    [900, 34, 70],
    [1500, 36, 50],
    [2000, 42, 60],
    [3000, 57, 75],
    [4200, 63, 75],
    [5500, 63, 75],
    [7000, 74, 60],
    [9000, 79, 75]
] #[altitude agl (m), wind (km/h), wind angle clockwise from north (deg)]

#Auto Setup Variables
Air_Data_Headers = ['Elevation AGL (m)', 'Wind North (m/s)', 'Wind East (m/s)', 'Air Density (kg/m^3)']
Air_Data = [Air_Data_Headers]


for item in Windy_Values:
    Air_Density = 0 #kg/m^3
    Height_ASL = item[0]+Surface_Level_ASL

    #calculating air density based on https://www.grc.nasa.gov/www/k-12/airplane/atmosmet.html
    if(Height_ASL < 11000):
        Air_Density = 101.29*((15.04-0.00649*Height_ASL+273.1)/288.08)**5.256
    elif(Height_ASL < 25000):
        Air_Density = 22.65*math.e**(1.73-0.000157*Height_ASL)
    else:
        Air_Density = 2.488*((-131.21+0.00299*Height_ASL+273.1)/216.6)^-11.388

    Air_Data.append([item[0], item[1]*math.cos(math.radians(item[2]))/3.6, item[1]*math.sin(math.radians(item[2]))/3.6, Air_Density])

with open('Input_Files/Air_Data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(Air_Data)