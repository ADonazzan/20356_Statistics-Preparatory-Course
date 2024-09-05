import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom, poisson

plt.style.use("seaborn-v0_8-whitegrid")
grapics_dir = "graphics/"

def plot_binomial_pdf():
    n = 20
    p = 0.5
    x = np.linspace(0, n, n + 1)
    y = np.array([binom.pmf(i, n, p) for i in x])\
    
    plt.scatter(x, y, label="n = 20, p = 0.5")
    plt.xlabel("x")
    plt.ylabel("P(X = x)")
    plt.legend()
    plt.savefig(grapics_dir + "binomial_pdf.png", dpi = 300)
    plt.clf()

    # binomial cdf
    y = np.array([binom.cdf(i, n, p) for i in x])
    plt.scatter(x, y, label="n = 20, p = 0.5")
    plt.xlabel("x")
    plt.ylabel("P(X <= x)")
    plt.legend()
    plt.savefig(grapics_dir + "binomial_cdf.png", dpi = 300)
    plt.clf()

def plot_poisson_pdf():
    lambda_ = 5
    x = np.linspace(0, 20, 21)
    y = np.array([poisson.pmf(i, lambda_) for i in x])
    plt.scatter(x, y, label="lambda = 5")
    plt.xlabel("x")
    plt.ylabel("P(X = x)")
    plt.legend()
    plt.savefig(grapics_dir + "poisson_pdf.png", dpi = 300)
    plt.clf()

    # poisson cdf
    y = np.array([poisson.cdf(i, lambda_) for i in x])
    plt.scatter(x, y, label="lambda = 5")
    plt.xlabel("x")
    plt.ylabel("P(X <= x)")
    plt.legend()
    plt.savefig(grapics_dir + "poisson_cdf.png", dpi = 300)
    plt.clf()


def plot_exponential_pdf():
    lambda_ = 0.5
    x = np.linspace(0, 10, 100)
    y = np.array([lambda_ * np.exp(-lambda_ * i) for i in x])
    plt.plot(x, y, label="lambda = 0.5")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.savefig(grapics_dir + "exponential_pdf.png", dpi = 300)
    plt.clf()

    # exponential cdf
    y = np.array([1 - np.exp(-lambda_ * i) for i in x])
    plt.plot(x, y, label="lambda = 0.5")
    plt.xlabel("x")
    plt.ylabel("F(x)")
    plt.legend()
    plt.savefig(grapics_dir + "exponential_cdf.png", dpi = 300)
    plt.clf()

def plot_gamma_pdf():
    alpha = 2
    lambda_ = 0.5
    x = np.linspace(0, 10, 100)
    y = np.array([lambda_ ** alpha * x ** (alpha - 1) * np.exp(-lambda_ * x) for x in x])
    plt.plot(x, y, label="alpha = 2, lambda = 0.5")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.savefig(grapics_dir + "gamma_pdf.png", dpi = 300)
    plt.clf()

    # gamma cdf
    y = np.array([1 - np.exp(-lambda_ * i) for i in x])
    plt.plot(x, y, label="alpha = 2, lambda = 0.5")
    plt.xlabel("x")
    plt.ylabel("F(x)")
    plt.legend()
    plt.savefig(grapics_dir + "gamma_cdf.png", dpi = 300)
    plt.clf()

def plot_weibull_pdf():
    alpha = 2
    lambda_ = 0.5
    x = np.linspace(0, 10, 100)
    y = np.array([alpha * lambda_ * (lambda_ * x) ** (alpha - 1) * np.exp(-lambda_ * x) for x in x])
    plt.plot(x, y, label="alpha = 2, lambda = 0.5")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.savefig(grapics_dir + "weibull_pdf.png", dpi = 300)
    plt.clf()

    # weibull cdf
    y = np.array([1 - np.exp(-lambda_ * i) for i in x])
    plt.plot(x, y, label="alpha = 2, lambda = 0.5")
    plt.xlabel("x")
    plt.ylabel("F(x)")
    plt.legend()
    plt.savefig(grapics_dir + "weibull_cdf.png", dpi = 300)
    plt.clf()
    

if __name__ == "__main__":
    plot_binomial_pdf()
    plot_poisson_pdf()
    plot_exponential_pdf()
    plot_gamma_pdf()
    plot_weibull_pdf()