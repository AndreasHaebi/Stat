from pandas import Series
import pandas as pd
import numpy as np

# ---------------------------------------
# Aufgabe 1.3
# a) Berechnen Sie die Summen ∑ xi und ∑ x2i.
# -----------------------------------------

x = Series([2.1,2.4,2.8,3.1,4.2,4.9,5.1,6.0,6.4,7.3,10.8,12.5,13.0,13.7,14.8,17.6,19.6,23.0,25.0,35.2,39.6])
x.sum()
(x*x).sum()

# ---------------------------------------
# Aufgabe 1.3
# b) Berechnen Sie den Mittelwert und die Standardabweichung (ohne die in pandas
# implementierten Funktionen, sondern aufgrund der Definition der Grössen).
# -----------------------------------------
mean_x = x.sum() / x.size
mean_x
n = x.size
var_x = 1/(n-1) * ((x-mean_x)**2).sum()
standardabweichung = var_x**0.5
standardabweichung = np.sqrt(var_x)
standardabweichung

# ---------------------------------------
# Aufgabe 1.3
# c) Bestimmen Sie den Median (ohne die in pandas implementierte Funktion, sondern aufgrund der Definition der Grössen).
# Python -Hinweis: Verwenden Sie zum Sortieren die Methode .sort_values()
# und den Befehl np.round() zum Runden.
# -----------------------------------------

x_sorted = x.sort_values()
n = x.size
k = np.round(0.5*n+0.5)-1
x_sorted[k]

# ---------------------------------------
# Aufgabe 1.3
# d) Bestimmen Sie nun Mittelwert, Standardabweichung, Median und das 75 %
# Quantil mit den Methoden .mean(), .std(), .median().
# -----------------------------------------

x.mean()
x.std()
x.median()
x.quantile(q=.75, interpolation="lower")

# ---------------------------------------
# Aufgabe 1.3
# e) Überprüfen Sie aufgrund des Datenvektors mit den landwirtschaftlichen Nutzflächen, 
# dass das arithmetische Mittel der standardisierten Variablen
# <<Formel>>
# gleich null und die empirische Standardabweichung von zi gleich 1 ist.
# -----------------------------------------
z = (x-x.mean())/x.std()
z.mean()
z.std()