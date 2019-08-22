#

# Question 1:
# Expected output:24
num1 = (7 + 1) * 3
print("num1 evaluates to: ", num1)
# Actual output: 24
# Explanation: Parentheses first (8), then multiplication (24).

# Question 2:
# Expected output:2
num2 = (12 % 5)
print("num2 evaluates to: ", num2)
# Actual output:2
# Explanation: Mod of 12 and 5 has a remainder(2).

# Question 3:
# Expected output:21
num3 = (21 % 49)
print("num3 evaluates to: ", num3)
# Actual output:21
# Explanation: Mod of 21 and 49 has a remainder(21).

# Question 4:
# Expected output: 2
num4 = (5 - 3) + (10 - 5) * (8 % 2)
print("num4 evaluates to: ", num4)
# Actual output:2
# Explanation: Five minus three(2), ten minus five(5), eight mod two(0), 
# five times zero(0), two plus zero(2).

# Question 5:
# Expected output:34
num5 = 6.5 + 5 / 2 * (4 + 7)
print("num5 evaluates to: ", num5)
# Actual output:34.0
# Explanation: Four plus seven(11), five divided by two(2.5), two and a half 
# times eleven(27.5), twenty-seven and a half plus six and a half(34).

# Question 6:
# Expected output:5
num6 = 9 / 3 + 18 - 4 * 4
print("num6 evaluates to: ", num6)
# Actual output:5.0
# Explanation: Nine divided by three(3), four times four(16), three plus
# eighteen(21), twenty-one minus sixteen(5).

# Question 7:
# Expected output:22
num7 = 8 % 3 + 5 * 4
print("num7 evaluates to: ", num7)
# Actual output:22
# Explanation: Eight mod three(2), five times four(20), two plus twenty(22).

# Question 8:
# Expected output:79.9
num8 = 81.3 / 2.1 + ((51.5 % 65.2) * 2 / 2.5)
print("num8 evaluates to: ", num8)
# Actual output:79.9
# Explanation: Fifty-one and a half mod sixty-five and a fifth(51.5), fifty-one
# and a half times two(103), one hundred three divided by two and a half(41.2),
# eighty one and three tenths divided by two and a tenth(38.7), thirty eight
# and seven tenths plus forty-one and two tenths(79.9).
 
# Question 9:
num9 = 100 - ((8 * 8) + 1) / 0.5 
print("num9 evaluates to:", num9 , "and should be", -30)

# Question 10:
num10 = (84 / (10 + 11) - 4) * 4
print("num10 evaluates to:", num10 , "and should be", 0)
