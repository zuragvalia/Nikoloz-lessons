# 2) შექმენი ფუნქცია სახელად checkEvenOdd, რომელიც იღებს
# ერთ რიცხვს და აბრუნებს "ლუწია" თუ რიცხვი ლუწია, ან "კენტია" თუ კენტია.


def checkevenodd(a):
    if a %2==0:
        return "ლუწია"
    else:
        return "კენტია"

print(checkevenodd(6))
print(checkevenodd(5))