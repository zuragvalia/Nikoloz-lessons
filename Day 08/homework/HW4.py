# 4)შექმენი ფუნქცია greetAll, რომელიც იღებს სახელების სიას (მასივს) 
# და for ციკლის გამოყენებით თითოეულს აბრუნებს მისალმებას:
# “გამარჯობა, [სახელი]!.


def greetall_lst(lst):
    for i in lst:
        print(f"hello, {i}")
print(greetall_lst(["nika","zura","elene"]))
