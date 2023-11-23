function x=isPD(A)
[M,N] = size(A);
if M~=N
    error('given matrix is not Symmetric');
end
x1 = 2 ;
x = 1 ;
while x1
    for i=1:M
        subA=A(1:i,1:i); %Extract upper left kxk submatrix
        if (det(subA)<=0) %Check if the determinent of the kxk submatrix is posetive or not
            x=0 ;
            break;
        end
    end
   x1 = 0;
        
end
%     if x
%         display('Given Matrix is Positive definite');
%     else
%         display('Given Matrix is NOT positive definite');
%     end
end