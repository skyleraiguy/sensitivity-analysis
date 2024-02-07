import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# Homeownership Details
purchase_price = 200000
mortgage_rate = 0.04
mortgage_term = 30

# Financial Variables
income = 50000
income_growth = 0.03
retirement_savings = 0
investment_return = 0.07
inflation = 0.02

# Health Variables
healthcare_costs = 5000
healthcare_growth = 0.05

# Social Variables
community_engagement = 0.7

# Life Satisfaction
life_satisfaction = 0.8


# Create a DataFrame to store the data
df = pd.DataFrame(index=range(30, 71))
df['Age'] = df.index


# Calculate home equity, remaining mortgage, retirement savings, and healthcare costs for each year
for age in df['Age']:
    df.loc[age, 'Home Equity'] = min((age - 30) / mortgage_term, 1) * purchase_price
    df.loc[age, 'Remaining Mortgage'] = max(0, purchase_price - df.loc[age, 'Home Equity'])
    df.loc[age, 'Retirement Savings'] = retirement_savings * (1 + investment_return) ** (age - 30)
    df.loc[age, 'Healthcare Costs'] = healthcare_costs * (1 + healthcare_growth) ** (age - 30)


# Calculate financial stability and overall life satisfaction scores
df['Financial Stability'] = df['Retirement Savings'] - df['Remaining Mortgage'] - df['Healthcare Costs']
df['Life Satisfaction'] = life_satisfaction * (1 + community_engagement)

# Adjust variables and recalculate
purchase_price = 250000
mortgage_rate = 0.05
income = 60000
healthcare_costs = 6000
community_engagement = 0.8
life_satisfaction = 0.9

# Recalculate the model
# ...

# Plot financial stability and life satisfaction over time
plt.figure(figsize=(10, 5))
plt.plot(df['Age'], df['Financial Stability'], label='Financial Stability')
plt.plot(df['Age'], df['Life Satisfaction'], label='Life Satisfaction')
plt.xlabel('Age')
plt.ylabel('Score')
plt.legend()
plt.show()
