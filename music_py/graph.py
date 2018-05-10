#!usr/bin/env/ python3
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0.0, 0.01, int(44100*0.01))
triangle_formula = np.sin(2.0 * np.pi * 440 * time)

plt.plot(time, triangle_formula)
plt.show()