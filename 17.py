"""
17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.



** This problem could be solved by hand, but should be more fun computationally **
"""



numbers = { 0:'',
            1:'one', 
            2:'two',
            3:'three',
            4:'four',
            5:'five',
            6:'six',
            7:'seven',
            8:'eight',
            9:'nine',
            10:'ten',
            11:'eleven',
            12:'twelve',
            13:'thirteen',
            # 14:'fourteen',
            # 15:'fifteen',
            # 16:'sixteen',
            }
# Fancy teens
for x in xrange(4,10):
    numbers[x+10] = numbers[x]+'teen'
    numbers[15] = 'fifteen'
    numbers[18] = 'eighteen'

tens_dash = {20: 'twenty', 
            30: 'thirty',
            40: 'forty', # US spelling
            50: 'fifty',
            60: 'sixty',
            70: 'seventy',
            80: 'eighty', 
            90: 'ninety',
    }

numbers.update(tens_dash)

number_hundred = 'hundred'

def write_number(n, recursed=0): # Add to numbers?
    hundred_position = (n // 100) % 10
    # one_to_99 = n % 100
    if n > 999: # once 999 is done, can easily implement the others
        raise NotImplementedError
    if n == 0: 
        return '' if recursed else 'zero'
    if n < 0:
        return 'negative ' + write_number(n*-1)
    # Add thousands, etc before hundreds
    if hundred_position: #If there is a digit in the hundred-position
        last_two_digits = write_number(n % 100, recursed=recursed+1)
        if last_two_digits:
            last_two_digits = ' and ' + last_two_digits

        return numbers[hundred_position] + '-' + number_hundred + last_two_digits

    if n in numbers:
        return numbers[n]

    if n > 99:
        raise NotImplementedError # Should never reach here

    tens_number = n//10 * 10
    tens_spelling = tens_dash[tens_number] # 20-90
    single_digit = n % 10
    digit_spelling = numbers[single_digit] # 0-9
    return "%s-%s" % (tens_spelling, digit_spelling)


print write_number(20)
print write_number(21)
print write_number(100)
print write_number(102)