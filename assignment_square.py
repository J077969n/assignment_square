
lst = [4,5,2,9]

def square(lst):
    return lst**2

square_lst = list(map(square,lst))
print(square_lst)