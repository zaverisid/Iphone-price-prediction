import pandas
import matplotlib.pyplot as plt


data = pandas.read_csv('iphone_price.csv')
# model.LinearRegression()
# model.fit(data[['version']], data[['price']])
# print(model.predict[[14]])

plt.scatter(data['version'], data['price'])
plt.show()
