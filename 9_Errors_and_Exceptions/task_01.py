# Exceptions

count = int(input())

array = []

for i in range(count):
    array.append(input().split())

for j in range(len(array)):
    try:
        print(int(array[j][0]) // int(array[j][1]))
    except ZeroDivisionError as ze:
        print("Error Code:", ze)
    except ValueError as ve:
        print("Error Code:", ve)
