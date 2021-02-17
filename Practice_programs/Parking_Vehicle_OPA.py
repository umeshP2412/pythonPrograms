class ParkedVehicle:
    def __init__(self, vehicleSeq, fourWheeler, parkedFor, valetParking):
        self.vehicleSeq = vehicleSeq
        self.fourWheeler = fourWheeler
        self.parkedFor = parkedFor
        self.valetParking = valetParking
        self.parkedStatus = "Parked"

class ParkingLot:
    def __init__(self, parkd_vehicle):
        self.parkd_vehicle = parkd_vehicle

    def updateParkedStatus(self, lot_number):
        pv = self.parkd_vehicle
        for k in pv.keys():
            if k == lot_number:
                pv[k].parkedStatus ="Cleared"
                return (lot_number, pv[k].parkedStatus)

        return None

    def getParkingCharges(self, lot_number):
        pv = self.parkd_vehicle
        for i in pv.keys():
            if i == lot_number:
                if pv[i].fourWheeler == "Yes":
                    parkingCharges=pv[i].parkedFor*50.0
                else:
                    parkingCharges=pv[i].parkedFor*30.0

                if pv[i].valetParking=="Yes":
                    parkingCharges=parkingCharges+10

                return parkingCharges
        return None

if __name__ == "__main__":
    noOfVehicle = int(input())

    dict={}
    while noOfVehicle>0:
        v_seq=int(input())
        fourWheeler = input()
        parkedFor = float(input())
        valetParking=input()
        lot_num=int(input())

        v=ParkedVehicle(v_seq, fourWheeler, parkedFor, valetParking)
        dict.update({lot_num:v})
        noOfVehicle -= 1

    pv = ParkingLot(dict)
    lot_no=int(input())
    result=pv.updateParkedStatus(lot_no)

    if result == None:
        print("Lot Number Invalid")
    else:
        print(result[0],result[1])

    result=pv.getParkingCharges(lot_no)
    if result == None:
        print("Lot Number Invalid")
    else:
        print(result)


