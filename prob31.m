num = 200
count = 0;
for a = 0:200/100
    for b = 0:200/50
        for c = 0:200/20
            for d = 0:200/10
                for e = 0:200/5
                    for f = 0:200/2
                        for g = 0:200
                            if g+2*f+5*e+10*d+20*c+50*b+100*a == 200
                                [a,b,c,d,e,f,g];
                                count = count +1;
                            end
                        end
                    end
                end
            end
        end
    end
end
                            