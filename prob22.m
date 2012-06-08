al = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
score = 0;
namscore = 0;
for t = 1:5163
    nam = Book2{t};
    for e = 1:length(nam)
        for q = 1:length(al)
            if nam(e) == al(q)
                namscore = namscore + q;
                break;
            end
        end
    end
    score = score + namscore*t
    namscore = 0;
end
