import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = [64000, 65000, 66000, 67000, 66500]
days = range(len(data))

plt.plot(days, data, label="Bitcoin Price")
plt.xlabel("Days")
plt.ylabel("Price (USD)")
plt.title("Bitcoin Price Example")
plt.legend()
plt.show()
