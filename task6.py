# Phone bill The cell phone plan includes 50 min.
# of calls and 50 text messages for $15.00 per month. Each additional minute
# costs $0.25 and each additional text message costs $0.15. All phone bills
# include the 911 call center support tax of $0.44, and the total amount,
# including the call center charges is taxed at 5%.
# Write a program that will ask the user for the number of #
# of minutes and sms-messages used per month and display the basic
# billing amount, the amount for additional minutes and messages, the amount of
# charges to 911 call centers, tax, and the total amount due. In this case
# additional calls and messages should be displayed only when they are
# if they've been spent. Make sure that all amounts are displayed in two decimal places.
# decimal places.

minutes = int(input('Enter the number of used minutes: '))
messages = int(input('Enter the number of sent messages: '))

base_tariff_cost = 15.00
tax_911 = 0.44
tax_total = 0.05
cost_per_additional_minute = 0.25
cost_per_additional_message = 0.15

total_cost = base_tariff_cost + tax_911

if minutes > 50:
    additional_minutes = minutes - 50
    additional_minutes_cost = additional_minutes * cost_per_additional_minute
    total_cost += additional_minutes_cost

if messages > 50:
    additional_messages = messages - 50
    additional_messages_cost = additional_messages * cost_per_additional_message
    total_cost += additional_messages_cost

tax_amount = total_cost * tax_total
total_amount = total_cost + tax_amount

print(f'Phone Bill Invoice:')
print(f'Base tariff cost: ${base_tariff_cost:.2f}')
if additional_minutes > 0:
    print(f'Additional minutes cost: ${additional_minutes_cost:.2f}')
if additional_messages > 0:
    print(f'Additional messages cost: ${additional_messages_cost:.2f}')
print(f'911 call center contributions: ${tax_911:.2f}')
print(f'5% Tax amount: ${tax_amount:.2f}')
print(f'Total amount to pay: ${total_amount:.2f}')
