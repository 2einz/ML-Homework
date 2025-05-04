import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sklearn.svm
import sklearn.metrics
from sklearn.model_selection import GridSearchCV

from scipy.io import loadmat

def load_data(filename):
    return loadmat(filename)
