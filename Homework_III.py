from datetime import datetime



def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        print("Невірний формат дати. Використовуйте ГГГГ-ММ-ДД.")
        return None
    today_date = datetime.today().date()
    return (given_date - today_date).days

user_date = input("ГГГГ-ММ-ДД: ")
days_difference = get_days_from_today(user_date)

if days_difference is not None:
    print(f"Різниця між {user_date} і сьогоднішнім днем: {abs(days_difference)} днів")

import random
def get_numbers_ticket(min, max, count):
    if min > max or min < 1 or (max-min+1)<count:
        return[]
    numbers = random.sample(range(min, max + 1), count)
    return sorted(numbers)


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)



import re 

def normalize_phone(phone_number):
    phone_number = re.sub(r'\D', '', phone_number)
    
    if phone_number.startswith('38'):
        return "+" + phone_number
        normalize_phone = "+" + re.sub(r'(38)?\D', '', phone_number)
        return normalize_phone
    if  not phone_number.startswith('38'):
        normalize_phone = "+38"+ re.sub(r'\D', '', phone_number)

    return normalize_phone

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)




