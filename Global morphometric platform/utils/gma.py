import math
import csv
def appendcsv(filename,list):
    with open(filename,"a", newline="") as f:
        csv.writer(f).writerows(list)
        f.flush()
        
def loadcsv(filename):
    with open(filename, newline='') as f: 
        return list(csv.reader(f))

def check_elevation(coord):
    ave = (coord[0] + coord[1])/2
    print(ave, coord[2])
    if ave >= coord[2] : res = 1
    else: res = -1
    return res

def calculate_distance(coord1,coord2):
    return math.sqrt((coord2[0]-coord1[0]) ** 2 + (coord2[1]-coord1[1]) ** 2 + (coord2[2]-coord1[2]) ** 2)
def calculate_midpoint(coord1,coord2):
    return((coord1[0]+coord2[0])/2 , (coord1[1]+coord2[1])/2 , (coord1[2]+coord2[2])/2)
def main():
    coordinates=[]
    coordinates1 = []
    headrow =['id']+ ['Length']+['Width_25']+ ['Width_50']+['Width_75']+ ['Elevation_25']+  ['Elevation_50']+ ['Elevation_75'] 
  #  appendcsv('results_som.csv',[headrow])
    data=loadcsv('Y27Rec30min_3_19som.csv')
    for i in range(1,len(data)):
        x = float(data[i][0])
        y = float(data[i][1])
        z1 = float(data[i][2])
        z2 = float(data[i][3])
        z = z1 * z2
        coordinates.append([x, y, z])
        if i <3:
            a = float(data[i][4])
            b = float(data[i][5])
            c = float(data[i][6])
            coordinates1.append([a,b,c])

  #  for i in range(1,18):
        
 #       x=float(input(f"Enter x coordinate {i} :"))
 #       y=float(input(f"Enter y coordinate {i} :"))
 #       z=float(input(f"Enter z coordinate {i} :"))
 #       coordinates.append([x, y, z])
        
        
    length=calculate_distance(coordinates[0],coordinates[1])
    print("length of the neuropore:",length)
    width_25=calculate_distance(coordinates[2],coordinates[3])
    print("width at 25%:",width_25)
    width_50=calculate_distance(coordinates[4],coordinates[5])
    print("width at 50%:", width_50)
    width_75=calculate_distance(coordinates[6],coordinates[7])
    print("width at 75%:", width_75)
    midpoint_25=calculate_midpoint(coordinates[8],coordinates[9])
    elevation_25=calculate_distance(midpoint_25,coordinates[10])
    print("elevation at 25%:", elevation_25)
    midpoint_50=calculate_midpoint(coordinates[11],coordinates[12])
    elevation_50=calculate_distance(midpoint_50,coordinates[13])
    print("elevation at 50%:", elevation_50)
    midpoint_75=calculate_midpoint(coordinates[14],coordinates[15])
    elevation_75=calculate_distance(midpoint_75,coordinates[16])
    print("elevation at 75%:", elevation_75)
    elevation_status_50 = check_elevation(coordinates1[0])
    elevation_status_75 = check_elevation(coordinates1[1])
    elevation_50 =  elevation_status_50 * elevation_50
    elevation_75 =  elevation_status_75 * elevation_75
    
    row = ['']+[length]+ [width_25]+[width_50]+[width_75]+[elevation_25]+  [elevation_50] + [elevation_75] 
    
    appendcsv('results_som_main.csv',[row])

