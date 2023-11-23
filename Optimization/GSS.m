function [x_star y_star] = GSS_amri(a0,b0,error,fu,x)
length_new = 0;
length = b0-a0;
p = 0.381966;
n = ceil((log(error)-log(length))/log(1-p));
temp = length * p;
a1 = a0 + temp ;
b1 = b0 - temp ;
y_a1 = double(subs(fu,x,{a1})) ;
y_b1 = double(subs(fu,x,{b1})) ;

 if (y_a1) < (y_b1)
        b0 = b1 ;
        b1 = a1 ;
        y_b1 = y_a1 ;
        length_new = b0 - a0 ;
        a1 = a0 + length_new * p ;
        y_a1 =double(subs(fu,x,a1)) ;
 else
        a0 = a1 ;
        a1 = b1 ;
        y_a1 = y_b1 ;
        length_new = b0 - a0 ;
        b1 = b0 - length_new * p ;
        y_b1 = double(subs(fu,x,b1)) ;
 end
    
 
for i=2:n
 if y_a1 < y_b1;
        b0 = b1 ;
        b1 = a1 ;
        y_b1 = y_a1 ;
        length_new = b0 - a0 ;
        a1 = a0 + length_new * p ;
        y_a1 = double(subs(fu,x,a1)) ;
 else
        a0 = a1 ;
        a1 = b1 ;
        y_a1 = y_b1 ;
        length_new = b0 - a0 ;
        b1 = b0 - length_new * p ;
        y_b1 = double(subs(fu,x,b1)) ;
 end
end
  if y_a1 < y_b1
      y_star = y_a1;
      x_star = a1;
  else
      y_star = y_b1;
      x_star = b1;

  end
end