# 2)შექმენი სია სადაც ჩაამატებ 1-დან 100-მდე ყველა ლუწ რიცხვს.
# საბოლოოდ დაპრინტე ეს სია(გამოიყენე for loop)

lst_nums1 = []
for i in range(1,100):
    if i %2==0:
        lst_nums1.append(i)
print(lst_nums1)
