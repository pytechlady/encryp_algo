# Core Python

Below are tasks that you are expected to complete and provide solutions to. Happy hacking, cheers...👍👍👍

## Validate Credit or Debit Card

A credit (or debit) card, of course, is a plastic card with which you can pay for goods and services. Printed on that card is a number that's also stored in a database somewhere so that when your card is used to buy something, the creditor knows whom to the bill.

### For Context

Your task is to take a credit card number and determine whether that number is an American Express Credit Card number or Master Card number or Visa or something else.

Luckily for us, credit card numbers actually have some structure or patterns to them.

- American Express Card numbers always have 15 digits and start with 34 or 37;
- Most Master Card numbers have 16 digits and start with 51, 52, 53, 54, or 55;
- Visa Card numbers have 13 or 16 digits and start with 4.

Also for a credit card number to be considered valid, it has to satisfies the `checksum` or `Luhn Algorithm`: a mathematical algorithm invented by Hans Peter Luhn of IBM which is mostly used in generating credit card numbers.

How does this algorithm work?

The algorithm takes the following steps:

1. Multiply every other digit by 2, starting with the second-to-last digit
2. Add those product’s digits together
3. Add the sum to the sum of the digits that weren’t multiplied by 2
4. If the total’s last digit is 0, the number is valid else it invalid

That’s kind of confusing, so let’s try an example with David’s Visa: 4003600000000014

#### Step 1: Multiply every other digit by 2, starting with the second-to-last digit

For the sake of discussion, let‘s put every other digit in a quote, starting with the number’s second-to-last digit. This will give us

`4`  0  `0`  3  `6`   0   `0`   0   `0`   0   `0`  0   `0`    0   `1`    4

Okay, let’s multiply each of the quoted digits by 2:

1•2 + 0•2 + 0•2 + 0•2 + 0•2 + 6•2 + 0•2 + 4•2

That gives us:

2 + 0 + 0 + 0 + 0 + 12 + 0 + 8

#### Step 2: Add those product’s digits together

2 + 0 + 0 + 0 + 0 + 1 + 2 + 0 + 8 = 13

NB: We only add the product digit and not the products themselves together

#### Step 3: Add the sum to the sum of the digits that weren’t multiplied by 2

Sum of numbers that weren’t multiplied by 2 are:

4 + 0 + 0 + 0 + 0 + 0 + 3 + 0 = 7

Then Let’s add the sum in step2 to it

7 + 13 = 20

#### Step 4: If the total’s last digit is 0, the number is valid else it invalid

Yes, the last digit in the sum was 0, so David’s card is valid!

So, validating credit card numbers isn't hard, but it does get a bit tedious by hand. Let's write a program.

### Program Expectation

- Prompt the user for input: a credit card number
- Calculate the checksum: to figure out if it could be a valid credit card or not
- Check for card length and starting digits
- Print AMEX for American Express Card, MASTERCARD for mastercard, VISA for visa card, or INVALID: if it doesn’t satisfy any of the 3 types of cards
- Test your program on different credit card

## Cryptography

Cryptography is a method of protecting information and communications through the use of cyphers or codes so that only those for whom the information is intended can read and process it. This involves both encryption and decryption of information. [Read more →](https://searchsecurity.techtarget.com/definition/cryptography)

### For Context

You are to write a simple command-line program that encrypts and decrypts English alphabet letters using an integer as an encryption/decryption key.

Your program should be able to:

- Encrypt → convert information (plaintext) into a secret code (ciphertext)
- Decrypt → convert secret code (ciphertext) into information (plaintext)
- Accept encryption or decryption key
- Encrypt based on the encryption key provided by shifting each character forward on the English alphabet using encryption key e.g
  - encrypt “abcd” with the encryption key of  “1” should return “bcde”  
  - encrypt “abcd” with the encryption key of “5”  should return “fghi”
- Decrypt based on the decryption key provided by shifting each character backwards on the English alphabet using the decryption key e.g
  - decrypt “fghi” with the decryption key of “5” should return “abcd”
  - decrypt  “abcd” with the decryption key of “1” should return “zabc”

### Program Expectations

Your program is expected to behave in the following ways

- Prompt user either she wants to encode (encrypt) or decode (decrypt)
- Prompt user to insert the plaintext to encode or ciphertext to decode
- Prompt user to insert the encryption/decryption key which must be an integer
- The program encodes the plaintext or decodes the ciphertext as the case may be
- Show the user the encoded text or decoded text
- Prompt the user if she wants to go again
  - If the user response was `No`:
    - The program should stop and thank the user for using the cryptography service
  - If the user responds with `Yes`:
    - The program prompts the user either she wants to encode(encrypt) or decode (decrypt)
- The cycle continues...

### Constraints

The followings are the constraints that your program should adhere to:

- Your program should only encrypt or decrypt lowercase alphabet characters. Other characters should remain the same
- If no encryption/decryption key is provided default to zero
- Make sure all necessary exception is caught

## Dict Comprehension

Write a function named `dict_comp` that takes in two integer values `stop` and `step` as arguments and returns a dictionary generated using python comprehensions, which will have string keys in the format ` "items-#" ` and values of type `list`, where each list is of length `step` and contains only integers. 

The integers within the list values will be sequentially generated, such that integers in a second list is a continuation of those in the first list and so on for others until we get to `stop` 

```python
# Example output dictionary given that : stop = 10 and step = 4 

{
   "items-1": [ 1, 2, 3, 4 ],
   "items-2": [ 5, 6, 7, 8 ], 
}

```

Notice in the example above, the first list starts from 1 and not 0 and that the remaining integers `9 & 10` were discarded since they are not up to 4 integers to make up another entry in the dictionary.
