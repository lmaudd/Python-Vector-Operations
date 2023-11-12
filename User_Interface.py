from Functions import *

#User Interface
while True:

    print("""\nMain Menu:\n
            What would you like to do? [enter with number]\n
                1. Vector Addition
                2. Vector Subtraction
                3. Vector Multiplication by Scalar
                4. Vector Division by Scalar
                5. Vector Dot Product
                6. Vector Cross Product
                7. Vector Projection
                8. Quit""")

    try:
        choice = int(input("\n            Option: "))
    except:
        print('\nPlease only enter a number!')
        continue

#1. VECTOR MULTIPLICATION
    if choice == 1:
        print("\nMain Menu: Vector Addition\n")
        vec_add()
        
#2. Vector Subtraction
    elif choice == 2:
        print(f"\nMain Menu: Vector Subtraction\n")
        vec_sub()

#3. Vector Multiplication by Scalar
    elif choice == 3:
        print("\nMain Menu: Vector Multiplication by Scalar\n")
        vec_mult()

#4. Vector Division by Scalar
    elif choice == 4:
        print("\nMain Menu: Vector Division by Scalar\n")
        vec_div()

#5. Vector Dot Product  
    elif choice == 5:
        print("\nMain Menu: Vector Dot Product\n")
        vec_dp()

#6. Vector Cross Product
    elif choice == 6:
        print("\nMain Menu: Vector Cross Product\n")
        vec_cp()

#7 Vector Projection
    elif choice == 7:
        print("\nMain Menu: Vector Projection\n")
        vec_projection()

# DONE
    else:
        print("\nThank you!\n\n")
        break
