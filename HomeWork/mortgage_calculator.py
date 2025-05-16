print("MORTGAGE CALCULATOR")

"""
Pseudo code
- Collect the principal from user using float which i initialized as amount.
- Collect the interestRate from user using float.
- Collect the duration from user using float
- For me to get monthly rate,i will divide the interestRate by percentage because percentage is per hundred and number of month which is 12 which will give 1200.
- And my number of months for the duration, i multiplied it by number of months in a year.
- Then for me to now get the monthly payment that i will use the amount to multiply the Monthly interest rate according to the formula given.
- And will get the monthly payment.
"""

amount = (float)(input("Enter the principal amount: "))

interestRate = (float)(input("Enter the annual interest rate: "))
		
duration =(float)(input("Enter the duration in years: "))
	

MonthlyinterestRate = interestRate / 1200;

numberOfMonth = duration * 12;
 
value1 = amount * MonthlyinterestRate * (1 + MonthlyinterestRate) ** numberOfMonth / ((1 + MonthlyinterestRate) ** numberOfMonth - 1)




print("Your monthly payment is: ", value1);


