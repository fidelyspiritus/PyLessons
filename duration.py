duration = int(input("Enter number of sec: "))
time = [0] * 4
numbers = [60, 60, 24, 24]
names = ["days", "hours", "minutes", "sec"]
for i in range(len(numbers)):
    time[i] = duration % numbers[i]
    duration //= numbers[i]
time.reverse()
for i in range(len(time)):
    if time[i] != 0:
        print(time[i], names[i], end=" ")
