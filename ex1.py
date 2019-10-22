import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cars_data = pd.read_csv('Toyota.csv',index_col=0,na_values=["??","????"])
print(cars_data)
cars_data.dropna(axis=0,inplace=True)
print(cars_data)
plt.scatter(cars_data['Age'],cars_data['Price'],c='blue')
plt.title('scatter plot of PRICE vs AGE OF CARS')
plt.xlabel('Age:(Months)')
plt.ylabel('Price:(Dollersa)')
plt.show()
plt.hist(cars_data['KM'])
plt.show()
plt.hist(cars_data['KM'],color='green',edgecolor='white',bins=6)
plt.title('Histogram of Kilometer')
plt.xlabel('KM')
plt.ylabel('Frequency')
plt.show()
count=[979,120,12]
fuelType=['petrol','diesel','CNG']
index=np.arange(len(fuelType))

plt.bar(index,count,color=['red','blue','cyan'])
plt.title('Bar plots of FUEL Types')
plt.xlabel('FuelType')
plt.ylabel('Frequency')
plt.show()



plt.bar(index,count,color=['red','blue','cyan'])
plt.title('Bar plots of FUEL Types')
plt.xlabel('FuelType')
plt.ylabel('Frequency')
plt.xticks(index,fuelType,rotation=90)
plt.show()


