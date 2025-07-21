# მიგეცემათ რიცხვების სია (მაგ: [5, 10, 3, 8]).
# დაწერეთ ფუნქცია, რომელიც იპოვის:
# ყველაზე პატარა რიცხვს.
# ყველაზე დიდ რიცხვს
# და საშუალოს (ყველა რიცხვის ჯამი გაყოფილი ელემენტების რაოდენობაზე)

def bigest_numbers(numbers):
    if not numbers:
        return "sia carielia"
    min_num = min(numbers)
    max_num = max(numbers)
    average = sum(numbers) / len(numbers)
    return min_num,max_num,average
print(bigest_numbers([5, 10, 3, 8]))