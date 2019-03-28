import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st


# a) Simulieren Sie n = 10, 20, 50 und 100 (standard-) normalverteilte Zufallszahlen
# und betrachten Sie die jeweilige Folge mit einem Normalplot.
# Wiederholen Sie diese Simulationen einige Male, bis Sie abschätzen können, wie
# weit zufällige Abweichungen von einer Geraden im Normalplot üblich sind.

plt.subplot(2, 2, 1)
x = st.norm.rvs(size = 10)
st.probplot(x, plot = plt)
plt.title("n=10")

plt.subplot(2, 2, 2)
x = st.norm.rvs(size = 20)
st.probplot(x, plot = plt)
plt.title("n=20")

plt.subplot(2, 2, 3)
x = st.norm.rvs(size = 50)
st.probplot(x, plot = plt)
plt.title("n=50")

plt.subplot(2, 2, 4)
x = st.norm.rvs(size = 100)
st.probplot(x, plot = plt)
plt.title("n=100")
plt.tight_layout()
plt.show()

# b) Langschwänzige Verteilung: Simulieren Sie je n = 20 und 100 t-verteilte Zufallszahlen mit ν = 20, 7 und 3 Freiheitsgraden. 
# Wiederholen Sie diese Simulationen einige Male, bis Sie abschätzen können, wie gross Abweichungen von einer
# Geraden im Normalplot üblich sind.

# n = 20 & verteilte Zufallszahlen 20

for i in range(1,4):
    plt.subplot(1,3,i)
    x = st.t.rvs(size=20, df=20)
    st.probplot(x,plot=plt)
    plt.title("n=20, df=20")
plt.tight_layout()
plt.show()
# n = 100 & verteilte Zufallszahlen 20
for i in range(1,4):
    plt.subplot(1,3,i)
    x = st.t.rvs(size=100, df=20)
    st.probplot(x,plot=plt)
    plt.title("n=100, df=20")
plt.tight_layout()
plt.show()
# n = 20 & verteilte Zufallszahlen 7
for i in range(1,4):
    plt.subplot(1,3,i)
    x = st.t.rvs(size=20, df=7)
    st.probplot(x,plot=plt)
    plt.title("n=20, df=7")
plt.tight_layout()
plt.show()
# n = 100 & verteilte Zufallszahlen 7
for i in range(1,4):
    plt.subplot(1,3,i)
    x = st.t.rvs(size=100, df=7)
    st.probplot(x,plot=plt)
    plt.title("n=100, df=7")
plt.tight_layout()
plt.show()
# n = 20 & verteilte Zufallszahlen 3
for i in range(1,4):
    plt.subplot(1,3,i)
    x = st.t.rvs(size=20, df=3)
    st.probplot(x,plot=plt)
    plt.title("n=20, df=3")
plt.tight_layout()
plt.show()
# n = 100 & verteilte Zufallszahlen 3
for i in range(1,4):
    plt.subplot(1,3,i)
    x = st.t.rvs(size=100, df=3)
    st.probplot(x,plot=plt)
    plt.title("n=100, df=3")
plt.tight_layout()
plt.show()

for i in range(1,4):
    plt.subplot(1,3,i)
    x = st.t.rvs(size=20, df=1)
    st.probplot(x,plot=plt)
    plt.title("n=20,df=1")
plt.tight_layout()
plt.show()

plt.figure(figsize=(6,3))
for i in range(1,4):
    plt.subplot(1,3,i)
    x = st.t.rvs(size=100, df=1)
    st.probplot(x,plot=plt)
    plt.title("n=100,df=1")
plt.tight_layout()
plt.show()

# c) Schiefe Verteilung: Simulieren Sie je n = 20 und 100 chiquadrat-verteilte 
# Zufallszahlen mit ν = 20 und 1 Freiheitsgraden. Wiederholen Sie diese Simulationen
# einige Male, bis Sie abschätzen können, wie gross Abweichungen von einer Geraden im Normalplot üblich sind.

plt.subplot(2, 2, 1)
x = st.chi2.rvs(size = 20, df = 20)
st.probplot(x, plot = plt)
plt.title("n=20, df=20")

plt.subplot(2, 2, 2)
x = st.chi2.rvs(size = 100, df = 20)
st.probplot(x, plot = plt)
plt.title("n=100, df=20")

plt.subplot(2, 2, 3)
x = st.chi2.rvs(size = 20, df = 1)
st.probplot(x, plot = plt)
plt.title("$n=20, df=1")

plt.subplot(2, 2, 4)
x = st.chi2.rvs(size = 100, df = 1)
st.probplot(x, plot = plt)
plt.title("n=100, df=1")

plt.tight_layout()
plt.show()




