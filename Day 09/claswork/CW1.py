# classworclasswork 1) შექმენი ფუნქცია,
# რომელსაც არგუმენტად გადაეცემა სია. 
# ფუნქციამ უნდა დაბეჭდოს ეს სია შებრუნებულად
# (არ გამოიყენო slicing-ი).


def revers(numbers):
    i = len(numbers)-1
    while i>=0:
      print(numbers[i])
      i = i-1

revers(12,6,8,91,0)