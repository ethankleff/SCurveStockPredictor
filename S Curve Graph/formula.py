import matplotlib.pyplot as plt
import numpy as np
import math

saturation = int(9100)
growth = int(15)
mid = int(2009)
t = int(2004)


    y = (-1*(np.log(81)))
    y = float(y)
    x = (y/growth)*(t-mid)
    x = float(x)
    z = saturation/(1 + np.e**(x))
    z = float(z)



print(z)
