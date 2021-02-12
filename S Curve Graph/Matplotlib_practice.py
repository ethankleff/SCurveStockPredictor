import matplotlib.pyplot as plt
import numpy as np
t = np.arange(0.,5.,0.2)





plt.figure(1)
plt.subplot(211)
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
plt.axis([0,5,0,150])
plt.ylabel(' Growth percentage')
plt.xlabel(' Years')

plt.figure(2)
plt.subplot(212)
n = np.arange(0.,5.,0.2)
plt.plot(n,n,'r--')
plt.show()
