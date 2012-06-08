countm = 0;
tic
for p = 1:1000;
count = 0;
for c = 1:p/2-1
    for b = 1:p/2-1
        if (p-b-c)^2+b^2==c^2
            count = count + 1;
        end
    end
end
if count>countm
    countm = count;
    anse = p;
end
end
toc