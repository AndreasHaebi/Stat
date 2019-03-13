from pandas import Series,DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

schlamm = pd.read_table(r"D:\Git\Stat\W2\klaerschlamm.dat", sep=" ", index_col=0)
schlamm = schlamm.drop("Labor", 1)

# a) Erstellen Sie für jede Probe einen Boxplot, und berechnen Sie jeweils das arithmetische Mittel und den Median. Bei welchen Proben gibt es Ausreisser, und
# wo unterscheiden sich arithmetisches Mittel und Median wesentlich? Bei welchen
# der 9 Proben ist es plausibel, dass die wahre Konzentration unter 400 mg/kg
# liegt?

#Median und Mittelwert sind in der Methode Describe ersichtlich
schlamm.describe()

#Plot
schlamm.plot(kind="box")
plt.show()

# Lösung
# Bei den Proben 1 und 5 ist es plausibel, dass die Konzentration unter 400 mg/kg
# liegt, während wir bei Probe 2, 3, 7 und 8 eher dazu tendieren, den Grenzwert
# 400 mg/kg als überschritten zu betrachten.
# Die übrigen Proben, Probe 4, 6 und 9 sind eher Grenzfälle. Die Konzentrationen
# scheinen zwar unter 400 mg/kg zu liegen, die drei Proben weisen jedoch jeweils
# extreme Ausreisser über dem Grenzwert auf


# b) Erstellen Sie für jedes Labor einen Boxplot der Messfehler. Unter dem Messfehler eines Labors bei einer Probe verstehen wir den gemessenen Wert minus den Median über alle Labors. 
# Welche der 21 Labors haben systematische
# Fehler in ihrem Analyseverfahren? Welche haben grosse Zufallsfehler, und bei
# welchen Labors ist die Qualität der Analysen besonders gut?

schlamm_centered = schlamm - schlamm.median()

schlamm_centered.T.plot(kind="box")
plt.show()

# Lösung
# Als erstes stechen die Messungen der Labors 15 und 21 ins Auge. Beide haben
# sowohl eine grosse Standardabweichung als auch systematische Fehler. Die
# Labors 6 und 12 haben beide Ausreisser zu verzeichnen. Die Labors 1, 7, 12,
# 13, 14, 17, 18, 20 und 21 geben systematisch zu kleine Werte an, während die
# Labors 6, 8, 10 und 15 zu grosse Werte erhalten. Die Labors 2, 3, 4, 5 und 19
# scheinen zuverlässige Untersuchungen durchzuführen. Sowohl systematische
# wie auch Zufallsfehler scheinen sich hier in Grenzen zu halten