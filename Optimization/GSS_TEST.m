clc
clear 
close all
syms x 
f = x^4-14*x^3+60*x^2-70*x;

%double(subs(f,x,1))
[x_star y_star] = GSS_amri(0,2,0.3,f,x);