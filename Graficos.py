import pandas as pd
import matplotlib.pyplot as plt 

amdprocess = pd.read_csv('./amd_processors.csv')
print(amdprocess.head(5))

bench = pd.read_csv("cpu_benchmarks.csv")
print(bench.head(10))

intelark = pd.read_csv("intel_ark_processors.csv")
print(intelark.head(10))

intelprocess = pd.read_csv("intel_processors.csv")
print(intelprocess.head(10))

comp11 = pd.read_csv("Windows11_supported_intel_processors.csv")
print(comp11.head(10))

cores = amdprocess.groupby('cores')['cores'].count()
amdprocess.plot(kind = 'bar')
plt.show()

plt.scatter(amdprocess['name'],amdprocess['threads'])
plt.show()

plt.pie(cores, labels=cores)
plt.show()


