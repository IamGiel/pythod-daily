nums = [i for i in range(1,1001)]
string = "Practice Problems to Drill List Comprehension in Your Head."
# print(nums)

# Find all of the numbers from 1–1000 that are divisible by 8
divisible_by_eight = [i for i in range(1,1001) if i%8==0]
print(f"divisible by 8: {divisible_by_eight}")

print(f"\n\ndivider ========================================================== divider\n\n")    

# Find all of the numbers from 1–1000 that have a 6 in them
have_sixes = [i for i in range(1,1001) if str(6) in str(i)]
print(f"numbers 1-1000 with 6 in them: {have_sixes}")

print(f"\n\ndivider ========================================================== divider\n\n") 
# Count the number of spaces in a string (use string above)
num_of_spaces = string.count(' ')
q3_answer = len([char for char in string if char == " "])

print(f"num of spaces in a string: {q3_answer}")

print(f"\n\ndivider ========================================================== divider\n\n") 
# Remove all vowels in a string (use string above)
vowels=['A','E','I','O','U','a','e','i','o','u']
q4_answer = "".join([char for char in string if char not in vowels])
print(f"string with no vowels: {q4_answer}")

print(f"\n\ndivider ========================================================== divider\n\n") 
# Find all of the words in a string that are less than 5 letters (use string above)
words = string.replace(".", "").split()
q5_answer = " ".join([word for word in words if len(word) < 5])
print(f"string with less than 5 chars: {q5_answer}")

print(f"\n\ndivider ========================================================== divider\n\n") 
# Use a dictionary comprehension to count the length of each word in a sentence
q6_answer = {word: len(word) for word in words}
print(f"Use a dictionary: {q6_answer}")

print(f"\n\ndivider ========================================================== divider\n\n") 
# Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit besides 1 (2–9)
q7_answer = [num for num in nums if True in [True for divisor in range(2,10) if num % divisor == 0]]
print(f"Use a nested list comprehension: {q7_answer}")