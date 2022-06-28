# calculate average temperature


numbDays = int(input("How Many Days Temperature?"))

total = 0
for i in range(0, numbDays):
    nextDay = int(input("Day" + str(i+1) + "'s hifh temp:"))
    total += nextDay

avg = round(total/numbDays, 2)
print("\nAverage = " + str(avg))
