
import re

input = open('input.txt', 'r')
Lines = input.readlines()
 
 # Mapping of word numbers to digits
word_to_digit = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

#create output file
output = open('output.txt', 'w')
count = 0
for line in Lines:
    numbers = re.findall(r'(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine)', line)
    numbers = [word_to_digit.get(num, num) for num in numbers]

    first_number = numbers[0]
    last_number = numbers[-1]
    # concat string
    string = first_number + last_number
    # convert to int
    number = int(string)
    # print number and corresponding line on the same line to an output file
    output.write(str(number) + ' ' + line)
    # add to count
    count += number

output.write('\n')
output.write(str(count))

input.close()

output.close()