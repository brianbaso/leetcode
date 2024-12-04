class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        # create a hashmap to manage spaces
        self.hashmap = {}
        self.hashmap[1], self.hashmap[2], self.hashmap[3] = big, medium, small

    def addCar(self, carType: int) -> bool:
        if self.hashmap[carType] > 0:
            self.hashmap[carType] -= 1
            return True
        else:
            return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)