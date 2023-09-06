# num_rows = int(input("Please enter the number of rows: "))
# for i in range(num_rows,0,-1):
#     for j in range(0, num_rows-i):
#         print(end=" ")
#     for j in range(0,i):
#         print("*", end=" ")
#     print()

# Bonus Task
# num_rows = int(input("Enter the number of rows: "))
# k = 0
# for i in range(1, num_rows + 1):
#     for j in range(1, (num_rows - i) + 1):
#         print(end=" ")
#     while k != (2 * i - 1):
#         print("*", end="")
#         k = k + 1
#     k = 0
#     print()
# k = 2
# m = 1
# for i in range(1, num_rows):
#     for j in range(1, k):
#         print(end=" ")
#     k = k + 1
#     while m <= (2 * (num_rows - i) - 1):
#         print("*", end="")
#         m = m + 1
#     m = 1
#     print()

list = [1,2,3,4,5,6,7,8,9,10]

# print(list[::4])

nested_lists1 = [[1,2,3],[4,5,6],[7,8,9]]

# print(nested_lits[::2])

nested_list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# list += nested_lists1[2]
# list += nested_lists1[0]

list = nested_list2[2] + nested_lists1[0]

tuple1 = (1,2,3)
tuple2 = (4,5,6)

tuple1 += tuple2
dict = tuple1._replace()

print(dict)

