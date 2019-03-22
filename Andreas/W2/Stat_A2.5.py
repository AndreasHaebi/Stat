from pandas import Series,DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#  a) Lesen Sie den Datensatz income.dat ein und generieren Sie Streudiagramme, 
#  in welchen das Einkommen versus Anzahl Jahre Schulbildung und Einkommen versus 
#  Intelligenzquotient aufgetragen sind.

income = pd.read_table(r"D:\Git\Stat\W2\income.dat", sep=" ")
income.head()

# Einkommen versus Anzahl Jahre Schulbildung
income.plot(kind="scatter",x= "Educ", y="Income2005")
# plt.show()

b, a = np.polyfit(income["Educ"], income["Income2005"], deg=1)
x = np.linspace(income["Educ"].min(), income["Educ"].max())

plt.plot(x, a+b*x, c="orange")
plt.show()

# inkommen versus Intelligenzquotient
income.plot(kind="scatter",x= "AFQT", y="Income2005")
# plt.show()
b, a = np.polyfit(income["AFQT"], income["Income2005"], deg=1)
x = np.linspace(income["AFQT"].min(), income["AFQT"].max())
plt.plot(x, a+b*x, c="orange")
plt.show()

# b) Bestimmen Sie die Parameter a und b des linearen Modells y = a + bx, wobei y
# das Einkommen bezeichnet und x die Anzahl Jahre Schulbildung. Zeichnen Sie
# die Regressionsgerade wie im Skript

# Print siehe a)
print (a, b)

# Wir finden also die Werte a = −40′200 und b = 6451 für den Fall von Einkommen gegen Anzahl Jahre Schulbildung ( und a = 21′182 und b = 518.68 für
# den betrachteten Fall Einkommen gegen Intelligenzquotient). Mit jedem zusätzlichen Jahr Schulbildung geht also eine jährliche Einkommenszunahme von
# 6451 USD einher.
# Nun ist allerdings Vorsicht geboten: jemand ohne Schulbildung würde ein Einkommen von −40′200 USD haben. Dies macht natürlich keinen Sinn. Wann
# immer man in Bereiche extrapoliert, wo keine Datenpunkte vorhanden waren, ist Vorsicht bei der Interpolation geboten

# c) Berechnen Sie die Korrelation zwischen Einkommen und Anzahl Jahre Schulbildung. 
# Wie angebracht ist ein Regressionsmodell für diesen Datensatz?
income.corr()

# Da der Korrelationskoeffizient mit 0.346 relativ klein ist, scheint ein Modell beruhend
# auf einem linearen Zusammenhang zwischen Einkommen und Anzahl Jahre Schulbildung nicht angebracht zu sein.
