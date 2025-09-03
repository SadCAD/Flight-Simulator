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
RasAero_Flight_Data = pandas.read_csv("Input_files/Flight Test.CSV")
RasAero_Aero_Data = pandas.read_csv("Input_files/CD Test.CSV")
Air_Data = pandas.read_csv("Input_files/Air Data.CSV")
Thrust_Data = [(RasAero_Flight_Data['Time (sec)'].values), (RasAero_Flight_Data['Thrust (lb)'].values)*4.44822]
#Flight_Data = [] #a place to store flight data as it is generated
#Headers = ['Time (s)', 'Position North (m)', 'Position East (m)', 'Height AGL (m)', 'Distance From Pad (m)', 'Direction Vector North', 'Direction Vector East', 'Direction Vector Up']

#auto setup variables
Time = ['Time (s)', 0] #(s)
Position = [['Position East [m]', 'Position North [m]', 'Position Verical [m]'], [0, 0, 0]] #East, North, Vertical. relative to launch site (m)
Direction = [['Direction East Component', 'Direction North Component', 'Direction Vertical Component'], [math.sin(math.radians(Rail_Direction))*math.sin(math.radians(Rail_Angle)), math.cos(math.radians(Rail_Direction))*math.sin(math.radians(Rail_Angle)), math.cos(math.radians(Rail_Angle))]]#unit vector showing rocket direction East, North, Up (unitless)
Direction_Rad = [['Direction East [Rad]', 'Direction North [Rad]', 'Direction Vertical [Rad]'], [math.acos(Direction[-1][0]), math.acos(Direction[-1][1]), math.acos(Direction[-1][2])]]#direction given in rad
Ground_Speed_Velocity = [['Ground Speed Velocity East [m/s]', 'Ground Speed Velocity North [m/s]', 'Ground Speed Velocity Verical [m/s]'], [0, 0, 0]] #Ground Speed East, North, Up (m/s)
Air_Speed_Velocity = [['Air Speed Velocity East [m/s]', 'Air Speed Velocity North [m/s]', 'Air Speed Velocity Verical [m/s]'], [Ground_Speed_Velocity[-1][0] + numpy.interp(Position[-1][2], Air_Data['Elevation AGL (m)'], Air_Data['Wind East (m/s)'])], Ground_Speed_Velocity[-1][1] + numpy.interp(Position[-1][2], Air_Data['Elevation AGL (m)'], Air_Data['Wind North (m/s)']), Ground_Speed_Velocity[-1][2]] #Air Speed East, North, Up (m/s) https://www.grc.nasa.gov/www/k-12/airplane/move2.html
Angular_Velocity = [['Angular Velocity East [Rad/s]', 'Angular Velocity North [Rad/s]', 'Angular Velocity Verical [Rad/s]'], [0, 0, 0]] #East, North, Up (Rad/s)
Acceleration = [['Acceleration East [m/s/s]', 'Acceleration North [m/s/s]', 'Acceleration Verical [m/s/s]'], [0, 0, 0]] #East, North, Up (m/s/s) (using change in ground speed/time)
Angular_Acceleration = [['Angular Acceleration East [Rad/s/s]', 'Angular Acceleration North [Rad/s/s]', 'Angular Acceleration Verical [Rad/s/s]'], [0, 0, 0]] #East, North, Up (Rad/s/s)

#Functions
def Thrust_at_Time(t):#time
    return numpy.interp(t, Thrust_Data[0], Thrust_Data[1])#returns thrust in newtons

Flight_Data = [Time, Position]

#while(Position_Height_AGL >= 0){
#    Time = Time+Timestep
#    
#    if(On_Rail){
#        
#    }
#}

with open('Simulated Flight Data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(Flight_Data)