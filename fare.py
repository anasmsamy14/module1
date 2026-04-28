class Vehicle:
    def fare(self, capacity):
        return capacity * 100


class Bus(Vehicle):
    def fare(self, capacity):
        total = super().fare(capacity)
        return total + (total * 0.10)   # add 10%


# Create bus object
bus = Bus()

# Seating capacity = 50
print("Total Bus Fare:", bus.fare(50))