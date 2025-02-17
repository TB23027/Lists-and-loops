for number in range(1, 11):
    print(number)

list_1 = ["1", "2", "3", "4", "5"]
for number in list_1:
    print(number)

multiply =  int(input("Enter a number: "))
for i in range(1,11):
    print(f"{multiply} x {i} = {multiply * i}")

for number in range(1, 21):
    if number % 2 == 0:
         print(number)


squarenum = [1,2,3,4,5]
for number in squarenum: 
    print(int(number) * (number))

list_2 = [1,2,3,4,5,6,7,8,9,10]

list_2.reverse()
for reversed in list_2:
    print(reversed)

list_3 = ["Alice", "Bob", "Charlie"]
for name in list_3:
    print(f"Hello, {name}!")

total_sum = 0
for number in range(1,11):
    total_sum += number
    print("The sum of the first 10 Natural numbers is:", total_sum)

list_4 = [10,20,30,40,50]
for number in list_4:
    if number >= 25:
        print(number)

sentence = input("please Enter a sentence: ")
words = sentence.split()
for word in words:
    print(word)

list_5 = [1, 3, 5, 7, 9]
total = 0
for number in list_5:
    total += number
    print(total, end=' ')

a, b = 0, 1
for _ in range(10):
    print(a)
    a, b = b, a + b

grades = [70, 85, 90, 75, 60]
for grade in grades:
    if grade >= 70:
        print(f"Grade {grade}: Pass")
    else:
        print(f"Grade {grade}: Fail")

variable_1 = int(input("Please enter a number: "))
print(f"The factors of {variable_1} are:")
for i in range(1, variable_1 + 1):
    if variable_1 % i == 0:
        print(i)

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    

def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in input_string:
        if char in vowels:
            count += 1
    
    return count
input_string = "Hello, World!"
vowel_count = count_vowels(input_string)
print(f"The number of vowels in the string is: {vowel_count}")


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_first_n_primes(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            print(num, end=' ')
            count += 1
        num += 1

if __name__ == "__main__":
    try:
        n = int(input("Enter a number: "))
        if n > 0:
            print_first_n_primes(n)
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

list_6 = [9, 15, 27, 33, 45]
for number in list_6:
    result = number / 3
    print(result)