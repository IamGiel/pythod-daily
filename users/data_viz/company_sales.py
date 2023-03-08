import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("C:/Users/lfage/Downloads/company_sales_data.csv")
df.head(5)
df.columns.values

# ['month_number', 'facecream', 'facewash', 'toothpaste',
#        'bathingsoap', 'shampoo', 'moisturizer', 'total_units',
#        'total_profit']

profit_list = df['total_profit'].tolist()
month_list = df['month_number'].tolist()
face_cream_list = df['facecream'].tolist()

profit_list

print(np.arange(1000,18000,1000))

plt.plot(month_list, profit_list, label = 'Month-wise Profit data of last year', color='red', linewidth=3, marker='o', markerfacecolor='black', markersize=5)
plt.plot(month_list, face_cream_list, label = 'Face Cream Profit data of last year', color='blue', linewidth=3, marker='o', markerfacecolor='blue', markersize=5)


plt.xlabel('month')
plt.ylabel('profits')
plt.xticks(month_list)
plt.yticks(np.arange(1000,18000,1000))
plt.legend(loc="best")
plt.show()