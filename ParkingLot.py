'''
Reason to use the heap to get the nearest possible slot available so that we can get the possible lowest slot at O(1).
Here we use an HashMap between the cars and slots thus making us easy to access so that.
-> Car[Registration_Number] to Slot[Avaliable_Slot_Number], vice versa
-> Driver Age -> List[No.of parked cars with specific age]
'''

import heapq
from collections import defaultdict, OrderedDict

'''
Car contains two attributes -> Car's registration number and age of driver.
'''
class Car:
    def __init__(self, registration_number, driver_age):
        self.registration_number = registration_number
        self.driver_age = driver_age

class ParkingLot:
    def __init__(self):
        self.registration_slot_mapping = dict()
        self.age_registration_mapping = defaultdict(list)
        self.slot_car_mapping  = OrderedDict()
        self.available_parking_lots = []

    def create_parking_lot(self, total_slots):
        print("Created a parking lot with {} slots".format(total_slots))
        for i in range(1, total_slots + 1):
            heapq.heappush(self.available_parking_lots, i)
        return True

    def get_nearest_slot(self):
        return heapq.heappop(self.available_parking_lots) if self.available_parking_lots else None

    def leave(self, slot_to_be_freed):
        found = None
        for registration_no, slot in self.registration_slot_mapping.items():
            if slot == slot_to_be_freed:
                found = registration_no

        if found:
            heapq.heappush(self.available_parking_lots, slot_to_be_freed)
            del self.registration_slot_mapping[found]
            car_to_leave = self.slot_car_mapping[slot_to_be_freed]
            self.age_registration_mapping[car_to_leave.driver_age].remove(found)
            del self.slot_car_mapping[slot_to_be_freed]
            print("Slot number {0} vacated, the car with vehicle registration number {1} left the space, the driver of the car was of age {2}"\
                  .format(slot_to_be_freed, \
                          car_to_leave.registration_number, \
                          car_to_leave.driver_age))
          
            return True

        else:
            print("slot is not in use")
            return False

    def park(self, car):
        slot_no = self.get_nearest_slot()
        if slot_no is None:
            print("Sorry, parking lot is full")
            return
        print("Car with vehicle registration number " + car.registration_number + \
              " has been parked at {0}".format(slot_no))
        self.slot_car_mapping[slot_no] = car
        self.registration_slot_mapping[car.registration_number] = slot_no
        self.age_registration_mapping[car.driver_age].append(car.registration_number)
        return slot_no

    # Registration numbers of all cars of a specific age
    def registration_numbers_for_cars_for_driver_age(self, driver_age):
        registration_numbers = self.age_registration_mapping[driver_age]
        print(", ".join(registration_numbers))
        return self.age_registration_mapping[driver_age]

    # Slot numbers of all slots where a car of specific aged driver is parked
    def slot_numbers_for_cars_for_driver_age(self, driver_age):
        registration_numbers = self.age_registration_mapping[driver_age]
        slots = [self.registration_slot_mapping[reg_no] for reg_no in registration_numbers]
        print(", ".join(map(str, slots)))
        return slots

    def slot_number_for_registration_number(self, registration_number):
        slot_number = None
        if registration_number in self.registration_slot_mapping:
            slot_number = self.registration_slot_mapping[registration_number]
            print(slot_number)
            return slot_number
        else:
            print("Not found")
            return slot_number