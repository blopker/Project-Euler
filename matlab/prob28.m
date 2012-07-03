
format long
tic
s = 1;
t = 2;
e = 1;
while t<=1001
    for o = 1:4
        e = e+t;
        s = s + e;
    end
    t = t+2;
end
toc
s;