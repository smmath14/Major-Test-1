# Write a program to take an integer N and print the sum of all its even digits and sum of all its odd digits separately.



num = [int(a) for a in str(input())]
even_sum = 0
odd_sum = 0

for i in num:
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i

print(even_sum, odd_sum)
