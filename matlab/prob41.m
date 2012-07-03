% n = primes(10000000);
for i = 1:2:100000000
    n = 99254320-i;
    a = num2str(n);
    if isprime(n) == 1 && numel(unique(a))==numel(a)
        for o = 1:numel(a)
            if str2double(a(o)) == 0
                k = 1;
            end
        end
        if k == 1
        else
            n
        end
    end
    k = 0;
end