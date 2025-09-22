# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 23:23:19 2025
@author: Shwet

Project: Housing Price Analysis
Objective: Perform data wrangling, visualization, and derive insights from Housing dataset
"""

# ----------------------------
# 1. Import Libraries
# ----------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set visualization style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10,6)

# ----------------------------
# 2. Load Dataset
# ----------------------------
df = pd.read_csv("C:/Users/Shwet/Downloads/archive/Housing.csv")

# Basic checks
print("\nDataset Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nData Types:\n", df.dtypes)

# ----------------------------
# 3. Data Exploration
# ----------------------------
print("\nSample Records:\n", df.head())
print("\nNull Values:\n", df.isnull().sum())
print("\nDuplicate Rows:", df.duplicated().sum())
print("\nSummary Statistics:\n", df.describe())

# ----------------------------
# 4. Data Visualization
# ----------------------------

# Price Distribution
plt.hist(df['price']/1000000, bins=50, color='steelblue', edgecolor='black')
plt.title('Price Distribution')
plt.xlabel('Price (in Millions)')
plt.ylabel('Frequency')
plt.show()

# Area Distribution
sns.histplot(df['area']/1000, bins=50, kde=True, color="green")
plt.title("Area Distribution")
plt.xlabel("Area (in 1000 sq ft)")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot - Price vs Area
sns.scatterplot(data=df, x='area', y='price', hue='bedrooms', palette="viridis", alpha=0.7)
plt.title("Price vs Area (colored by Bedrooms)")
plt.xlabel("Area")
plt.ylabel("Price")
plt.show()

# Regression Line - Price vs Area
sns.regplot(x='area', y='price', data=df, scatter_kws={'alpha':0.4}, line_kws={'color':'red'})
plt.title("Area vs Price with Regression Line")
plt.show()

# Boxplot - Price vs Bedrooms
sns.boxplot(x='bedrooms', y='price', data=df, palette="Set2")
plt.title("Price Distribution by Number of Bedrooms")
plt.xlabel("Bedrooms")
plt.ylabel("Price")
plt.show()

# Boxplot - Price vs Furnishing Status
sns.boxplot(x='furnishingstatus', y='price', data=df, palette="Set3")
plt.title("Price vs Furnishing Status")
plt.show()

# Correlation Heatmap (All Numerical Columns)
corr = df.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

# Pairplot (Optional - Relationship between features)
sns.pairplot(df[['price', 'area', 'bedrooms', 'bathrooms']], diag_kind="kde")
plt.suptitle("Pairwise Relationships", y=1.02)
plt.show()

# Pie Chart - Furnishing Status
df['furnishingstatus'].value_counts().plot.pie(autopct='%1.1f%%', colors=['#66b3ff','#99ff99','#ff9999'])
plt.title("Furnishing Status Distribution")
plt.ylabel("")
plt.show()

# ----------------------------
# 5. Key Insights / Inference
# ----------------------------
"""
1. House prices are right-skewed → most houses are in lower price ranges.
2. Area and Price have a strong positive correlation (larger area → higher price).
3. Bedrooms and bathrooms also influence price but less strongly than area.
4. Furnishing status has visible impact on price (furnished houses usually cost more).
5. Correlation heatmap shows: Area is the strongest predictor of price.
6. Outliers exist in price (luxury houses), visible in boxplots.
"""
'''Analysis shows that house prices are majorly influenced by area, 
followed by bedrooms, bathrooms, and furnishing status. Most houses
 are priced in the affordable range, while a small portion belongs to 
 luxury housing. Furnished properties command a premium price and area is 
 the strongest factor driving cost'''

































