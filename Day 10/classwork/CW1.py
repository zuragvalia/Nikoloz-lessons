# classwork 1) შექმენი ფუნქცია, რომელსაც გადაეცემა რიცხვების სია.
# გადაუარე ამ სიას for ციკლით და ჩაამატე მხოლოდ ლუწი რიცხვები ახალ სიაში. საბოლოოდ დააბრუნეთ ეს სია.

def numbers_lst(numbers):
    new_lst = []
    for i in numbers:
        if i %2 == 0:
            new_lst.append(i)
    return new_lst
print(numbers_lst([1,2,2,55,77,8888]))