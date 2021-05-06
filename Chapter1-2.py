#Работа со строками
message ="hello, world!"
print(message.title())
message ="Hello, World2!"
print(message.lower())
print(message.upper())
first_name = "art"
last_name = "khaimov"
full_name = f"{first_name.title()} {last_name.title()}"
print(f"<Hello {full_name}, would you like some Python today'?")
print(full_name.upper(), "or", full_name.lower(), "or", full_name)
famous_person = "Albert Einstein"
message = "\t\tA person who never made\na mistake never tried anything new.       "
print(f'1{famous_person} once said,"{message}"')
print(f'l{famous_person} once said,"{message.lstrip()}"')
print(f'r{famous_person} once said,"{message.rstrip()}"')
print(f's{famous_person} once said,"{message.strip()}"')
print("__________________________________")
#Работа с числами
print(5+3)
print(4+4)
print(2+6)
print(1+7)
mess = "My favourite num is "
num = 5
print(f'{mess}{num}!')
