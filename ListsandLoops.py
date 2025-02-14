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



