import numpy as np 
from boid import Boid

# Study area bounds (Soquel Canyon MPA in EPSG32610)
minX = 585076 
minY = 4073066 
maxX = 594870 
maxY = 4078604

# Figure out the size of our study area 
xRange = maxX - minX 
yRange = maxY - minY 

# How many boids do we want? 
nB = 100 

# Let's generate the school! 
school = [Boid(np.random.random() * 10 + minX + xRange/2, np.random.random() * 10 + minY + yRange/2, minX, minY, maxX, maxY) for _ in range(nB)]

# Create a file. Will give an error if it exists already 
f = open("positions.csv","xt") 
# Write our CSV header 
f.write("time,boid,x,y,direction\n")

# How many time steps do we want? 
timeSteps = 1000 
# Let's loop! 
for tS in range(timeSteps):
    for boid in school: 
        # Do the behaviours and update positions 
        boid.behave(school) 
        boid.update() 
        # Calculate the direction (optional but gives nice animations) 
        direction = np.arctan2(boid.velocity[0], boid.velocity[1]) * 57.29578 
        # Output our time stamp, id, position, and direction to the file 
        f.write(str(tS)) # Time Stamp 
        f.write(",") 
        f.write(str(boid.boidID)) # Unique boid ID 
        f.write(",") 
        f.write(str(boid.position[0])) # X 
        f.write(",") 
        f.write(str(boid.position[1])) # Y 
        f.write(",") 
        f.write(str(direction)) # Direction (see note) 
        f.write("\n") # Newline
