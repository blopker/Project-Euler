w = zeros(0,1);
m = zeros(0,1);
e = zeros(0,1);
for t = 1:10000
    for r = 1:t-1
        if mod(t,r) == 0
            w = [w,r];
        end
    end
    w = sum(w);
    for y = 1:w-1;
        if mod(w,y) == 0
            m = [m,y];
        end
    end
    if sum(m) == t && w ~= t
        e = [e,t]
    end
w = zeros(0,1);
m = zeros(0,1);
end