# 1)classwork:შექმენი ცვლადი სადაც შეინახავ სთრინგს და გაიგეთ,
# არის თუ არა ის პალინდრომი(პალინდრომი არის ისეთი სიტყვა,
# რომელიც ორივე მხრიდან ერთნაირად იკითხება, მაგალითად, "ana"...)

name = "nika"

change_word = (name[::-1])

if change_word == name:
    print(change_word)
else:
    print("this word is not palindrome")
