name = input().strip().title()
marks = list(map(int,input().split()))

def analyze(*marks, pass_marks = 40):
    total = sum(marks)
    average = round(total / len(marks),2 )
    highest = max(marks)
    lowest = min(marks)

    failed_count = 0

    for mark in marks:
        if mark < pass_marks:
            failed_count += 1

    return total, average,highest, lowest, failed_count

total, average , highest, lowest, failed_count = analyze(*marks)

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

print("===== REPORT CARD =====")
print(f"Student : {name}")

for index, mark in enumerate(marks, start = 1):
    if mark >= 40:
        status = "pass"
    else:
        status = "fail"

    print(f"Subject {index}: {mark} - {status}")

top_3 = sorted(marks, reverse = True) [:3]

print(f"Total : {total}")
print(f"Average : {average:.2f}")
print(f"Highest : {highest}")
print(f"Lowest  : {lowest}")
print(f"Failed  : {failed_count}")
print(f"Top 3   : {top_3}")
print(f"Grade   : {grade}")