n = 3000;
i = (1:n); 
P = i.*(3*i-1)/2;
k = 0;
D = zeros(0,1);
for t = 1:n
    for r = t:n
        if ispent(P(t)+P(r)) == 1 && ispent(abs(P(r)-P(t))) == 1
            D = [D,abs(P(t) - P(r))]
        end
    end
end
min(D)