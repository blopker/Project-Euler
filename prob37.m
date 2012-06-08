N = primes(1000000);
r = zeros(0,1);
t = zeros(0,1);
for g = 5:length(N)
for n = 1:6
    U = floor(N(g)/10^(n-1));
    if isprime(U) == 1 || U == 0
        r = [r,1];
    end
end
for n = 1:6
    U = N(g) - floor(N(g)/10^(6-n))*10^(6-n);
    if isprime(U) == 1 || U == 0
        r = [r,1];
    end
end
if sum(r) == 12
    t = [t,N(g)];
end
r = zeros(0,1);
end