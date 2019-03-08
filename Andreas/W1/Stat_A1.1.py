from pandas import Series,DataFrame
import pandas as pd
# ---------------------------------------
# Aufgabe 1.1 a (Einlesen der Datei)
# -----------------------------------------
data = pd.read_csv(r"D:\Git\Stat\W1\child.csv", sep=",", index_col=0)

data.head()
# Mit data.head werden die ersten 5 Zeilen ausgegeben. Damit kann geprüft werden ob die Datei korrekt eingelesen wurde.

# ---------------------------------------
# Aufgabe 1.1 b
# b) Überprüfen Sie mit dem Attribut .shape die Dimension der Daten.
# -----------------------------------------
data.shape

# Der Datensatz enthält also 30 Zeilen und 21 Spalten

# ---------------------------------------
# Aufgabe 1.1 c
# c) Bestimmen Sie den Mittelwert und Median der einzelnen Variablen mit dem
# Python-Attribut .describe().
# -----------------------------------------

data.describe() #zusammenfassung
data.mean() #Mittelwert
data.median() #Median

# ---------------------------------------
# Aufgabe 1.1 d
# Überprüfen Sie, ob die Niederlande in der Länderliste des Datensatzes auftaucht. Gibt es auch einen Eintrag für China? Die Zeilennamen ermitteln Sie
# mit dem Attribut .index.
# Wie erhalten Sie die Spaltennamen?
# -----------------------------------------

data.index                      #Array aus Zeilennamen
data.columns                    #Array aus Spaltennamen
"China" in data.index           #Checkt ob China als Zeilenname existiert
"Netherlands" in data.index     #Checkt ob Netherlands als Zeilenname existiert

# ---------------------------------------
# Aufgabe 1.1 e
# In welchen fünf Ländern waren die meisten Jugendlichen mindestens zweimal
# betrunken? Wie hoch ist der maximale Prozentsatz? Benützen Sie die Methode .sort_values(by=..., ascending=...). 
# -----------------------------------------

drunk = data.sort_values(by="Drunkenness", ascending=False)
drunk["Drunkenness"].head()
data.loc["Denmark", "Drunkenness"] #???

# ---------------------------------------
# Aufgabe 1.1 f
# f) In welchem Land ist die Säuglingssterblichkeit am geringsten? Wie hoch ist sie
# in diesem Land? Benützen Sie die Methode .nsmallest(...)
# -----------------------------------------

infant = data.nsmallest(n=1, columns = "Infant.mortality")
infant["Infant.mortality"]

# ---------------------------------------
# Aufgabe 1.1 g
# g) In welchen Ländern ist der Prozentsatz an Jugendlichen, die sich regelmässig
# bewegen, kleiner als der Durchschnitt? Benützen Sie das Attribut .mean() und
# -----------------------------------------

mean_phys = data["Physical.activity"].mean()
data.loc[data["Physical.activity"] < mean_phys,:].index