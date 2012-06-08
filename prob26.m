max = 0;
for n = 1:1000
    i = n;
    while mod(i,2) == 0
        i = i/2;
    end
    while mod(i,5) == 0
        i = i/5;
    end
    if mod(10^i-1,i) == 0;
        i;
        if i > max
            max = n
        end
        break;
    end
end
        