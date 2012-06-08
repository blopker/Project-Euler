function [ m ] = blanc( x )
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here
format long
set(0,'RecursionLimit',400)
assignin('caller','var',x)
if x >=1
    m = 1/2+blanc(x-1)
elseif x >1/2 && x <1
    m = 1/2 - blanc(1-x)
    
elseif x>0 && x <=1/2
    m = blanc(2*x)/4+x^2/2
    
else
    m = -blanc(-x)
    
end

end

