from pandas import Series,DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# a) Eine Elektronik-Firma stellt Widerstände her, die einen mittleren Widerstand
# von 100 Ω und eine Standardabweichung von 10 Ω haben. Die Widerstände
# sind normalverteilt. Bestimmen Sie die Wahrscheinlichkeit, dass sich für eine
# zufällige Stichprobe von n = 25 Widerständen ein mittlerer Widerstand unter
# 95 Ω ergibt.

# scale = standardfehler
# Standardfehler = Standardabweichung / √Stichproben
# Standardfehler = 10 / √25 = 2
# Formel auf Folie W4 Gesetz der grossen Zahlen Nr. 35

norm.cdf(x=95, loc=100, scale=2)
