class  vehicle:

    def __init__(self, max_speed, mileage):
        
        self.max_speed = max_speed
        self.mileage = mileage


model = vehicle(240,18)

print ('the max speed of car is',model.max_speed)

print ('model mileage',model.mileage)