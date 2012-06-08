A = zeros(1,0);
k = 4;
tic
for n = 100000:1000000
    len = length(unique(factor(n)));
    if len == k && n == m + 1
        A = [A,n];
    else
        A = zeros(1,0);
    end
    if length(A) == k
        break;
    end
    m = n;
end
toc