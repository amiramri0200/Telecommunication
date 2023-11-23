function [alpha_star] = Linesearch(alpha_max,c1,c2,fu,x)
i =2 ;
alpha(1) = 0;
alpha(2) = alpha_max/2 ;
while 1
    
    alpha_ph_i = double(subs(fu,x,{alpha(i)}));
    
    alpha_phi0 = double(subs(fu,x,{0}));
    
    alpha_phi_prime0 = double(subs(gradient(fu),x,{0}));
    
    alpha_phi_ii = double(subs(fu,x,{alpha(i-1)})) ;
    
    if (alpha_ph_i > (alpha_phi0+alpha(i)*c1*alpha_phi_prime0)) || ((alpha_ph_i>=alpha_phi_ii) && (i>2) )
        alpha_star =Zoom(alpha(i-1),alpha(i),c1,c2,fu,x)  ;
        break
    else
        alpha_phi_prime_i = double(subs(gradient(fu),x,{alpha(i)}));
        if abs(alpha_phi_prime_i) <= -1*c2*alpha_phi_prime0
            alpha_star = alpha(i)
            break
        end
        if alpha_phi_prime_i >= 0
            alpha_star = Zoom(alpha(i),alpha(i-1),c1,c2,fu,x) ;
            break
        else
            i = i + 1;
            alpha(i) = (alpha(i-1) + alpha_max)/2;
        end
    end
end
end