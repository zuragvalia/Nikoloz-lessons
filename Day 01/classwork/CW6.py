# 6)მომხარებელს შემოატანინეთ რიცხვი და შეინახეთ ცვლადში, შემდეგ კი 0-დან შემოტანილი რიცხვის ჩათვლით შეამოწმეთ, 
#  თუ ლუწია დაბეჭდეთ რიცხვი is Even, სხვა შემთხვევაში რიცხვი is Odd;(მაგალითად 4, ლუწია ამიტომაც დაბეჭდავთ "4 is Even")

num = int(input("enter number"))
for i in range (0,num+1):
    if i %2==0:
        print("number is even")
    else:
        print("number is odd")