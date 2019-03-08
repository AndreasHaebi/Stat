# ---------------------------------------
# Aufgabe 1.2
# a) Lesen Sie die auf Ilias abgelegte Datei d.fuel.dat ein mit dem folgenden
# Pandas-Befehl:
# -----------------------------------------

from pandas import DataFrame, Series
import pandas as pd

fuel = pd.read_table(r"D:\Git\Stat\W1\d.fuel.dat", sep=",", index_col=0)
fuel

# ---------------------------------------
# b) Wählen Sie nur die fünfte Zeile des Dataframe d.fuel aus. Welche Werte stehen in der fünften Zeile? 
# Verwenden Sie das Attribut .loc (siehe Aufgabe 1)).
# -----------------------------------------

fuel.loc[5,:]

# ---------------------------------------
# c) Wählen Sie nun die erste bis fünfte Beobachtung des Datensatzes aus. So lässt
# sich übrigens bei einem unbekannten Datensatz ein schneller Überblick über
# die Art des Dataframe gewinnen.
# -----------------------------------------

fuel.loc[1:5,:]
fuel.head()

# ---------------------------------------
# d) Berechnen Sie den Mittelwert der Reichweiten aller Autos in Miles/Gallon
# -----------------------------------------

fuel["mpg"].mean()

# ---------------------------------------
# e) Berechnen Sie den Mittelwert der Reichweite der Autos 7 bis 22.
# -----------------------------------------

fuel.loc[7:22,:].mean()

# ---------------------------------------
# f) Erzeugen Sie einen neuen Vektor t_kml, der alle Reichweiten in km/l, und
# einen Vektor t_kg, der alle Gewichte in kg enthält.
# -----------------------------------------

t_kml = fuel["mpg"]*1.6093/3.789
t_kml
t_kg = fuel["weight"]*0.45359
t_kg

# ---------------------------------------
# g) Berechnen Sie den Mittelwert der Reichweiten in km/l und denjenigen der
# Fahrzeuggewichte in kg.
# -----------------------------------------

t_kml.mean()
t_kg.mean()