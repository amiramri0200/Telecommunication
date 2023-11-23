clc
clear 
close all
%% 
a0 = 0;
b0 = 4;
deghat = 0.00001 ;
x_k = [1 2] ;
iteration = 0;
khata = 1;
%% comuting the value of the given function at the stating point
F1 = @(x1,x2) 100*(x2-x1^2)^2+(1-x1)^2 ;
gra_F1_x1 = @(x1,x2)  2*x1 - 400*x1*(- x1^2 + x2) - 2 ;
gra_F1_x2 = @(x1,x2) - 200*x1^2 + 200*x2;
f = F1(1,2)
%% assigning the function as symbolic so we can calculate the gradient of it
syms alpha x1 x2
Rosenbrocks_Func = 100*(x2-x1^2)^2+(1-x1)^2
gra = gradient(Rosenbrocks_Func)
%% the while loop for calculating the minimum x by the given accuracy t

while norm(khata) > 0.001
    
    x_k1 = x_k
                                               
     Gradient(1,1) = gra_F1_x1(x_k(1),x_k(2));%calculating the gradient of 
     Gradient(2,1) = gra_F1_x2(x_k(1),x_k(2)); %the fucntion at each iteration 
     Gradient
  
     temp1 = x_k - alpha*transpose(Gradient);%note that we are using the transpose of the Gradient
                                             %becouse we are actually using the
                                             %transpose of points
                                       
    temp = subs(Rosenbrocks_Func,[x1 x2],[temp1]);
    
    [alpha_k z]= GSS_amri(a0,b0,deghat,temp,alpha);
    
    x_k = double(x_k-alpha_k*transpose(Gradient))
    
    final_value = F1(x_k(1),x_k(2))
    
    iteration = iteration + 1 ;
    
    khata = x_k1-x_k ;
end
iteration
