function RunHornSchunck()
name = 'sphere';

fn1 = ['../data/',name,'/',name,'.0.bmp'];
fn2 = ['../data/',name,'/',name,'.1.bmp'];


im1 = imread(fn1);
im2 = imread(fn2);

figure(1)
HornSchunck(im1, im2);
%% compare to Matlab CV Toolbox
try
    figure(2)
    opticFlow = opticalFlowHS;
    estimateFlow(opticFlow,im1);
    flow = estimateFlow(opticFlow,im2);

    imshow(im2)
    hold on
    plot(flow,'DecimationFactor',[5 5],'ScaleFactor',25)
end  
%% compare to pure Python
try
   system('python ../HornSchunck.py ../data/box/box')
end
end