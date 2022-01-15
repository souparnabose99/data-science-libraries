# -*- coding: utf-8 -*-
"""Matplotlib-Operations.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n_Ai_T1GEXl24IJ5zHV8pXaXXAR9KTMs
"""

import matplotlib.pyplot as plt

plt.plot([2,3,5,7,9,1])
plt.xlabel("Indices")
plt.ylabel("Numbers")
plt.title("Num-Plot")
plt.show()

plt.plot([1,2,3,4],[1,4,9,16])
plt.grid()
plt.show()

plt.plot([1,2,3,4],[1,4,9,16], 'ro')
plt.grid()
plt.show()

import numpy as np

a = np.arange(0, 5, 0.2)

plt.plot(a, a**2, "b--", label="^2")
plt.plot(a, a**2.5, "rs", label="^2.5")
plt.plot(a, a**3, "g^", label="^3")
plt.legend()
plt.grid()
plt.show()

plt.plot([1,2,3,4],[1,4,9,16], linewidth=10)
plt.grid()
plt.show()

# Using keyword arguments:
x1 = [1,2,3,4]
y1 = [1,4,9,16]
x2 = x1
y2 = [2,4,6,8]

lines = plt.plot(x1, y1, x2, y2)

plt.setp(lines[0], color='r', linewidth=2)
plt.setp(lines[1], color='g', linewidth=2)

plt.grid()
plt.show()

plt.subplot(221)
plt.plot([1,2,3,4])
plt.subplot(222)
plt.plot([10,20,30,40])

plt.figure(1)
plt.subplot(211)
plt.plot([1,2,3,4])
plt.subplot(212)
plt.plot([10,20,30,40])

plt.figure(2)
plt.subplot(211)
plt.plot([1,2,3,4])
plt.subplot(212)
plt.plot([10,20,30,40])

plt.figure(1)
plt.subplot(221)
plt.plot([1,2,3,4])
plt.subplot(222)
plt.plot([2,6,8,3])

plt.figure(2)
plt.subplot(221)
plt.plot([1,2,3,4])
plt.subplot(222)
plt.plot([0.3, 0.9, 31, 13])

