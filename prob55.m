count = 0;
for a = 1:10000
    r = 0;
    e = a;
    while r <=51
        b = str2double(fliplr(num2str(e)));
        c = num2str(e+b);
        if fliplr(c) == c
            r = 55;
            break;
        elseif r == 51
            count = count +1;
        end
        r = r + 1;
        e = e+b;
    end
end