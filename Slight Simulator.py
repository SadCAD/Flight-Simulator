#Importing
import csv
from pandas import *
import os
import math

#manual setup variables
Timestep = 0.01 #time step of solver in seconds
Rail_Angle = 6 #rail angle from verticle in degrees from 0 to 90
Rail_Direction = 0 #rail direction on compass in degrees from 0 to 359

#automatic setup variables
RasAero_Flight_Data = read_csv("Input_files/Flight Test.csv")
RasAero_Aero_Data = read_csv("Input_files/CD Test.csv")
Time = 0
Position_North = 0
Position_East = 0
Position_Height_AGL = 0
Direction_North = math.cos(math.radians(Rail_Direction))*math.sin(math.radians(Rail_Angle))
Direction_East = math.sin(math.radians(Rail_Direction))*math.sin(math.radians(Rail_Angle))
Direction_Up = math.cos(math.radians(Rail_Angle))
Previous_Interval = [Time,Position_North,Position_East,Position_Height_AGL,Direction_North,Direction_East,Direction_Up]
#Thrust_Data = [[RasAero_Flight_Data['Time (sec)'].tolist()], [4.44822*x for x in RasAero_Flight_Data['Thrust (lb)'].tolist()]]



#output as csv file
with open('Simulated Flight Data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Time (s)', 'Position North (m)', 'Position East (m)', 'Height AGL (m)', 'Direction Vector North', 'Direction Vector East', 'Direction Vector Up']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)