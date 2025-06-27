# 4)შექმენი პროგრამა, რომელიც მომხმარებელს
# სთხოვს პაროლის შეყვანას. სწორი   პაროლია 
# "python123".სანამ არ ჩაწერს სწორად,პროგრამა 
# მას ისევ და ისევ სთხოვს შეყვანას.



password = "python123"
person_password = input("enter password: ")
while person_password != password:
    print("password is incorect: ")
    person_password = input("enter password: ")
print("your password is correct")
