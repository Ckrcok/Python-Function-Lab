# Part 1:

# task 1
# def pokemon_contains(incoming_letter):
# 	if incoming_letter in "pokemon":
# 		return True
# 	else:
# 		return False
#
# result1 = pokemon_contains("k")
# print(result1)
#
# result1 = pokemon_contains("o")
# print(result1)

# task 2
# a = 1
# b = 3
#
# def sum_two(a,b):
# 	answer = a + b
# 	return answer
#
# result3 = sum_two(a,b) # a and b were not defined
# print(result3)
# result4 = sum_two(5,6)
# print(result4)

# task 3

# def multiply(num1 , num2):
# 	answer = num1*num2 # a and b were not an argument in the function but num1 and num2 were
# 	return answer  #missing return answer
# result5 = multiply( 10 , 10 )
# print(result5)
# result6 = multiply( 5 , 6 )
# print(result6)

# task 4

# def multiplication(a,b):
# 	my_answer = a*b
# 	print("Calculating...")
# 	return my_answer
#
# print("Let's Multiply stuff...")
# answer = multiplication(5,6) # multiply wasn't defined as a function name but multiplication is
# answer = str(answer)
# print("The answer is..." + answer)

# task 5

# def subtract (a , b):
# 	result = b - a
# 	return result
#
# result1 = subtract(2, 8)
# print (result1)
# result2 = subtract(1, -9)
# print (result2)

# task 6

# def greater_than_5(a):
# 	if a > 5:
# 		return True
# 	elif a < 5:
# 		return False
#
# Big = greater_than_5(6)
# print(Big)
# Small = greater_than_5(1)
# print(Small)

# Part 2

# Task 1

# def sum_to(n):
#
# 	best = 0
# 	for x in range(n+1):
#
# 		best += x
#
#
# 	return best
# sum1 = sum_to(6)
# print (sum1)
# sum2 = sum_to(10)
# print (sum2)


# Task 2
#
# def largest(a):
# 		a.sort()
# 		print("Largest element is:", a[-1])
#
#
# largest([1, 2, 3, 4, 0])  # returns 4
# largest([10, 4, 2, 231, 91, 54])  # returns 231

# Task 3

# def occurances(a, b):
#
# 	return a.count(b)
#
#
# print(occurances('fleep floop', 'e'))   # returns 2
# print(occurances('fleep floop', 'p'))   # returns 2
# print(occurances('fleep floop', 'ee'))  # returns 1
# print(occurances('fleep floop', 'fe'))  # returns 0

def product(*arg):
	result = 0
	for idx,num in enumerate(arg):
	        result = num if idx == 0 else result * num
	return result

print(product(-1, 4)) # returns -4
print(product(2, 5, 5)) # returns 50
print(product(4, 0.5, 5)) # returns 10.0
