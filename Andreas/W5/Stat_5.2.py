import matplotlib.pyplot as plt
import numpy as np
from pandas import Series, DataFrame
import scipy.stats as st

# a) - d) Simulieren Sie X. Stellen Sie die Verteilung von X mittels eines Histogramms
# von 1000 Realisierungen von X dar, und vergleichen Sie sie mittels des Normalplots mit der Normalverteilung.

werte = np.array([0,10,11])
sim = Series(np.random.choice(werte, size=1000, replace=True))

plt.subplot(4,2,1)
sim.hist(bins=[0,1,10,11,12],edgecolor="black")
plt.title("Original")
plt.subplot(4,2,2)
st.probplot(sim,plot=plt)
plt.title("Normal Q-Q Plot")

n = 5
sim = np.random.choice(werte, size=n*1000, replace=True)
sim = DataFrame(np.reshape(sim,(n,1000)))
sim_mean = sim.mean()

plt.subplot(4,2,3)
sim_mean.hist(edgecolor="black")
plt.title("Mittelwerte von 5 Beobachtungen")
plt.subplot(4,2,4)
st.probplot(sim_mean,plot=plt)
plt.title("Normal Q-Q Plot")

n = 10
sim = np.random.choice(werte, size=n*1000, replace=True)
sim = DataFrame(np.reshape(sim,(n,1000)))
sim_mean = sim.mean()

plt.subplot(4,2,5)
sim_mean.hist(edgecolor="black")
plt.title("Mittelwerte von 10 Beobachtungen")
plt.subplot(4,2,6)
st.probplot(sim_mean,plot=plt)
plt.title("Normal Q-Q Plot")

n = 200
sim = np.random.choice(werte, size=n*1000, replace=True)
sim = DataFrame(np.reshape(sim,(n,1000)))
sim_mean = sim.mean()

plt.subplot(4,2,7)
sim_mean.hist(edgecolor="black")
plt.title("Mittelwerte von 200 Beobachtungen")
plt.subplot(4,2,8)
st.probplot(sim_mean, plot=plt)
plt.title("Normal Q-Q Plot")

plt.tight_layout()
plt.show()

import numpy as np
from pandas import Series, DataFrame
werte = np.array([0,10,11])
n = 200
sim = np.random.choice(werte, size=n*1000, replace=True)
sim = DataFrame(np.reshape(sim,(n,1000)))
sim_mean = sim.mean()
sim_mean.mean()
sim_mean.std()



