# 2)homework: while ციკლის გამოყენებით დაპრინტე 1-დან 50-მდე ყველა 4-ის ჯერადი რიცხვის კუბი


num = 1  
while num <= 50:
    if num %4==0:
        print(num ** 3)
    num += 1