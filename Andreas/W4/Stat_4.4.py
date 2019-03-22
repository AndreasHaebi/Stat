from pandas import Series,DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# b) Berechnen Sie die Wahrscheinlichkeit P (E[X1] − 1 ≤ X1 ≤ E[X1] + 1).
norm.cdf(x=2, loc=1, scale=2) - norm.cdf(x=0, loc=1, scale=2)

# c) Berechnen Sie P (E[Sn] − 1 ≤ Sn ≤ E[Sn] + 1).
norm.cdf(x=51, loc=50, scale=np.sqrt(200)) - norm.cdf(x=49, loc=50, scale=np.sqrt(200))

# d)
norm.cdf(x=2, loc=1, scale=np.sqrt(4/50)) - norm.cdf(x=0, loc=1, scale=np.sqrt(4/50))
