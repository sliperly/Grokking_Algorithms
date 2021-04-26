my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
item = input("Ввести число ")
low = 0
high = len(my_list) - 1
mid = int((low + high) / 2)
guess = my_list[mid]
if guess < int(item):
    low = mid + 1
