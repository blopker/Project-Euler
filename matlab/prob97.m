n = 28433
format long
for i = 1:7830457
    n = n*2;
    while n > 10000000000
        n = n - 10000000000;
    end
end