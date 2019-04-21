from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------
# a) Zeichnen Sie Histogramme von der Zeitspanne zwischen zwei Ausbrüchen.
# Lesen Sie zuerst die Datei ein
# -----------------------------------------
geysir = pd.read_table(r"C:\Users\Andreas\Documents\Projekte\Stat\Andreas\W1\geysir.dat", sep=" ", index_col=0)
geysir.head()

plt.subplot(131)
geysir["Zeitspanne"].plot(kind="hist", edgecolor="black")
plt.xlabel("10 Klassen")

plt.subplot(132)
geysir["Zeitspanne"].plot(kind="hist", bins=20, edgecolor="black")
plt.xlabel("20 Klassen")

plt.subplot(133)
geysir["Zeitspanne"].plot(kind="hist", bins=np.arange(41,107,11), edgecolor="black")
plt.xlabel("Klassengrenzen 41, 52 , 63, 74 , 85, 96")

plt.show()

# ---------------------------------------
# b) Zeichnen Sie Histogramme (Anzahl Klassen variieren) von der Eruptionsdauer:
# -----------------------------------------
plt.subplot(221)
geysir["Eruptionsdauer"].plot(kind="hist", bins=5, edgecolor="black")
plt.xlabel("5 Klassen")

plt.subplot(222)
geysir["Eruptionsdauer"].plot(kind="hist", bins=10, edgecolor="black")
plt.xlabel("10 Klassen")

plt.subplot(223)
geysir["Eruptionsdauer"].plot(kind="hist", bins=20, edgecolor="black")
plt.xlabel("20 Klassen")

plt.subplot(224)
geysir["Eruptionsdauer"].plot(kind="hist", bins=30, edgecolor="black")
plt.xlabel("30 Klassen")

plt.show()

# ---------------------------------------
# c) Zeichnen Sie die empirische kumulative Verteilungsfunktion von der 
# Eruptionsdauer von Old Faithful Geysir. Untersuchen Sie, wie viel Prozent der 
# Eruptionen höchstens 2 Minuten gedauert haben, sowie welche Eruptionsdauer der
# 60 % Eruptionen, die am längsten gedauert haben, mindestens gedauert haben.
# -----------------------------------------
geysir["Eruptionsdauer"].plot(kind="hist", normed=True, cumulative=True, edgecolor="black")
plt.show()
