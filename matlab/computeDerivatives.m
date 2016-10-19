function [fx, fy, ft] = computeDerivatives(im1, im2)

% derivatives as in Barron
% fx= conv2(im1,(1/12)*[-1 8 0 -8 1],'same');
% fy= conv2(im1,(1/12)*[-1 8 0 -8 1]','same');
% ft = conv2(im1, 0.25*ones(2),'same') + conv2(im2, -0.25*ones(2),'same');
% fx=-fx;fy=-fy;

% An alternative way to compute the spatiotemporal derivatives is to use simple finite difference masks.
% fx = conv2(im1,[1 -1]);
% fy = conv2(im1,[1; -1]);
% ft= im2-im1;

if size(im2,1)==0
    im2=zeros(size(im1));
end

Xkern = 0.25* [-1 1; 
               -1 1];
               
Ykern = 0.25*[-1 -1; 
               1 1];
               
Tkern = 0.25*ones(2);

% Horn-Schunck original method
fx = conv2(im1,Xkern,'same') + conv2(im2, Xkern,'same');
fy = conv2(im1, Ykern, 'same') + conv2(im2, Ykern, 'same');
ft = conv2(im1, Tkern,'same') + conv2(im2, -Tkern, 'same');

end