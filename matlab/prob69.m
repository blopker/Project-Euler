k = 10;
max = 0;
klast = 10;
while k < 1000000
    a = totient(k);
    if max < k/a
        max = k/a
        k
        k = k + klast;
        klast = k;
    else
        k = k + 10;
    end
end