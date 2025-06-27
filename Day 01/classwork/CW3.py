# 3)მომხმარებელს შემოატანინე მთელი რიცხვი. იმ შემთხვევაში, თუ ეს რიცხვი არის ლუწი და ამავდროულად არის 10-ზე მეტი,
# დაბეჭდე True. ყველა სხვა შემთხვევაში False.

num = int(input("enter number"))
if num %2==0 and 10<num:
    print(True)
else:
    print(False)