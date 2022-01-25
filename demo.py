from sq_footage_circum import square_footage, circum


running = True
while running:
    user_input = input(f"Would you like to calculate square footage, circumference, or exit?")
    if user_input == "square footage":
        user_input_l = float(input("What is the length"))
        user_input_w = float(input("What is the width"))
        print(square_footage(user_input_l, user_input_w))
    if user_input == "circumference":
        user_input_d = float(input("What is the diameter of your circle?"))
        print(circum(user_input_d))
    if user_input == "exit":
        print("Goodbye!")
        running =False