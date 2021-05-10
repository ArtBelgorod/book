from restaurant import Restaurant
from admin_user import Admin, User, Privileges

my_restaurant = Restaurant("Рига","Латвийский ресторан")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_admin = Admin('Art','Khaimov','admin@admin.com','Belgorod')
print(f"Админу {my_admin.f_name} {my_admin.l_name}:")
my_admin.privileges.show_privileges()