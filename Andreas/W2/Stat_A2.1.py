from pandas import Series
import matplotlib.pyplot as plt
import numpy as np

# a) Ändern Sie drei Noten im Datensatz so ab, dass der Median gleich bleibt, aber
# der Mittelwert sich stark ändert.

n1 = Series([4.2, 2.3, 5.6, 4.5, 4.8, 3.9, 5.9, 2.4, 5.9, 6, 4, 3.7, 5, 5.2, 4.5, 3.6, 5, 6, 2.8, 3.3, 5.5, 4.2, 4.9, 5.1])

n1.mean()
n1.median()

n2 = n1.sort_values()
n2.size #Grösse = 24 --> Median bildet sich aus n2[12] & n2[13]
#Da index mit sortiert wurde muss er neu gesetzt werden
n2.index = np.arange(1, n2.size+1)

n2[11], n2[10], n2[9] = 1, 1, 1

print("Vergleich Mittelwert")
n1.mean()
n2.mean()

print("\nVergleich Median")
n1.median()
n2.median()

# b) Erstellen Sie zu den beiden Datensätzen je ein Histogramm und einen Boxplot.
# Verwenden Sie plt.subplot(...) aus Aufgabe 1.

plt.subplot(221)
n1.plot(kind="box")
plt.subplot(222)
n2.plot(kind="box")
plt.subplot(223)
n1.plot(kind="hist",edgecolor="black")
plt.subplot(224)
n2.plot(kind="hist",edgecolor="black")
plt.show()
