from ParkingLot import ParkingLot, Car
parking_lot = ParkingLot()

def get_commands_and_arguments_from_file(line):
    splitted_line = line.strip("\n").split(" ")
    command = splitted_line[0]
    arguments = splitted_line[1:]
  
    return command, arguments

def main(command_params):

  try:
    file_path = command_params

    with open(file_path, 'r') as fileReader:
      Lines = fileReader.readlines()
      for line in Lines:
        command, arguments = get_commands_and_arguments_from_file(line)

        if command == 'Create_parking_lot':
          parking_lot.create_parking_lot(int(arguments[0]))

        elif command == 'Park':
          car = Car(arguments[0], arguments[2])
          parking_lot.park(car)

        elif command == 'Leave':
          parking_lot.leave(int(arguments[0]))

        elif command == 'Vehicle_registration_number_for_driver_of_age':
          parking_lot.registration_numbers_for_cars_for_driver_age(arguments[0])

        elif command == 'Slot_numbers_for_driver_of_age':
          parking_lot.slot_numbers_for_cars_for_driver_age(arguments[0])

        elif command == 'Slot_number_for_car_with_number':
          parking_lot.slot_number_for_registration_number(arguments[0])

        else:
          raise Exception("Wrong command")
  except:
    raise Error("Please pass input file")

if __name__ == "__main__":
  main("input1.txt")