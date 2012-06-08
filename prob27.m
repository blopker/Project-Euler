b = [-primes(1000),primes(1000)];
count = 0;
countm = 1;
mx = 0;
tic
for i = length(b)/2:length(b)
for a = 1:length(b)
    for n = 0:1000
        p = n^2 + b(a)*n + b(i);
        if isprime(abs(p)) == 0 && count > countm
            countm = count;
            mx = b(a)*b(i);
            count = 0;
            break;
        elseif isprime(abs(p)) == 0 && count < countm
            count = 0;
            break;
        else
            count = count + 1;
        end
    end
end
end
toc
