% c = 1;
% h = num2str(1);
% for q = 2:1000000
%     q = num2str(q);
%     h = [h,q];
% end
% for a = 0:6
%     c = c*str2double(h(10^a))
% end
% 
v = ones(1,9);
for n = 1:6
v = [v,(n+1)*ones(1,9*10^n)];
end
i = 0;
z = 1;
for g = 1:6
while z <= 10^g
    i = i +1;
    z = z+v(i);
    
end
[sum(v(1:i)),i]
    
end
    