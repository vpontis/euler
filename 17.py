int_to_word = {
  0: '',
  1: 'one',
  2: 'two',
  3: 'three',
  4: 'four',
  5: 'five',
  6: 'six',
  7: 'seven',
  8: 'eight',
  9: 'nine',
  10: 'ten',
  11: 'eleven',
  12: 'twelve',
  13: 'thirteen',
  14: 'fourteen',
  15: 'fifteen',
  16: 'sixteen',
  17: 'seventeen',
  18: 'eighteen',
  19: 'nineteen',
  20: 'twenty',
  30: 'thirty',
  40: 'forty',
  50: 'fifty',
  60: 'sixty',
  70: 'seventy',
  80: 'eighty',
  90: 'ninety',
  1000: 'onethousand',
}

for i in range(1000):
  if i not in int_to_word.keys():
    ones = i % 10
    tens = i / 10 % 10
    hundreds = i / 100 % 10

    if i % 100 <= 20:
      word = int_to_word[i%100]
    else:
      word = int_to_word[tens*10] + int_to_word[ones]

    if hundreds > 0:
      word = int_to_word[hundreds] + 'hundredand' + word
      if tens == 0 and ones == 0:
        word = word[:-3]
    int_to_word[i] = word

print int_to_word

total = 0
for i in range(1, 1000 + 1):
  total += len(int_to_word[i])

print total
