import random

def resamplingWheel(p,w,Nnew):
    pnew = []
    N = len(p)
    index = int(random.random()*N)
    beta = 0.0
    mw = max(w)
    for i in range(Nnew):
        beta += random.random()*2.0*mw
        while beta>w[index]:
            beta -= w[index]
            index = (index+1) % N
        pnew.append(p[index])
    return pnew
