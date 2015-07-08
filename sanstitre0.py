# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 15:48:27 2015

@author: MS241591
"""

import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0,10,1000)
Y = np.sin(2*np.pi*0.5*X)

plt.plot(X,Y)