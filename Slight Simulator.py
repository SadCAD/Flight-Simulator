#Importing
import csv
import pandas
import os
import math
import numpy
import xarray

#manual setup variables
Timestep = 0.01 #time step of solver in seconds
Rail_Angle = 6 #rail angle from verticle in degrees from 0 to 90
Rail_Direction = 0 #rail direction on compass in degrees from 0 to 359
Rail_Length = 0 #effective rail length (m)

#Logic switches
On_Rail = True

#data handling
RasAero_Flight_Data = pandas.read_csv("Input_files/Flight Test.csv")
RasAero_Aero_Data = pandas.read_csv("Input_files/CD Test.csv")
Air_Data = pandas.read_csv("Input_files/Air_Data.csv")
Thrust_Data = [(RasAero_Flight_Data['Time (sec)'].values), (RasAero_Flight_Data['Thrust (lb)'].values)*4.44822]
Flight_Data = [] #a place to store flight data as it is generated
#Headers = ['Time (s)', 'Position North (m)', 'Position East (m)', 'Height AGL (m)', 'Distance From Pad (m)', 'Direction Vector North', 'Direction Vector East', 'Direction Vector Up']

#auto setup variables
Time = 0 #(s)
Position = [0, 0, 0] #East, North, Up (m)
Direction = [math.sin(math.radians(Rail_Direction))*math.sin(math.radians(Rail_Angle)), math.cos(math.radians(Rail_Direction))*math.sin(math.radians(Rail_Angle)), math.cos(math.radians(Rail_Angle))]#unit vector showing rocket direction East, North, Up (unitless)
Angle = [math.acos(Direction[0]), math.acos(Direction[1]), math.acos(Direction[2])]
Velocity = [0, 0, 0] #East, North, Up (m/s)
Angular_Velocity = [0, 0, 0]
Acceleration = [0, 0, 0] #East, North, Up (m/s/s)
Angular_Acceleration = [0, 0, 0]
 
Flight_Data = []

#Functions
def Thrust_at_Time(t):
    return numpy.interp(t, Thrust_Data[0], Thrust_Data[1])


while(Position_Height_AGL >= 0){
    Time = Time+Timestep
    
    if(On_Rail){
        
    }
}

with open('Simulated Flight Data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(Flight_Data)