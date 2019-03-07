from pandas import Series,DataFrame
import pandas as pd
data = pd.read_csv(r"C:\Git\Stat\W1\child.csv", sep=",", index_col=0)

# Aufgabe 1.1 a (Einlesen der Datei)
data = pd.read_csv(r"C:\Git\Stat\W1\child.csv", sep=",", index_col=0)

data.head()
# Mit data.head werden die ersten 5 Zeilen ausgegeben. Damit kann geprüft werden ob die Datei korrekt eingelesen wurde.


data.shape


data.describe()
data.index

summary(data)