function [ y ] = ispent( x )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
if mod((sqrt(24*x+1)+1)/6,1)==0
    y = 1;
else
    y=0;
end

end

