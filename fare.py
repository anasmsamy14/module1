class Vehicle:
    def fare(self, capacity):
        return capacity * 100


class Bus(Vehicle):
    def fare(self, capacity):
        total = super().fare(capacity)
        return total + (total * 0.10)   
bus = Bus()


print("Total Bus Fare:", bus.fare(50))