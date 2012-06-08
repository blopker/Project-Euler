format long
% a =7;
% w = zeros(0,1);
% n = (1:2:80);
%     b = n.*(n-1);
%     w = mod(b,a^2)
% maxx = 0;
% summ = 0;
% for a = 3:1000
%     for n = 1:a/2
%         b = (a-1).^n+(a+1).^n;
%         c = mod(b,a^2);
%     if maxx < c && c < a^2
%         maxx = c;
%     end
%     end
%     summ = [summ,maxx];
% end


% maxx = 0;
% a = 10;
% n = 1:2:11;
% b = (a-1).^n+(a+1).^n
% maxx = [maxx,max(mod(b,a^2))]

sum((3:1000).*(floor((3:1000)/2))*2)
summ = 0;
for a = 3:1000
    n = 2;
    while 2*n < a
        n = n+1;
    end
    n = n-1;
    summ = summ + 2*a*n;
end

