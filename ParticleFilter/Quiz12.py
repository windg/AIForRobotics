from Class3 import robot
from ResamplingWheel import resamplingWheel

def eval(r, p):
    sum = 0.0;
    for i in range(len(p)): # calculate mean error
        dx = (p[i].x - r.x + (world_size/2.0)) % world_size - (world_size/2.0)
        dy = (p[i].y - r.y + (world_size/2.0)) % world_size - (world_size/2.0)
        err = sqrt(dx * dx + dy * dy)
        sum += err
    return sum / float(len(p))

myrobot = robot()
myrobot = myrobot.move(0.1, 5.0)
Z = myrobot.sense()
N = 1000
p = []
T = 10
for i in range(N):
    r = robot()
    r.set_noise(0.05, 0.05, 5.0)
    p.append(r)

print(eval(myrobot,p))
for n in range(T):
   
    myrobot = myrobot.move(0.1, 5.0)
    Z = myrobot.sense()
    w = []
    for i in range(N):
        p[i] = p[i].move(0.1, 5.0)
        w.append(p[i].measurement_prob(Z))
    
    p = resamplingWheel(p=p, w=w, Nnew=1000)
    print(eval(myrobot,p))

