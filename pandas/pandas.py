from os import sep
from pickle import FALSE
import pandas as pd

df = pd.read_csv("/content/drive/my drive/datasets/gapminder.csv",error_bad_lines-FALSE, sep-";")
