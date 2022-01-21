# You are given a list li[] of N integers. The task is to find the smallest positive natural number missing from the list.


n = int(input())
numbers = [int(x) for x in input().split()]
numbers.sort()
result = 1

for n in numbers:
    if n != result:
        break

    result += 1

print(result)