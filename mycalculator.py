def area_of_triangle(base, height):
    area = 0.5 * base * height
    print(f"Area: {area}")
    

def area_of_parallelogram(base, height):
    a_paral = base * height
    print(f"Area Of Parallelogram {a_paral}")


def main():
    user_input = int(input("1) Calculate Area Of Triangle \n2) Calculate Area Of Parallelogram \n Enter Choice: "))

    if user_input == 1:
        u_base = float(input("Enter Base Number: "))
        u_height = float(input("Enter Height Number: "))
        area_of_triangle(u_base, u_height)
        area_of_triangle(4, 5)
        main()
    elif user_input == 2:
        base = float(input("Enter Base Number: "))
        height = float(input("Enter height Number: "))
        area_of_parallelogram(base, height)
        main()


main()
