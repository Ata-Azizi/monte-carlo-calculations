# Monte Carlo Integration and Statistical Analysis

Numerical integration using **Monte Carlo sampling**, implemented in Python with NumPy, SciPy, and Matplotlib.

This project investigates the accuracy, statistical uncertainty, and convergence properties of Monte Carlo integration, including the Gaussian distribution of numerical estimates.

## 1. Mathematical Background

Monte Carlo integration approximates a definite integral using randomly sampled points.

For a function \(f(x)\) defined over \([a,b]\),

$$
I=\int_a^b f(x)\,dx,
$$

the Monte Carlo estimator using \(N\) uniformly distributed samples is

$$
I_N=\frac{b-a}{N}\sum_{i=1}^{N}f(x_i),
\qquad x_i\sim U(a,b).
$$

The statistical uncertainty of the estimator decreases approximately as

$$
\sigma_{I_N}\propto\frac{1}{\sqrt{N}}.
$$

This convergence rate is a fundamental property of standard independent-sampling Monte Carlo methods.

## 2. Numerical Example

The project evaluates

$$
I=\int_0^1 x^4\,dx=\frac15=0.2.
$$

The exact result provides a reference for assessing the numerical accuracy.

The theoretical standard error is

$$
\sigma_{I_N}=
\sqrt{\frac{1/9-1/25}{N}}.
$$

For \(N=1000\),

$$
\sigma_{I_N}\approx0.00843.
$$

## 3. Implementation

**Notebook:** [Monte_Carlo_Integration.ipynb](Monte_Carlo_Integration.ipynb)

The notebook includes:

- Monte Carlo integration using uniformly distributed random samples
- Comparison of numerical and exact integral values
- Statistical uncertainty estimation
- Repeated independent Monte Carlo experiments
- Histogram of the integral estimates
- Gaussian fitting using SciPy
- Numerical convergence analysis
- Verification of the expected \(N^{-1/2}\) error scaling

## 4. Statistical Analysis

According to the Central Limit Theorem, the distribution of Monte Carlo sample means approaches a Gaussian distribution for sufficiently large sample sizes, provided the sampled function has finite variance.

The probability density can be approximated by

$$
p(I_N)=\frac{1}{\sqrt{2\pi}\sigma}
\exp\left[-\frac{(I_N-\mu)^2}{2\sigma^2}\right].
$$

For this example, the expected mean is

$$
\mu=0.2,
$$

and the theoretical standard deviation is

$$
\sigma=\sqrt{\frac{1/9-1/25}{N}}.
$$

The notebook compares numerical estimates with these theoretical predictions.

## 5. Requirements

- Python 3
- NumPy
- SciPy
- Matplotlib
- Jupyter Notebook

## 6. Installation and Usage

Clone the repository:

```bash
git clone https://github.com/Ata-Azizi/monte-carlo-calculations.git
cd monte-carlo-calculations
```

Install dependencies:

```bash
python -m pip install numpy scipy matplotlib jupyter
```

Launch Jupyter:

```bash
jupyter notebook
```

Open `Monte_Carlo_Integration.ipynb` and run all cells.

Alternatively, open the repository in VS Code and select a Python kernel.

## 7. Relevance to Computational Physics

Monte Carlo methods are widely used in computational physics, statistical mechanics, and numerical simulations.

The techniques demonstrated in this project—including random sampling, uncertainty quantification, statistical convergence, and numerical validation—provide useful foundations for stochastic simulation and computational quantum physics.

## Author

**Ata Azizi Seraji**

MSc Theoretical Physics — University of Göttingen, Germany

[GitHub Profile](https://github.com/Ata-Azizi)