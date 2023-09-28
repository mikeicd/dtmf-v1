pkg load queueing

P = [0.8 0.2 0.0;
     0.2 0.0 0.8;
     0.7 0.2 0.1]
     
p0 = [0 0 1]

dtmc(P, 3, p0)