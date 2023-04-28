# Credit-Card-Checker
![CREDIT-CARD-CHECKER](PASSWORD_WEEK.png)
![CREDIT-CARD-CHECKER](valid-card-number.png)

# Credit Card Checker Program in Python

This program checks the validity of a credit card number using the Luhn algorithm. The Luhn algorithm, also known as the mod 10 algorithm, is a simple checksum formula used to validate various identification numbers, such as credit card numbers, IMEI numbers, and National Provider Identifier numbers.

## Usage

To use this program, simply run the `credit_card_checker.py` file and enter the credit card number you want to check when prompted. The program will then use the Luhn algorithm to validate the credit card number and output whether the card is valid or invalid.

## How it Works

The program first prompts the user to enter a credit card number. It then removes any whitespace characters from the input string and reverses the string for processing.

The program then applies the Luhn algorithm to the credit card number by doubling the value of every second digit starting from the rightmost digit, adding the digits of the resulting numbers together (e.g., 6 becomes 1+2+3), and summing the resulting values along with the sum of the remaining digits. If the total sum is divisible by 10, the credit card number is considered valid.

The program then outputs whether the credit card number is valid or invalid.

## Example

Here is an example of the program in action:

```
**************************
Enter the card number: 4012888888881881
Welcome! Your card is valid.
```

## Credits

This program was created by Mayank Mali.
