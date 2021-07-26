# Команда проекта «Дом питомца» планирует большой корпоратив для своих волонтеров. Вам необходимо написать программу,
# которая позволяла бы составлять список нескольких гостей. Решите задачу с помощью метода конструктора и примените
# один из принципов наследования. При выводе в консоль вы должны получить:  “Иван Петров, г.Москва, статус "Наставник"
# P.S. Если одной головой тяжело решается, позовите сокурсников. Вместе ведь всегда легче, веселее, интереснее. И еще
# у нас есть отзывчивые менторы  ;)

from guest import Guest

guest_1 = Guest('Иван Петров', 'г.Москва', 'Наставник')
guest_2 = Guest('Петр Иванов', 'г.Самара', 'Волонтер')

print(guest_1.get_name(), ',', guest_1.get_city(), ',', guest_1.get_status())
print(guest_2.get_name(), ',', guest_2.get_city(), ',', guest_2.get_status())