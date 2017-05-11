class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("The last name is: " + self.last_name)
        print("The eye color is: " + self.eye_color)

class Child(Parent):
    def __init__(self, first_name, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.first_name = first_name
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("The last name is: " + self.last_name)
        print("The last name is: " + self.eye_color)
        print("The last name is: " + str(self.number_of_toys))


billy_cyrus = Parent("Cyrus", "Blue")
# billy_cyrus.show_info()
# print(billy_cyrus.eye_color)

muema = Child("Muthiani","Mutiso", "Yellow", 25)
muema.show_info()
# print(muema.last_name)
# print(muema.eye_color)
# print(billy_cyrus.last_name)

