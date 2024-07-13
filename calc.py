import numpy as np

# Define the parameters for scenario 1
price_now = 725000
down_payment_now = 0.20 * price_now
loan_amount_now = price_now - down_payment_now
interest_rate_now = 0.065
loan_term = 30
months = loan_term * 12
monthly_interest_rate_now = interest_rate_now / 12

# Define the parameters for scenario 2
price_future = price_now * 1.05
down_payment_future = 150000 * 1.08
loan_amount_future = price_future - down_payment_future
interest_rate_future = 0.055
monthly_interest_rate_future = interest_rate_future / 12

# Define function to calculate monthly mortgage payment
def monthly_payment(principal, monthly_rate, n_months):
    return principal * (monthly_rate * (1 + monthly_rate) ** n_months) / ((1 + monthly_rate) ** n_months - 1)

# Define function to calculate remaining principal after n months
def remaining_principal(principal, monthly_rate, n_months_paid, total_months):
    p = principal
    for _ in range(n_months_paid):
        p -= monthly_payment(principal, monthly_rate, total_months) - (p * monthly_rate)
    return p

# Monthly payment for scenario 1 before refinancing
monthly_payment_now = monthly_payment(loan_amount_now, monthly_interest_rate_now, months)

# Remaining principal after 12 months
remaining_principal_1year = remaining_principal(loan_amount_now, monthly_interest_rate_now, 12, months)

# Monthly payment for scenario 1 after refinancing
monthly_interest_rate_refinance = 0.055 / 12
new_months = (loan_term - 1) * 12
monthly_payment_refinance = monthly_payment(remaining_principal_1year, monthly_interest_rate_refinance, new_months)

# Monthly payment for scenario 2
monthly_payment_future = monthly_payment(loan_amount_future, monthly_interest_rate_future, months)

# Closing costs and taxes
closing_costs_now = 0.03 * loan_amount_now
closing_costs_future = 0.03 * loan_amount_future
capital_gains_tax_rate = 0.15  # Assume long-term capital gains rate
investment_return = 150000 * 0.08
capital_gains_tax = investment_return * capital_gains_tax_rate

# Total cost calculation
total_cost_now = (monthly_payment_now * 12) + (monthly_payment_refinance * (months - 12)) + closing_costs_now + capital_gains_tax
total_cost_future = (monthly_payment_future * months) + closing_costs_future + capital_gains_tax

total_cost_now, total_cost_future, monthly_payment_now, monthly_payment_refinance, monthly_payment_future

print(total_cost_future)