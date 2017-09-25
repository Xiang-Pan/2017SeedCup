import math
import csv
import random
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import cross_val_score


base_elo = 1600
team_elos = {} 
team_stats = {}
X = []
y = []
folder = 'data' #存放数据的目录



