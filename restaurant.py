class Restaurant():
    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Ресторан - {self.restaurant_name}, тип - {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")

    def set_number_served(self, num_served):
        self.number_served = num_served

    def increment_number_served(self, inc_num_served):
        self.number_served += inc_num_served