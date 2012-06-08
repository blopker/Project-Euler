P = primes(1000000);
b = 4;
tic
for e = 5:length(P)
    p = int2str(P(e));
    if sum(mod(p,2)) == length(p)
    for a = 1:length(p)
        p = [p(2:end),p(1)];
        if isprime(str2double(p)) == 1
            k = k + 1;
        else
            break;
        end
    end
    if k == a
        b = b+1;
    end
    end
    k = 0;
end
toc
b