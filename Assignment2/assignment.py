def replace_value(values, index, new_value):
    values[index] = new_value
    return None



def find_first(values, target):
    count = 0
    for item in values:
        if item == target:
            return count
        count += 1
    return -1

def summarize(values):
    return (min(values), max(values), sum(values))

days = int(input("Enter the number of days: "))

original = []
for i in range(days):
    minutes = int(input("Enter exercise time in minutes: "))
    original.append(minutes)

updated = original[:]




ind_correct = int(input("Enter the index to correct: "))
nw_time = int(input("Enter the new exercise time: "))

replace_value(updated, ind_correct, nw_time)

target = int(input("Enter the exercise time to search for: "))

first_index = find_first(updated, target)
target_count = updated.count(target)

stat_record = summarize(updated)
minimum, maximum, total = stat_record

sorted_updated = sorted(updated)

print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_updated}")
print(f"Minimum exercise time: {minimum} minutes")
print(f"Maximum exercise time: {maximum} minutes")
print(f"Total exercise time: {total} minutes")

if first_index == -1:
    print("Target not found")
else:
    print(f"First matching index: {first_index}")

print(f"Matching values: {target_count}")