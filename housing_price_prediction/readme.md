# Housing Price Prediction

## Project Overview
This project analyzes a housing dataset to understand the factors affecting house prices. The analysis includes data cleaning, exploration, visualization, and deriving key insights to support better decision-making.

## Objective
- Perform data wrangling and cleaning
- Explore relationships between features like area, bedrooms, bathrooms, and furnishing status
- Visualize distributions and correlations
- Identify key factors influencing house prices

## Dataset
- The dataset `Housing.csv` contains information about houses, including:
  - `price` : House price
  - `area` : Area of the house (in sq ft)
  - `bedrooms` : Number of bedrooms
  - `bathrooms` : Number of bathrooms
  - `furnishingstatus` : Furnishing status of the house (furnished, semi-furnished, unfurnished)

> **Note:** Place the dataset inside the `data/` folder.

## Libraries Used
- Python 
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Visualizations
The analysis includes the following visualizations:
1. Price Distribution
2. Area Distribution
3. Scatter plot of Price vs Area (colored by Bedrooms)
4. Regression line for Price vs Area
5. Boxplots for Price vs Bedrooms and Furnishing Status
6. Correlation Heatmap
7. Pairplot of numerical features
8. Pie chart of Furnishing Status

## Key Insights
1. House prices are right-skewed → most houses are in lower price ranges.
2. Area and Price have a strong positive correlation (larger area → higher price).
3. Bedrooms and bathrooms moderately influence price.
4. Furnishing status impacts price (furnished houses usually cost more).
5. Outliers exist in price (luxury houses), visible in boxplots.

## Folder Structure

