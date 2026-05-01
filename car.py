class BMW:
    def fuel_type(self):
        print("BMW uses Petrol")

    def max_speed(self):
        print("BMW max speed is 250 km/h")

    def where_made(self):
        print("BMW is made in Germany")


class Ferrari:
    def fuel_type(self):
        print("Ferrari uses Petrol")

    def max_speed(self):
        print("Ferrari max speed is 340 km/h")

    def where_made(self):
        print("Ferrari is made in Italy")


class Tesla:
    def fuel_type(self):
        print("Tesla uses Electricity")

    def max_speed(self):
        print("Tesla max speed is 260 km/h")

    def where_made(self):
        print("Tesla is made in USA")


 
b = BMW()
f = Ferrari()
t = Tesla()


b.fuel_type()
b.max_speed()
b.where_made()

print()

f.fuel_type()
f.max_speed()
f.where_made()

print()

t.fuel_type()
t.max_speed()
t.where_made()