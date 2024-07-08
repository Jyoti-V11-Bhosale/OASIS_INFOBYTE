#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
apps_with_duplicates = pd.read_csv('apps.csv')
apps = apps_with_duplicates.drop_duplicates()
print('Total number of apps in the dataset = ', len(apps))
print(apps.info())
n = 5
apps.sample(n)


# In[8]:


chars_to_remove = ['+', ',', '$']
cols_to_clean = ['Installs', 'Price']
for col in cols_to_clean:
    for char in chars_to_remove:
        apps[col] = apps[col].astype(str).str.replace(char, '')
    apps[col] = pd.to_numeric(apps[col])


# In[16]:


num_categories = len(apps['Category'].unique())
print('Number of categories = ', num_categories)
num_apps_in_category = apps['Category'].value_counts().sort_values(ascending=False)
data = [go.Bar(
    x=num_apps_in_category.index,
    y=num_apps_in_category.values,
    marker=dict(color='green') 
)]
layout = go.Layout(
    title='Number of Apps in Each Category',
    xaxis=dict(title='Category'),
    yaxis=dict(title='Number of Apps')
)
fig = go.Figure(data=data, layout=layout)
plotly.offline.iplot(fig)


# In[17]:


avg_app_rating = apps['Rating'].mean()
print('Average app rating = ', avg_app_rating)

data = [go.Histogram(
    x=apps['Rating'],
    marker=dict(color='blue')
)]

layout = {
    'shapes': [{
        'type': 'line',
        'x0': avg_app_rating,
        'y0': 0,
        'x1': avg_app_rating,
        'y1': 1000,
        'line': {'dash': 'dashdot'}
    }]
}

plotly.offline.iplot({'data': data, 'layout': layout})


# In[11]:


get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
sns.set_style("darkgrid")
import warnings
warnings.filterwarnings("ignore")
apps_with_size_and_rating_present = apps[(~apps['Rating'].isnull()) & (~apps['Size'].isnull())]
large_categories = apps_with_size_and_rating_present.groupby(['Category']).filter(lambda x: len(x) >= 250).reset_index()
plt1 = sns.jointplot(x = large_categories['Size'], y = large_categories['Rating'], kind = 'hex')
paid_apps = apps_with_size_and_rating_present[apps_with_size_and_rating_present['Type'] == 'Paid']
plt2 = sns.jointplot(x = paid_apps['Price'], y = paid_apps['Rating'])


# In[12]:


import matplotlib.pyplot as plt
fig, ax = plt.subplots()
fig.set_size_inches(15, 8)
popular_app_cats = apps[apps.Category.isin(['GAME', 'FAMILY', 'PHOTOGRAPHY',
                                            'MEDICAL', 'TOOLS', 'FINANCE',
                                            'LIFESTYLE','BUSINESS'])]
ax = sns.stripplot(x = popular_app_cats['Price'], y = popular_app_cats['Category'], jitter=True, linewidth=1)
ax.set_title('App pricing trend across categories')
apps_above_200 = popular_app_cats[['Category', 'App', 'Price']][popular_app_cats['Price'] > 200]
apps_above_200


# In[13]:


apps_under_100 = popular_app_cats[popular_app_cats['Price'] < 100]
fig, ax = plt.subplots()
fig.set_size_inches(15, 8)
ax = sns.stripplot(x='Price', y='Category', data=apps_under_100,
                   jitter=True, linewidth=1)
ax.set_title('App pricing trend across categories after filtering for junk apps')


# In[18]:


reviews_df = pd.read_csv('user_reviews.csv')
merged_df = pd.merge(apps, reviews_df, on="App", how="inner")
merged_df = merged_df.dropna(subset=['Sentiment', 'Translated_Review'])
sns.set_style('ticks')
fig, ax = plt.subplots()
fig.set_size_inches(11, 8)
ax = sns.boxplot(x='Type', y='Sentiment_Polarity', data=merged_df, palette={'Paid': 'pink', 'Free': 'grey'})
ax.set_title('Sentiment Polarity Distribution')
plt.show()


# In[19]:


trace0 = go.Box(
    y=apps[apps['Type'] == 'Paid']['Installs'],
    name='Paid',
    marker=dict(color='grey')
)
trace1 = go.Box(
    y=apps[apps['Type'] == 'Free']['Installs'],
    name='Free',
    marker=dict(color='pink')
)
layout = go.Layout(
    title="Number of downloads of paid apps vs. free apps",
    yaxis=dict(
        type='log',
        autorange=True
    )
)
data = [trace0, trace1]
plotly.offline.iplot({'data': data, 'layout': layout})


# In[ ]:




