
import numpy as np
from pandas import Series

# a) Berechnen Sie die arithmetischen Mittelwerte der beiden Methoden und geben
# Sie für jede Methode den absoluten Fehler an

methode_A = Series([79.98 , 80.04 , 80.02 , 80.04 , 80.03 , 80.03 , 80.04 , 79.97 , 80.05 , 80.03, 80.02 , 80.00 , 80.02])
methode_A.mean()
methode_A.std() / np.sqrt(methode_A.size)

methode_B = Series([80.02 , 79.94 , 79.98 , 79.97 , 79.97 , 80.03 , 79.95 , 79.97 ])
methode_B.mean()
methode_B.std() / np.sqrt(methode_B.size)


# b) Wie lauten die relativen Fehler
methode_A.std() / np.sqrt(methode_A.size) / methode_A.mean()
methode_B.std() / np.sqrt(methode_B.size) / methode_B.mean()

