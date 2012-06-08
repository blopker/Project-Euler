summx = 0;
for a = 1:99
    summ = 0;
    for b = 1:99
        s = num2str(a^b);
        for e = 1:numel(s)
            summ = summ+str2double(s(e));
        end
        if summ >summx
            summx=summ;
            [a,b]
        end
    end
end