# 1)homework:მომხარებელს შემოატანინე ორი რიცხვი, აიყვანე ისინი მე-3 ხარისხში და გაიგე მათი ჯამი,
# თუ ჯამი ლუწია დაპრინტე "Result is Even", სხვა შემთვევაში "Result is Odd"
# აღწერეთ თითოეული მოქმედება კომენტარები.


#i ** 3

num = int(input("enter number first: "))
num1 = int(input("enter number second: "))
kub1 = num ** 3
kub2 = num1 ** 3
sum = kub1 + kub2
if sum %2==0:
    print("result is even")
else:
    print("number is odd")