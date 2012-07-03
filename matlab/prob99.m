so =0;
for t = 1:numel(a)
    s = b(t)*log(a(t));
    if s > so
        so = s
        t
    end
end