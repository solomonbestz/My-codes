monthly_expenses = [['January', 2200], ['February', 2350], ['March', 2600], ['April', 2130], ['May', 2190]]


feb_dol_spent = monthly_expenses[1][1] - monthly_expenses[0][1]
print(f'The extra dollar spent Febrauary Compared to January is {feb_dol_spent}')

total_expenses = 0
for n in range(0, len(monthly_expenses)-2):
    total_expenses = total_expenses + monthly_expenses[n][1]

print(f"The total expenses i  first quarter is {total_expenses}")

for n in range(len(monthly_expenses)):
    if monthly_expenses[n][1] == 2000:
        print(f'I spent 2000 in {monthly_expenses[n][0]}')
    else:
        pass

add_item = input("Enter Month and Price: ")
word = add_item.split()

monthly_expenses.append(word)

print(monthly_expenses)

for n in range(len(monthly_expenses)):
    if 'April'.lower == monthly_expenses[n][0].lower:
        monthly_expenses[n][1] = 2005

print(f'New monthly Expenses is {monthly_expenses}')

