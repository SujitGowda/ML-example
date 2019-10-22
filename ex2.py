import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

cars_data = pd.read_csv('Toyota.csv',index_col=0,na_values=["??","????"])
print(cars_data)
cars_data.dropna(axis=0,inplace=True)


sns.set(style="darkgrid")
sns.regplot(x=cars_data['Age'],y=cars_data['Price'],marker="*",fit_reg=False)
sns.lmplot(x='Age',y='Price',data=cars_data,fit_reg=False,hue='FuelType',legend=True,palette='Set2')


