o = 12000;
k = 0;
for d = 1:o
    for n = 1:d
        if isprime(d)==1 || isprime(n)==1
        if n/d <1/2 && n/d > 1/3
            k = k +1;
        end
        end
    end
end