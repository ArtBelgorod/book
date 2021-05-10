from adm_priv import Admin, Privileges

my_admin = Admin('Art','Khaimov','admin@admin.com','Belgorod')
print(f"Админу {my_admin.f_name} {my_admin.l_name}:")
my_admin.privileges.show_privileges()