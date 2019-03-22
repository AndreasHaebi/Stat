import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np


# Erzeugen Sie mit norm.rvs() m = 500 Stichproben aus einer 
# Standardnormalverteilung mit Umfang n = 5. Speichern Sie die Stichproben als (n × m)− Matrix ab.

n = 5
m = 500
ran = np.array(norm.rvs(size=n*m))
sim = ran.reshape((n,m))

# a) Stellen Sie die Stichproben als Runs graphisch dar, und staunen Sie über die
# zahlreichen möglichen Verläufe.

out = plt.plot(sim)
plt.show()

# b) Berechnen Sie nun für jede Stichprobe den Mittelwert x¯, und erzeugen Sie ein
# Histogramm der Mittelwerte. Aus der Theorie wissen Sie, dass die Mittelwerte
# normalverteilt mit Parameter µ = 0 und Standardabweichung σ = √1n sein müssten. 
# Überprüfen Sie dies graphisch mit Hilfe von Histogrammen und dertheoretischen Wahrscheinlichkeitsdichtekurve

plt.hist(sim.T, bins=20, density=True, edgecolor="black", facecolor="white")
x = np.linspace(-4, 4, num=100)
y = norm.pdf(x)
plt.plot(x,y)
plt.title("Histogramm sim")
plt.show()

sim_mean = sim.mean(axis=0)
plt.hist(sim_mean, density=True, edgecolor="black", facecolor="white")
x = np.linspace(-4, 4, num=100)
y = norm.pdf(x, loc=0, scale=1/np.sqrt(n))
plt.plot(x,y)
plt.title("Histogramm sim_mean")
plt.show()

# c) Wiederholen Sie die Aufgabe für n = 2, 10, 100
# n = 2
# n = 10
n = 100

m = 500
ran = np.array(norm.rvs(size=n*m))
sim = ran.reshape((n,m))


plt.hist(sim.T, bins=20, density=True, edgecolor="black", facecolor="white")
x = np.linspace(-4, 4, num=100)
y = norm.pdf(x)
plt.plot(x,y)
plt.title("Histogramm sim")
plt.show()

sim_mean = sim.mean(axis=0)
plt.hist(sim_mean, density=True, edgecolor="black", facecolor="white")
x = np.linspace(-4, 4, num=100)
y = norm.pdf(x, loc=0, scale=1/np.sqrt(n))
plt.plot(x,y)
plt.title("Histogramm sim_mean")
plt.show()









