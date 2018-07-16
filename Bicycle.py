# -----------------
# USER INSTRUCTIONS
#
# Write a function in the class robot called move()
#
# that takes self and a motion vector (this
# motion vector contains a steering* angle and a
# distance) as input and returns an instance of the class
# robot with the appropriate x, y, and orientation
# for the given motion.
#
# *steering is defined in the video
# which accompanies this problem.
#
# For now, please do NOT add noise to your move function.
#
# Please do not modify anything except where indicated
# below.
#
# There are test cases which you are free to use at the
# bottom. If you uncomment them for testing, make sure you
# re-comment them before you submit.

from math import *
import random
# --------
# 
# the "world" has 4 landmarks.
# the robot's initial coordinates are somewhere in the square
# represented by the landmarks.
#
# NOTE: Landmark coordinates are given in (y, x) form and NOT
# in the traditional (x, y) format!

landmarks  = [[0.0, 100.0], [0.0, 0.0], [100.0, 0.0], [100.0, 100.0]] # position of 4 landmarks
world_size = 100.0 # world is NOT cyclic. Robot is allowed to travel "out of bounds"
max_steering_angle = pi/4 # You don't need to use this value, but it is good to keep in mind the limitations of a real car.

# ------------------------------------------------
# 
# this is the robot class
#

class robot:

    # --------

    # init: 
    #	creates robot and initializes location/orientation 
    #

    def __init__(self, length = 10.0):
        self.x = random.random() * world_size # initial x position
        self.y = random.random() * world_size # initial y position
        self.orientation = random.random() * 2.0 * pi # initial orientation
        self.length = length # length of robot
        self.bearing_noise  = 0.0 # initialize bearing noise to zero
        self.steering_noise = 0.0 # initialize steering noise to zero
        self.distance_noise = 0.0 # initialize distance noise to zero
    
    def __repr__(self):
        return '[x=%.6s y=%.6s orient=%.6s]' % (str(self.x), str(self.y), str(self.orientation))
    # --------
    # set: 
    #	sets a robot coordinate
    #

    def set(self, new_x, new_y, new_orientation):

        if new_orientation < 0 or new_orientation >= 2 * pi:
            raise(ValueError, 'Orientation must be in [0..2pi]')
        self.x = float(new_x)
        self.y = float(new_y)
        self.orientation = float(new_orientation)


    # --------
    # set_noise: 
    #	sets the noise parameters
    #

    def set_noise(self, new_b_noise, new_s_noise, new_d_noise):
        # makes it possible to change the noise parameters
        # this is often useful in particle filters
        self.bearing_noise  = float(new_b_noise)
        self.steering_noise = float(new_s_noise)
        self.distance_noise = float(new_d_noise)
    
    ############# ONLY ADD/MODIFY CODE BELOW HERE ###################
    def sense(self,add_noise = 1):
        Z = []
        for i in range(len(landmarks)):
            bearing = atan2(landmarks[i][1]-self.y,landmarks[i][0]-self.x) - self.orientation
            if add_noise:
                bearing += random.gauss(0,self.bearing_noise)
            bearing %= 2.0*pi
            Z.append(bearing)
        return Z
    # --------
    # move:
    #   move along a section of a circular path according to motion
    #
    
    def move(self, motion,tolerance = 0.001): # Do not change the name of this function

        # ADD CODE HERE
        alpha = motion[0]
        d = motion[1]
        if d < 0.0:
            raise(ValueError,'Moving backwards is not valid')
        alpha = random.gauss(alpha, self.steering_noise)
        d = random.gauss(d, self.distance_noise)
        beta = d/self.length*tan(alpha)
        if abs(beta) > tolerance:
            R = d/beta
            Cx = self.x-sin(self.orientation)*R
            Cy = self.y+cos(self.orientation)*R
            self.x = Cx+sin(self.orientation+beta)*R
            self.y = Cy-cos(self.orientation+beta)*R
            self.orientation +=beta 
            self.orientation %= 2*pi
        else:
            self.x += d*cos(self.orientation)
            self.y += d*sin(self.orientation)
            self.orientation += beta
            self.orientation %= 2*pi
        res = robot(self.length)
        res.set(self.x, self.y, self.orientation)
        res.set_noise(self.bearing_noise, self.steering_noise, self.distance_noise)
        
        return res
       
    ############## ONLY ADD/MODIFY CODE ABOVE HERE ####################


