from Coordinates import Coordinates

if __name__ == '__main__':
    unknown_place = Coordinates(10.00, 0.00)
    new_york = Coordinates(40.7127753, -74.0059728)

    print("First Coordinates instance: ", unknown_place)
    print("Second Coordinates instance: ", new_york)
    print("Sum of two Coordinates instance: ", unknown_place + new_york)

    new_york.visualize()