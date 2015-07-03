def is_palindrome(n):
  return str(n) == str(n)[::-1]

total = 0
for i in range(1000000):
  if not is_palindrome(i):
    continue
  if is_palindrome(bin(i)[2:]):
    total += i

print total
