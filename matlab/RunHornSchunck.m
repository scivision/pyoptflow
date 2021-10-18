
name = 'sphere';

datadir = fullfile("../src/pyoptflow/tests/data/",name);

fn1 = fullfile(datadir, name + ".0.bmp");
fn2 = fullfile(datadir, name + ".1.bmp");


im1 = im2gray(imread(fn1));
im2 = im2gray(imread(fn2));

figure(1)
HornSchunck(im1, im2);
%% compare to Matlab CV Toolbox
if ~isempty(ver('vision'))
figure(2)
opticFlow = opticalFlowHS;
estimateFlow(opticFlow,im1);
flow = estimateFlow(opticFlow,im2);

imshow(im2)
hold on
plot(flow,'DecimationFactor',[5 5],'ScaleFactor',25)
end
%% compare to pure Python
if ispc
  % Numpy needs mkl*.dll on PATH on Windows
  pe = pyenv;
  old_path = getenv("PATH");
  new_path = fullfile(pe.Home, "Library/bin");
  if ~contains(old_path, new_path, 'IgnoreCase', true)
    setenv('PATH', fullfile(pe.Home, "Library/bin") + pathsep + getenv('PATH'))
  end
end

UV = py.pyoptflow.HornSchunck(py.numpy.asarray(im1), py.numpy.asarray(im2));
U = single(UV{1});
V = single(UV{2});

figure(2)
plotFlow(U,V)
