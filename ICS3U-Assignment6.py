# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: December 2022
# ICS3U-Unit5-04.py File, learning functions with parameters in python.

import math


def area_of_triangle(radius_as_float, height_as_float):

    surface_area = (
        radius_as_float * 2.0 * height_as_float * math.pi
        + 2.0 * math.pi * math.pow(radius_as_float, 2)
    )
    return surface_area


def main():

    radius = input("Enter the radius of a cylinder(cm): ")
    height = input("Enter the height of a cylinder(cm): ")
    print("")
    try:
        radius_as_float = float(radius)
        height_as_float = float(height)
        if radius_as_float <= 0 or height_as_float <= 0:
            print(
                "A cylinder cannot have a height or a base with a value that's equal or less than 0."
            )
        else:
            surface_area = area_of_triangle(radius_as_float, height_as_float)
            print(
                "The surface area of the cylinder is {0:,.2f} cm².".format(surface_area)
            )

    except ValueError:
        print("Invalid input, please try again.")
    print("\n\nDone.")


if __name__ == "__main__":
    main()
