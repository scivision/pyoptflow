
name = 'box';

datadir = fullfile("../src/pyoptflow/tests/data/",name);

fn1 = fullfile(datadir, name + ".0.bmp");
fn2 = fullfile(datadir, name + ".1.bmp");


im1 = imread(fn1);
im2 = imread(fn2);

if ndims(im1) == 3
  im1 = im2gray(im1);
  im2 = im2gray(im2);
elseif islogical(im1)
  im1 = uint8(im1);
  im2 = uint8(im2);
end

fg = figure(1);
%t = tiledlayout(fg, 1, 3);
subplot(1,3,1)
[Umat, Vmat] = HornSchunck(im1, im2);
plotFlow(Umat, Vmat)
title("Matlab plain")
%% compare to Matlab CV Toolbox
if ~isempty(ver('vision'))
%nexttile(t)
subplot(1,3,2)
opticFlow = opticalFlowHS('MaxIteration', 100);
estimateFlow(opticFlow, im1);
flow = estimateFlow(opticFlow, im2);

%plot(flow,'DecimationFactor',[5 5],'ScaleFactor',25)
plotFlow(flow.Vx, flow.Vy)
title("Matlab Computer Vision toolbox")
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

%nexttile(t)
subplot(1,3,3)
plotFlow(U,V)
title("PyOptFlow")
