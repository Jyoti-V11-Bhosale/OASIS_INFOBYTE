#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[4]:


retail = pd.read_csv('retail_sales_dataset.csv')
df = retail.copy()
df.head(5)


# In[3]:


df.info()


# In[5]:


df['Date'] = pd.to_datetime(df['Date'])


# In[6]:


df.info()


# In[7]:


df.isnull().sum()


# In[8]:


df.nunique()


# In[9]:


df.describe()


# In[42]:


mean_total_sales = df["Total Amount"].mean()
print(f"Mean (Average) of 'Total Amount': {mean_total_sales}")
median_total_sales = df["Total Amount"].median()
print(f"Median of 'Total Amount': {median_total_sales}")
mode_total_sales = df["Total Amount"].mode()
print(f"Mode of 'Total Amount': {mode_total_sales[0]}")
std_dev_total_sales = df["Total Amount"].std()
print(f"Standard Deviation of 'Total Amount': {std_dev_total_sales}")


# In[12]:


monthly_transactions = df.groupby(df['Date'].dt.month)
def analyze_month(group):
  """Analyzes data for a single month group."""
  most_bought_category = group['Product Category'].mode().iloc[0] 
  num_customers = group['Customer ID'].nunique()  
  gender_counts = group['Gender'].value_counts()  
  total_spending = group['Total Amount'].sum()
  print(f"Month: {group.name}")
  print(f"  Most bought Product Category: {most_bought_category}")
  print(f"  Number of Customers: {num_customers}")
  if 'Male' in gender_counts:
    print(f"    Male Customers: {gender_counts['Male']}")
  if 'Female' in gender_counts:
    print(f"    Female Customers: {gender_counts['Female']}")
  print(f"  Total spending on all Product Categories: {total_spending:.2f}")
  print()  
monthly_transactions.apply(analyze_month)


# In[15]:


df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month_name()
df['Month']


# In[20]:


df['Month'] = df['Date'].dt.month
transaction_count = df.groupby('Month')['Transaction ID'].count()
plt.figure(figsize=(14,8))
sns.barplot(x=transaction_count.index, y=transaction_count.values)
plt.title('Transaction Frequency Over Months', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Transaction Count', fontsize=14)
plt.show()


# In[28]:


age_bins = [0, 18, 25, 35, 50, 100]
age_group = ['0-18', '19-25', '26-35', '36-50', '50+']
df['Age Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_group)
plt.figure(figsize=(14, 8))
sns.barplot(x='Age Group', y='Quantity', hue='Product Category', data=df, palette='Greens')
plt.title('Product Category Purchased by Age Group', fontsize=16)
plt.xlabel('Age Group', fontsize=14)
plt.ylabel('Quantity Purchased', fontsize=14)
plt.show()


# In[26]:


month_gender_grouped = df.groupby(["Month", "Gender"])["Total Amount"].sum().unstack()
plt.figure(figsize=(20, 8))
month_gender_grouped.plot(kind="bar", stacked=False, colormap="coolwarm")
plt.xlabel("Month")
plt.ylabel("Total Spending")
plt.title("Total Spending by Month and Gender")
plt.legend(title="Gender")
plt.tight_layout()
plt.show()


# In[35]:


gender_counts = df['Gender'].value_counts()
plt.figure(figsize=(8, 6))
sns.barplot(x=gender_counts.index, y=gender_counts.values, palette=['#FFC0CB', '#FF69B4'])
plt.title('Frequency of Gender', fontsize=16, fontweight='bold')
plt.xlabel('Gender', fontsize=14, fontweight='bold')
plt.ylabel('Count', fontsize=14, fontweight='bold')
plt.show()


# In[27]:


heatmap = df.pivot_table(index='Month', columns='Product Category', values='Total Amount')
plt.figure(figsize=(14, 8))
sns.heatmap(heatmap, annot=True, fmt='.0f', cmap='Blues')
plt.title('Sales Heatmap', fontsize=16)
plt.xlabel('Product Category', fontsize=14)
plt.ylabel('Month', fontsize=14)
plt.show()


# In[34]:


total_revenue_by_category = df.groupby('Product Category')['Total Amount'].sum().reset_index()
highest_revenue_category = total_revenue_by_category.loc[total_revenue_by_category['Total Amount'].idxmax()]['Product Category']
df_highest_revenue = df[df['Product Category'] == highest_revenue_category]
pivot_df = df_highest_revenue.pivot_table(index='Month', columns='Product Category', values='Total Amount')

plt.figure(figsize=(14, 8))
sns.lineplot(data=pivot_df, markers=True, dashes=False)
plt.title(f'Sales Trend for {highest_revenue_category}', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Total Sales Amount', fontsize=14)
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


# In[ ]:




