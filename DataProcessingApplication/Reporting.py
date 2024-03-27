import json
import pandas as pd
import matplotlib.pyplot as plt
import webbrowser
import  pytest
from abc import ABC, abstractmethod

# Stradegy Pettern Data Processing Strategeies

# interface

class DataProcess(ABC):
    @abstractmethod
    def process_data(self, data):
        pass

#Concrete class

class MonthlySalesAnalysis(DataProcess):

    def process_data(self, data):

        pd_data = panda_data_frame(data)
        # convert the data column to datetime format for easier manipulation
        pd_data['data'] = pd.to_datetime(pd_data['data'])
        # Group the data by "Branch id" and "year month" and calculate the total sale
        pd_data['year_month'] = pd_data['date'].dt.to_period('M')
        #analyse data
        pd_data_quantity = (pd_data.groupby(['branch_id','year_month'])
                            .agg({'quantity': 'sum', 'price': 'sum'})
                            .sort_values(by= 'quantity', ascending=False)
                            .reset_index())

        pd_data_quantity.rename(columns= {'price': 'Total_income'}, inplace=True)
        print("monthly data analysing....")
        plt.figure(figsize=(10,5))
        plt.axis('off')
        plt.subplot(2,1,1)
        plt.title('quantity of sale')
        pd_data_quantity['quantity'].value_counts(normalize=True).plot.pie(labels=pd_data_quantity['branch_id'])
        plt.subplot(2,1,2)
        plt.xlabel('Branch ID')
        plt.ylabel('Total Income')
        plt.title('Total Income by Branch')
        plt.bar(pd_data_quantity['branch_id'], pd_data_quantity['Total_income'], width = 0.4)

        #pd_data_quantity['Total_income'].value_counts(normalize=True).plot(kind='bar', title ='Income')
        plt.show()
        return  pd_data_quantity


class PriceAnalysis(DataProcess):
    def process_data(self, data):
        pd_data = panda_data_frame(data)
        product_analysis = pd_data.groupby('product_id').agg({
            'quantity' : ['sum','mean'], # Total Quantity sold and average quantity per transaction
            'price' : lambda x: x.iloc[0], # Price of one item(assuming price is constant for a
            'transaction_id' : 'count' # count of transaction for each product

        }).reset_index()

        # rename column
        product_analysis.columns = ['Product_id', 'Total_quantity_sold', 'Average_quantity_per_transaction','Price_of_one_item', 'Transaction_count']

        #sorting base on quantity
        product_analysis = product_analysis.sort_values(by='Total_quantity_sold', ascending=False).reset_index()
        print("Price analysing...")
        plt.figure(figsize=(10,5))
        plt.axis('off')
        plt.subplot(2,1,1)
        plt.title("Total Sold Quantity of each Item")
        plt.pie(product_analysis['Total_quantity_sold'],labels=product_analysis['Product_id'])
        plt.subplot(2,1,2)
        plt.xlabel('Item ID')
        plt.ylabel('Total Income')
        plt.title('Total Income by Item')
        plt.bar(product_analysis['Product_id'],product_analysis['Total_quantity_sold']*product_analysis['Price of one_item'],width = 0.4)


class WeeklySalesAnalysis(DataProcess):

    def process_data(self, data):
        pd_data = panda_data_frame(data)
        weekly_sales = pd_data.groupby(['week_number','branch_id']).agg({'quantity': 'sum', 'price': 'sum'})
        weekly_sales1 = pd_data.groupby('week_number').agg({'quantity' : 'sum', 'price' : 'sum'}).reset_index()
        #sorting base on week number and quantity
        weekly_sales = weekly_sales.sort_value(by = ['week_number', 'quantity'], ascending =[True, False]).reset_index()
        # rename columns
        weekly_sales.columns = ['Week_number', 'Branch_id', 'Quntity_of_items_sold', 'Income']
        print("Weekly data analysis")
        plt.figure(figsize=(10,5))
        plt.axis('off')
        plt.subplot(2, 1, 1)
        plt.title("Total Quantity of each Item sold in each week")
        plt.pie(weekly_sales1['quantity'], labels=weekly_sales1['week_number'])
        plt.subplot(2, 1, 2)
        plt.xlabel('Week number')
        plt.ylabel('Total Income')
        plt.title('Total Income by week')
        plt.bar(weekly_sales1['week_number'],weekly_sales1['price'], width = 0.4)
        plt.show()
        return  weekly_sales


class ProductPreferenceAnalysis(DataProcess):
    def process_data(self, data):
        pd_data= panda_data_frame(data)
        product_preferece = pd_data.groupby('product_id').agg({
           'quantity': 'sum',
           'price': ['mean', 'sum'], #average price
           'transaction_id': 'count' #number of transaction
        })

        #rename
        product_preferece.columns = ['Total_Quantity_sold','Average_income','Total_income','Number_of_Transactions']
        # sorting base on quantity
        product_preferece = product_preferece.sort_values(by='Total_Quantity_Sold', ascending=False).reset_index())
        print("Product Preference data analysing ...")
        plt.figure(figsize=(10,5))
        plt.axis('off')























# (Interface Strategy)
class DataProcessingApplication(ABC):
  @abstractmethod
  def (self):
    pass

# Concrete Strategies
class SquareAreaCalculator(ShapeAreaCalculator):
  def __init__(self, side):
    self.side = side

  def calculate_area(self):
    return self.side * self.side

class CircleAreaCalculator(ShapeAreaCalculator):
  def __init__(self, radius):
    self.radius = radius

  def calculate_area(self):
    return 3.14159 * self.radius * self.radius

# Context
class Shape:
  def __init__(self, area_calculator):
    self.area_calculator = area_calculator

  def get_area(self):
    return self.area_calculator.calculate_area()

# Usage
# HR = ModelType(HR(data))
square = Shape(SquareAreaCalculator(5))
print("Square Area:", square.get_area())

circle = Shape(CircleAreaCalculator(3))
print("Circle Area:", circle.get_area())
