# 3)შექმენი ორი ცარიელი სია, for loop-ის გამოყენებით
# მომხარებელს 5-ჯერ შემოატანინე ნებისმიერი სიტყვა.
# თუ შემოტანილი სიტყვის სიგრძე არ აღემატება 5-ს ჩაამატე
# პირველ სიაში, სხვა შემთხვევაში მეორეში. საბოლოოდ დაბეჭდე ორივე სია.

ELEMENTS1 =  []
ELEMENTS2 =  []

for i in range(5):
    word = input("enter word")
    if len(word)>5:
        ELEMENTS2.append(word)
    else:

        ELEMENTS1.append(word)

    print(ELEMENTS1)
    print(ELEMENTS2)