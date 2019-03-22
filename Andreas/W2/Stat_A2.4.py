from pandas import Series,DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# a) Erstellen Sie von den Daten in Tabelle 1 ein Streudiagramm, in dem Sie die
# Distanz versus Fluchtgeschwindigkeit aufzeichnen.

hubble = pd.read_table("D:\Git\Stat\W2\hubble.txt", sep=" ")
hubble.head()

# b) Bestimmen Sie mit dem Befehl np.polyfit(...) (siehe Skript) die Koeffizienten 
# β0 und β1 für die Regressionsgerade

hubble.plot(kind="scatter",x= "distance", y="recession.velocity")
plt.show()


hubble.plot(kind="scatter",x= "distance", y="recession.velocity")

beta1, beta0 = np.polyfit(y= hubble["distance"], x=hubble["recession.velocity"], deg=1)
x = np.linspace(hubble["recession.velocity"].min(), hubble["recession.velocity"].max())

plt.plot(x, beta0 + beta1*x, color="orange")
plt.show()

# stimmt nicht, keine Ahung was die scheisse soll...

# c) Bestimmen Sie noch den Korrelationskoeffizienten und interpretieren Sie diesen.
hubble.corr()

