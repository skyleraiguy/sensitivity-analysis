import numpy as np
import matplotlib.pyplot as plt

# Define initial variables
purchase_price_30 = 200000  # Purchase price for 30-year-old
purchase_price_40 = 200000  # Purchase price for 40-year-old
mortgage_rate = 0.04  # Mortgage interest rate
income_30 = 50000  # Income at age 30
income_40 = 60000  # Income at age 40
income_growth = 0.03  # Annual income growth
retirement_savings_rate = 0.15  # Percentage of income saved for retirement
investment_return = 0.07  # Annual return on investments
healthcare_costs_60 = 10000  # Annual healthcare costs at age 60
healthcare_costs_70 = 20000  # Annual healthcare costs at age 70
social_situation_score = 7  # Score out of 10 for social situation

# Define function to calculate outcomes
def calculate_outcomes(purchase_price, income, mortgage_rate, income_growth, retirement_savings_rate, investment_return, healthcare_costs_60, healthcare_costs_70, social_situation_score):
    # Calculate equity in home and remaining mortgage at ages 60 and 70
    equity_60 = purchase_price * (1 + mortgage_rate) ** 30
    equity_70 = purchase_price * (1 + mortgage_rate) ** 40
    mortgage_60 = purchase_price - equity_60
    mortgage_70 = purchase_price - equity_70

    # Calculate retirement savings at ages 60 and 70
    retirement_savings_60 = income * retirement_savings_rate * (1 + investment_return) ** 30
    retirement_savings_70 = income * retirement_savings_rate * (1 + investment_return) ** 40

    # Calculate financial stability score (out of 10) based on equity, mortgage, retirement savings, and healthcare costs
    financial_stability_score_60 = (equity_60 - mortgage_60 + retirement_savings_60 - healthcare_costs_60) / 10000
    financial_stability_score_70 = (equity_70 - mortgage_70 + retirement_savings_70 - healthcare_costs_70) / 10000

    # Calculate overall life satisfaction score (out of 10) based on financial stability and social situation
    life_satisfaction_score_60 = (financial_stability_score_60 + social_situation_score) / 2
    life_satisfaction_score_70 = (financial_stability_score_70 + social_situation_score) / 2

    return life_satisfaction_score_60, life_satisfaction_score_70

# Conduct sensitivity analysis by adjusting key variables and observing changes in outcomes
variables = [purchase_price_30, income_30, mortgage_rate, income_growth, retirement_savings_rate, investment_return, healthcare_costs_60, healthcare_costs_70, social_situation_score]
variable_names = ['Purchase Price', 'Income', 'Mortgage Rate', 'Income Growth', 'Retirement Savings Rate', 'Investment Return', 'Healthcare Costs at 60', 'Healthcare Costs at 70', 'Social Situation Score']
outcomes_60 = []
outcomes_70 = []

for i in range(len(variables)):
    # Increase variable by 10%
    variables[i] *= 1.1
    outcome_60, outcome_70 = calculate_outcomes(*variables)
    outcomes_60.append(outcome_60)
    outcomes_70.append(outcome_70)

    # Reset variable
    variables[i] /= 1.1

# Plot outcomes
plt.figure(figsize=(10, 6))
plt.plot(variable_names, outcomes_60, label='Age 60')
plt.plot(variable_names, outcomes_70, label='Age 70')
plt.xlabel('Variable')
plt.ylabel('Life Satisfaction Score')
plt.title('Sensitivity Analysis')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
