from tabulate import tabulate
from datetime import datetime
from dateutil.relativedelta import relativedelta


def generate_annuity_schedule(schedule_start_date, loan_amount, period_in_months, year_interest_rate):
    n = 0
    loan_schedule = []
    # Add initial row, with date today
    loan_schedule.append([n, schedule_start_date, 0, 0, 0, loan_amount])

    # Calculate monthly interest
    monthly_interest_rate = year_interest_rate / 1200

    # Calculate monthly payment
    payment = round(
        (monthly_interest_rate * loan_amount) / (1.0 - (1.0 / pow((1.0 + monthly_interest_rate), period_in_months))), 2)

    while n < period_in_months:
        n += 1
        date_after_month = datetime.today() + relativedelta(months=n)
        interest_payment = round(monthly_interest_rate * loan_amount, 2)
        principal_payment = round(payment - interest_payment, 2)
        loan_amount = round(loan_amount - principal_payment, 2)
        schedule_row = [n, date_after_month.strftime('%Y-%m-%d'), principal_payment, interest_payment, payment,
                        loan_amount]
        loan_schedule.append(schedule_row)

    return loan_schedule


if __name__ == "__main__":
    loan_schedule = generate_annuity_schedule(schedule_start_date='2024-04-04', loan_amount=1000, period_in_months=12, year_interest_rate=5.477)
    tabular_schedule = (tabulate(loan_schedule, headers=["#", "Payment date", "Principal", "Interest", "Payment", "Residual"], tablefmt="grid"))
    print(tabular_schedule)
    # Write it to file
    try:
        # https://www.geeksforgeeks.org/reading-writing-text-files-python/
        with open('loan_schedule.txt', 'w') as f:
            f.write(f"{tabular_schedule}\n\n")
            f.close()
    except:
        print("An exception occurred")