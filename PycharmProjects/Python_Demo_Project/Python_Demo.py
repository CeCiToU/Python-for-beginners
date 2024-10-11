# Pesho wants to know how much his Bitcoin investment has increased in value. He knows the current value of Bitcoin in euros and its old value in euros. Additionally, he has some Bitcoin and is aware of the conversion rate between Bitcoin and Bulgarian lev. He would like to calculate the total price of his Bitcoin in Bulgarian lev and then convert it to euros.
#
# Write a program that:
#
#     Takes the new value of Bitcoin in euros.
#     Takes the old value of Bitcoin in euros.
#     Calculates the total price of Bitcoin in Bulgarian lev using the conversion rate of 1 Bitcoin = 113057 BGN.
#     Converts the value in lev to euros using the rate of 1 Euro = 1.96 BGN.
#     Prints:
#         The current price of Bitcoin in euros (formatted to two decimal places).
#         The percentage increase in Bitcoin value between the new and old values.
#
# Input:
#
#     New value of Bitcoin in euros (real number).
#     Old value of Bitcoin in euros (real number).
#
# Output:
#
#     Price of Bitcoin in euros (formatted to two decimal places).
#     Percentage increase in the value of Bitcoin (formatted to two decimal places).

new_value_of_bitcoin = float(input("New value of bitcoin in euro: "))
old_value_of_bitcoin = float(input("Old value of bitcoin in euro: "))

bitcoin_price_in_leva = 113057

bitcoins_in_leva = new_value_of_bitcoin * bitcoin_price_in_leva


price_in_euro = bitcoins_in_leva / 1.96

print(f"Price of bitcoin (10-10-2024): {'{:.2f}'.format(new_value_of_bitcoin)} euro")
print(f"Increase: {'{:.2f}'.format(((new_value_of_bitcoin / old_value_of_bitcoin) - 1)* 100)}%")
