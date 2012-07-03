function [ a ] = totient( n )
%Computes Euler's Totient function
%From: http://en.wikipedia.org/wiki/Euler's_totient_function

if mod(log(n)/log(2),1) == 0
    a = n/2;
else
k = 1:n;
a = real(sum(gcd(k,n).*exp(-2*pi*1i*k/n)));
end

end

