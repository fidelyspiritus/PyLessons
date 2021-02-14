percent = ['процентов', 'процент', 'процента']
numbers = [[0, 5, 6, 7, 8, 9, 11, 12, 13, 14], [1], [2, 3, 4] ]
num = int(input("Enter a number: "))
for i, number in enumerate(numbers):
    if num%100 in number:
        print(f"{num} {percent[i]}")
        break
    elif num%10 in number: print(f"{num} {percent[i]}")
