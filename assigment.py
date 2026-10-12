


def classify(value):
    if value < 198:
        return "Below range"
    elif value <= 202 and value>=198:
        return "In range"
    else:
        return "Above range"


def calculate_average(total, count):
    average = total / count
    return average

count = int(input("Enter the number of strips: "))

count1 = 0
count2 = 0
count3 = 0
total = 0

for i in range(count):
    value = int(input("Enter the strip length: "))

    total += value

    print(classify(value))

    if classify(value) == "Below range":
        count1 += 1
    elif classify(value) == "In range":
        count2 += 1
    else:
        count3 += 1

print(f"Total length: {total} mm")
print(f"Average length: {calculate_average(total, count)} mm")
print(f"Below range: {count1}")
print(f"In range: {count2}")
print(f"Above range: {count3}")
