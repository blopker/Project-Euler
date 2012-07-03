a = zeros(0,1);
b = zeros(0,1);
for d = 1:40
    a = [a,sum(sum(graphminspantree(sparse(tril(network)))))];
%     b = [b,sum(graphmaxflow(sparse(network),d,d))];
end
min(a)