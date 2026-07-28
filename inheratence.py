class vehicle:

    def __init__(self,nam,topspeed,mileage,modle):

        self.nam = nam
        self.topspeed = topspeed
        self.mileage = mileage
        self.modle = modle



class bmv(vehicle):
    pass

private_vehical = bmv('bmv',450,9000,'Anas_vehical')

print('vehical name is :',private_vehical.nam,'\n speed is: ',private_vehical.topspeed,'\n mileage is: ',private_vehical.mileage,'\n modle is: ',private_vehical.modle)