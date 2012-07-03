divisors = zeros(0,1);
abund = zeros(0,1);
summ = zeros(0,1);
for i = 1:20161
    for o = 1:i/2
        if mod(i,o) == 0
            divisors = [divisors,o];
        end
    end
    if sum(divisors) > i
        abund = [abund,i];
    end
    divisors = zeros(0,1);
end
k = 0;
for r = 1:20161
    for a = 1:length(abund)
        for b = a:length(abund)
            if r == abund(a) + abund(b)
                k = 1;
                break;
            end
        end
    if k ==1;
        break;
    end
    end
    if k == 0;
        summ = [summ,r];
    end
    k = 0;
end
Asnwer = sum(summ)