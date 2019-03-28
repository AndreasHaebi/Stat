import matplotlib.pyplot as plt
import numpy as np
from pandas import Series, DataFrame
import pandas as pd
import scipy.stats as st

# a) Erstellen Sie für jede der 3 Versuchsbedingungen einen Boxplot, 
# am besten gerade nebeneinander. 
# Wie unterscheiden sich die Daten der verschiedenen Versuchsbedingungen?

iron = pd.read_table("D:/Git/Stat/Andreas/W5/ironF3.dat", sep=" ", index_col=False)
iron.plot(kind="box")
plt.show()

# b) Transformieren Sie alle Werte mit dem Logarithmus und erstellen Sie wieder die
# 3 Boxplots wie bei Aufgabe a). Was hat sich durch die Transformation geändert?

plt.subplot(1,2,1)
iron.plot(kind="box",ax=plt.gca())
plt.ylabel("iron")
plt.subplot(1,2,2)
np.log(iron).plot(kind="box",ax=plt.gca())
plt.ylabel("log(iron)")

plt.tight_layout()
plt.show()

# c) Erstellen Sie einen Normalplot der Daten bei mittlerer Dosis vor und nach dem
# Logarithmieren. Wann passt die Normalverteilung besser? Verwenden Sie die
# Python-Funktion

st.probplot(iron["medium"], plot=plt)
plt.show()
st.probplot(np.log(iron["medium"]), plot=plt)
plt.show()

# d) Unter der Annahme, dass die Daten bei mittlerer Dosis normalverteilt sind,
# schätzen Sie die Parameter µ und σ2. Wie gross ist die Wahrscheinlichkeit, dass
# eine Maus mehr als 10 % Eisen zurückhält.
iron["medium"].mean()
iron["medium"].var()
1 - st.norm.cdf(x=10, loc=8.204, scale=np.sqrt(29.67))







