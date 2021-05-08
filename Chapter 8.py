# Ex 8.1 8.2
def display_message() :
    """Выводит сообщение"""
    print(f"Изучаем функции в этом файле!")

def favourite_book(title) :
    """Выводит сообщение о книге"""
    print(f"Моя любимая книга -'{title}'!")

favourite_book("Чук и Гек")

# Ex 8.3-8.5
def make_shirt(size = "XL", text = "I love Python!"):
    """Выводит сообщение и размер футболки"""
    print(f'Моя футболка размера {size} с надписью: "{text}"')

def describe_city(city, country = "Russia"):
    """Выводит город и страну"""
    print(f'{city.title()} находится в {country.title()}')

make_shirt(52, "You!")
make_shirt(size = 48, text = "You do it!")
make_shirt()
make_shirt(size = "L", text = "You do it too!")
print("---------------------------")
describe_city("Moscow")
describe_city("Reykjavik","Iceland")
describe_city("Belgorod")

# Ex 8.6 - 8.8
def city_country(city,country):
    city_and_country = city + ", " + country
    return city_and_country

print(city_country ("Moscow", "Russia"))
print(city_country ("Santiago", "Chile"))
print(city_country ("Kiev", "Ukraine"))

def make_album(album_name, artist, my_count=None):
    my_album = {'artist': artist, 'album_name': album_name}
    if my_count:
        my_album['count'] = my_count
    return my_album

print(make_album("3 Сентября", "М. Шуфутинский"))
print(make_album("Вагон Столыпинский", "Лесоповал"))
print(make_album("Владимирский централ", "М. Круг"))
print(make_album("Владимирский централ", "М. Круг", 12))

active = True
while active:
    user_album = input("Введите название альбома: ")
    user_artist = input("Введите исполнителя: ")
    repeat = input ("Введём ещё? (д/н) ")
    while True:
        if repeat == "н":
            active = False
            break
        elif repeat == "д":
            break
        else:
            repeat = input ("Введём ещё? (д/н) ")
    print(f"Словарь - {make_album(user_album, user_artist)}")

#Ex 8.9 - 8.11
def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages):
    sent_messages = []
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)
    sent_messages.reverse()
    return sent_messages

my_messages = ["Hello!","Boys and Girls!","Good game!"]
print(send_messages(my_messages[:]))
print(my_messages)
