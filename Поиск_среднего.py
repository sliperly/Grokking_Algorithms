
item = input ("Ввести число ")
low = 0
high = len (list) - 1
mid = (low + high) / 2
guess = list [mid]
if guess < item:
    low = mid + 1