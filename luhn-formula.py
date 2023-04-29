sum_odd_number = 0
sum_even_number = 0
total = 0

print("**************************")
print("Enter the card number:")
card_number = input()
card_number_r = card_number[::-1]
for i in card_number[::2]:
    sum_odd_number += int(i)

for i in card_number[1::2]:
    x = int(i) * 2
    if x >= 10:
        sum_even_number += (1 + (x % 10))
    else:
        sum_even_number += x
total = sum_even_number + sum_odd_number

if total % 10 == 0:
    print("Welcome! Your card is valid.")
else:
    print("Sorry, your card is invalid.")
