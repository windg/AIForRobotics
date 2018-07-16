from math import *
from numpy import *

def evalGaus(mu, sigma2, x):
    return 1/sqrt(2.*pi*sigma2)*exp(-.5*(x-mu)**2/sigma2)


def multiplyScalar(mean1, var1, mean2, var2):
    new_mean = (var2*mean1+var1*mean2)/(var1+var2)
    new_var = 1/(1/var1 + 1/var2)
    return [new_mean, new_var]


def addScalar(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]


def multiplyVector(mean1, var1, mean2, var2):
    # Update (measurement)
    sumInv = (var1 + var2).I
    new_var = var1*sumInv*var2
    new_mean =var2*sumInv*mean1 + var1*sumInv*mean2
    return [new_mean, new_var]


def addVector(mean1, var1, mean2, var2):
    # Predict (motion)
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

def kalman_filter(x, P):
    for n in range(len(measurements)):
        # measurement
        Z = matrix([[measurements[n]]])
        y = Z.transpose() - H*x
        S = H*P*H.transpose() + R 
        K = P*H.transpose()*S.I
        x = x + K*y
        P = (I-K*H)*P
        # predict
        x = F*x + u
        P = F*P*F.transpose()
    return [x, P]



measurements = [1, 2, 3]

x = matrix([[0.], [0.]]) # initial state (location and velocity)
P = matrix([[1000., 0.], [0., 1000.]]) # initial uncertainty
u = matrix([[0.], [0.]]) # external motion
F = matrix([[1., 1.], [0, 1.]]) # next state function
H = matrix([[1., 0.]]) # measurement function, C
R = matrix([[1.]]) # measurement uncertainty
I = matrix([[1., 0.], [0., 1.]]) # identity matrix

print(kalman_filter(x,P))
