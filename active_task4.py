from Location import Location

if __name__ == '__main__':
    unknown_place = Location(10.00, 0.00)
    new_york = Location(40.7127753, -74.0059728)

    print("First Location instance: ", unknown_place)
    print("Second Location instance: ", new_york)
    print("Sum of two Location instance: ", unknown_place + new_york)

    new_york.visualize()
