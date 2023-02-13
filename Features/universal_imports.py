#------------------------------
# LIBRARIES

import flask
import pandas as pd
import datetime
import random
import time
import os

# fix MacOS compatibility issue
import matplotlib.pyplot as plt
# plt.switch_backend('Agg')

import seaborn as sns
# set desired graph size and font
sns.set(rc={'figure.figsize':(9,3)})
sns.set_theme(font_scale = 1)
# set background color
sns.set(rc={"axes.facecolor":"white", "figure.facecolor":"white"})

#------------------------------
# DATABASE IMPORT

# Not yet implemented in beta. This program will work first on offline data.

#------------------------------
# IMPORT FEATURES

# We do NOT import all features in the universal import file because we don't want a feature to call itself.