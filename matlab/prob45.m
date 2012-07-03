format long
num = 100000;
n = 1:num;
N = (n.^2+n)/2;
M = (3*n.^2-n)/2;
J = 2*n.^2-n;
tic
    for t = 1:num
        if mod((1+sqrt(1+24*M(t)))/6,1) == 0
            M(t)
        end
    end
