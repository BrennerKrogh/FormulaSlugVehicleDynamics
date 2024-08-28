import math

#Mass
VehicleMass:int = 0
DriverMass:int = 0
ACCMass:int = 0
TotalMass:int = VehicleMass + DriverMass + ACCMass
CenterOfGravity = []



WheelDiameter:int = 16.1 #From onshape
#Drivetrain
MotorV:int
MotorA:int
DrivingGearTeeth:int = 11 #From onshape
DrivenGearTeeth:int = 40 #From onshape
GearingRatio:int = DrivenGearTeeth/DrivenGearTeeth
#reflected mass inertia?? https://www.motioncontroltips.com/how-do-gearmotors-impact-reflected-mass-inertia-from-the-load/


#Suspension
RollCenter=0


#Aerodynamics