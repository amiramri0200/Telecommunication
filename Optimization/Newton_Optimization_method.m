clc
clear 
close all
%%
a0 = 0;
b0 = 10;
x_start = [1 2 2 2] ; 
xk = [1 2 2 2] ;
error = 1;
iteration = 0;
%%
syms x1 x2 x3 x4 alpha
powell_function = (x1+10*x2)^2+5*(x3-x4)^2+(x2-2*x3)^4+10*(x1-x4)^4 ;
powell_gradient = gradient(powell_function) ;
powell_hessi = hessian(powell_function) ;
powell_hessian_inverse = inv(powell_hessi) ;
 %%
while norm(error) > .001
    Hk = double(subs(powell_hessi,{x1 x2 x3 x4},{xk}))%calculating the 
                                                      %hessian of powell function
    if ~isPD(Hk)
        miu_k =abs(min(eig(Hk))) + 0.01;
        I = eye(4);  %  unit matrix
        Hk = Hk + miu_k * I ;
    end
    Hk_inv =inv(Hk);%calculating the inverse of the hessian matrix
    
    gk = double(subs(powell_gradient,[x1 x2 x3 x4],xk)) ;
    
    temp1 = xk - alpha * transpose(Hk_inv * gk) ;%note that type of alpha
                                                 % is syms
    
    temp = subs(powell_function,[x1 x2 x3 x4],temp1);
    
    [alpha_k z] = GSS_amri(a0,b0,.00001,temp,alpha);
    
    xk_new =xk - alpha_k * transpose(Hk_inv * gk) ;
    
    final_value = double(subs(powell_function,{x1 x2 x3 x4},{xk_new}))
    
    error = xk - xk_new ;
    
    xk = xk_new
    
    iteration = iteration + 1;
end
iteration