function [alpha] = Zoom(aj,bj,c1,c2,fu,x)

while 1
    
    alpha = (aj+bj)/2 ;
    
    alpha_phi = double(subs(fu,x,{alpha})); %%evaluating the the phi function at the alpha point
    
    alpha_phi_zero = double(subs(fu,x,{0}));
    
    alpha_phi_a = double(subs(fu,x,{aj}));
    
    alpha_phi_zero_prime =double(subs(gradient(fu),x,{0}));
    
    if alpha_phi > alpha_phi_zero+c1*alpha*alpha_phi_zero_prime  || alpha_phi > alpha_phi_a
        
        bj = alpha ;
        
    else
        
        alpha_phi_prime =double(subs(gradient(fu),x,{alpha}));
        
        if alpha_phi_prime <= -1*c2*alpha_phi_zero_prime
            break
        else
            if alpha_phi_prime*(bj-aj) >= 0
                bj = aj ;
            end
            aj = alpha ;
        end
    end
end

end