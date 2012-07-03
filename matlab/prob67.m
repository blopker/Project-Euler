tic
A = zeros(100);
n = 1;
w = 1;
for i = 1:100
    for t = 1:n
        A(i,t) = triangle(w);
        w = w+1;
    end
    n = n+1;
end
n = 2;
for i = 2:100
    for t = 1:n
        if t == 1
            A(i,t) = A(i,t) + A(i-1,t);
        else
        A(i,t) = A(i,t) + max(A(i-1,t),A(i-1,t-1));
        end
    end
    n = n+1;
end
toc
max(A(end,:))