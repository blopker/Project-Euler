E = zeros(1,0);
for t = 1901:2000
    for y = 1:12
        E = [E,eomday(t,y)];
    end
end
E = E(9:end);
r = 0;
count = 1;
for i = 1:length(E)
    r = r+E(i);
    if mod(r,7)==0
        count = count + 1;
    end
end
