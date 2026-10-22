# 1
def even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"
print(even_or_odd)

# 2
def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    return c
print(largest_of_three(4,9,2))
# 3
def sum_list(nums):
    total = 0
    for n in nums:
        total += n
    return total
print(sum_list([1,2,3]))

# 4
def only_evens(nums):
    result = []
    for n in nums:
        if n % 2 == 0:
            result.append(n)
    return result
print(only_evens([1,2,3,4]))

# 5
def string_length(s):
    count = 0
    for ch in s:
        count += 1
    return count
print(string_length("hello"))

# 6
def to_upper(s):
    return s.upper()
print(to_upper("hello"))

# 7
def check_sign(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    return "Zero"
print(check_sign(-5))

# 8
def multiple_of_3_and_5(n):
    return n % 3 == 0 and n % 5 == 0
print(multiple_of_3_and_5(15))

# 9
def max_value(nums):
    biggest = nums[0]
    for n in nums:
        if n > biggest:
            biggest = n
    return biggest
print(max_value([3,8,2]))

# 10
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    return "Fail"
print(get_grade(80))

# 11
def discounted_price(price):
    return price - (price * 10 / 100)
print(discounted_price(200))

# 12
def count_even_odd(nums):
    even = 0
    odd = 0
    for n in nums:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd
print(count_even_odd([1,2,3,4,5]))


# 13
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32
print(celsius_to_fahrenheit(100))    