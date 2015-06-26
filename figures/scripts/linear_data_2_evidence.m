% Matlab script to evaluate the evidence for the linear and noise models
% from linear_data_2.py

% load x and y data
data = load('linear_data_2.txt');

sigma2 = 1.; % variance of data

% get sums required for the integral
d2 = sum(data(2,:).^2)/sigma2;
x2 = sum(data(1,:).^2)/sigma2;
dx = sum(data(1,:).*data(2,:))/sigma2;
d = sum(data(2,:))/sigma2;
x = sum(data(1,:))/sigma2;
n = length(data);

% prior ranges for m and c
ms = [0., 5.];
cs = [-2., 4.];

% create symbolic variables for m and c
syms m c

% perform integral over m
int1 = int(exp(-(d2 + m^2*x2 + n*c^2 + 2*m*c*x - 2*m*dx - 2*c*d)/2), m, ms(1), ms(2));

% perform integral over c
int2 = int(int1, c, cs(1), cs(2));

logpriorm = -log(ms(2)-ms(1));
logpriorc = -log(cs(2)-cs(1));
logprior = logpriorm + logpriorc;

% get log evidence for a linear model in data given sigma^2 = 1
Z1 = -0.5*n*log(2.*pi*sigma2) + log(eval(int2)) + logprior;

% get the log evidence that the data is just Gaussian noise
Z2 = -0.5*n*log(2.*pi*sigma2) - d2/2.;

lnratio = Z1-Z2;
ratio = exp(lnratio);

% now get the evidence in the case that we known that c = 1
Z3 = -0.5*n*log(2.*pi*sigma2) + log(eval(subs(int1, c, 1))) + logpriorm;
lnratio2 = Z1-Z3;
