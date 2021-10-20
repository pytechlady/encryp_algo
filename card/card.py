# Input requesting for card number
card_number = input("Enter your card number: ")

# convert cardnumber to string
card_string = str(card_number)

# convert the string card number to list
c_n = list(card_string)
# print(c_n)

# Declare empty array avriable for holding the even and odd values
even = []
odd = []

# Loop through the the list cardnumber to determine the odd and even index[value] and push to the empty array variable declared 
for i in range(0, len(c_n)):
    if i % 2:
        even.append(c_n[i])
    else:
        odd.append(c_n[i])
# print(odd)
# print(even)

# Loop through the odd index[value] and multiply by 2 and push to the new empty array variable
num_2 = []
for i in range(0, len(odd)):
    num_2.append(int(odd[i])*2)
# print(num_2)

# join the value, map through as an integer, conver to list and sum all values
x_odd = ''.join(str(e)for e in num_2)
y_odd = map(int, x_odd)
s_odd = list(y_odd)
m_odd = sum(s_odd)
# print(x_odd)
# print(m_odd)
x_even = ''.join(even)
y_even = map(int, x_even)
m_even = sum(y_even)
# print(x_even)
# print(m_even)
odd_even = m_odd + m_even
result = [int(x) for x in str(odd_even)]
#print(result)

# Conditional statement to check card type using the length of card number and the first 2 numbers to determine
#if card is AMEX, MASTERCARD or VISA CARD
if (c_n[0] == '3' and c_n[1] == '4') or (c_n[0] == '3' and c_n[1] == '7'):
    if len(c_n) == 15:
        if result[-1] == 0:
            print("your AMEX card is valid")
        else:
            print("Your card is invalid")
    else:
        print("Card number should be 15 digits")
elif (c_n[0] == '5' and c_n[1] == '1') or (c_n[0] == '5' and c_n[1] == '2') or (c_n[0] == '5' and c_n[1] == '3') or (c_n[0] == '5' and c_n[1] == '4') or (c_n[0] == '5' and c_n[1] == '5'):
    if len(c_n) == 16:
        if result[-1] == 0:
            print("Your MASTERCARD is valid")
        else:
            print("Your MASTERCARD is invalid")
    else:
        print("Card number should be 16 digits")
elif c_n[0] == '4':
    if (len(c_n) == 13) or (len(c_n) == 16):
        if result[-1] == 0:
            print("Your VISA card is valid")
        else:
            print("Your VISA card is invalid")
    else:
        print("Card number should be 13 or 16 digits")
else:
    print("Invalid card. Enter the correct details")
