import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def gaussian(x, A, mu, sigma):
    return A * np.exp(-(x - mu)**2 / (2 * sigma**2))
def f2(x):
    return x**8

def f(x):
    return x**4

def I(N,V, func):
    Sum=0
    for i in range (1,N+1):
        x=np.random.random()
        Sum=Sum+func(x)
    estimator=V/N*Sum
    return estimator
def sigma(N,V):
    j=I(1000,1,f2)/V
    k=I(1000,1,f)/V
    error=V*np.sqrt(((j-k**2)/(N-1)))
    return error
z=I(1000,1, f)
w=sigma(1000,1)
multiples=(0.2-z)/w
print(z)
print(w)
print(multiples)
l=[]
for i in range (1000):
    l.append(I(1000,1, f))
print(l)

font = {
    'family': 'serif',  # Choose the font family (e.g., 'serif', 'sans-serif', 'monospace')
    'color':  'Black',   # Font color
    'weight': 'normal', # Font weight ('normal', 'bold', 'heavy', 'light')
    'size': 12 ,         # Font size
    'style': 'italic'   # Set the font style to 'italic'
}
plt.xlabel(r'$I_{N}$',fontdict=font)
plt.ylabel(r'$Count$',fontdict=font)
bin_heights, edges, _ = plt.hist(l, bins=50, density=True)
bin_centers = (edges[:-1] + edges[1:]) / 2

params, covariance = curve_fit(gaussian, bin_centers, bin_heights)
fit_mu, fit_sigma = params[1], params[2]
x = np.linspace(min(bin_centers), max(bin_centers), 100)
y_fit = gaussian(x, *params)
plt.plot(x, y_fit, 'r', label='Fit')

plt.legend()
plt.show()

plt.show()
print(fit_mu, fit_sigma)