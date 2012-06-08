al = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
n = 1:1000;
T = .5*n.*(n+1);
score = 0;
namscore = 0;
tic
for t = 1:1786
    nam = words{t};
    for e = 1:length(nam)
        for q = 1:length(al)
            if nam(e) == al(q)
                namscore = namscore + q;
                break;
            end
        end
    end
    for a = 1:length(T)
        if namscore == T(a)
            score = score +1;
        end
    end
    namscore = 0;
end
toc
