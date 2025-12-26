def title():
    print("==== GPA CALCULATOR ====")
    print("1. View current GPA and credit hours")
    print("2. Calculate new GPA (or add to a current one)")
    print("3. Delete current GPA record")
    print("4. Exit program\n")

def read_gpa():
    try:
        with open("gpa_data.txt", 'r') as f:
            if f.read(1) == "":
                print("\nNo record exists for now.\n")
                return False
            else:
                f.seek(0)
                gpa_data = {}
                for x in f:
                    list_dict = x.split(':')
                    if list_dict[1].strip().isalpha() or list_dict[1].strip().isalnum():
                        gpa_data[list_dict[0]] = list_dict[1].strip()
                    else:
                        gpa_data[list_dict[0]] = float(list_dict[1].strip())
                return gpa_data
    except FileNotFoundError:
        print("\nNo file exists for now, please calculate a GPA to make one.\n")

def output_gpa():
    if read_gpa != False:
        gpa_data = read_gpa()
        print(f"\nStudent name: {gpa_data["name"]}")
        print(f"Your current GPA is: {gpa_data["GPA"]}")
        print(f"Credit hours completed: {gpa_data["hours"]}\n")
    else:
        print("\nNo record exists for now.\n")

def write_gpa(gpa_data):
    with open("gpa_data.txt", 'w') as f:
        name = input("Enter your name: ")
        gpa_data["name"] = name
        for x,y in gpa_data.items():
            f.writelines(f"{x}:{y}\n")

def calculate_gpa(gpa_data):
    gpa_scheme = {"A+":4.00, "A":3.75, "B+":3.50, "B":3.00, "C+":2.50, "C":2.00, "D+":1.50, "D":1.00, "F":0.00}
    num_subjects = int(input("Enter the number of subjects to input: "))
    total_quality_points = 0
    temp_hours = 0
    for x in range(num_subjects):
        new_credit_hours = int(input(f"Enter the number of credit hours of class number {x + 1}: "))
        temp_hours += new_credit_hours
        grade = input(f"Enter the grade of class number {x + 1} (for example: A+, A, B+, B...): ")
        total_quality_points += (gpa_scheme[grade] * new_credit_hours)
    if "hours" in gpa_data:
        existing_quality_points = float(gpa_data["GPA"]) * float(gpa_data["hours"])
        total_quality_points += existing_quality_points
        existing_hours = int(gpa_data["hours"])
        total_hours = temp_hours + existing_hours
    else:
        total_hours = temp_hours
    gpa = float(f"{total_quality_points / total_hours:.2f}")
    gpa_and_hours = {"GPA":gpa, "hours":total_hours}
    return gpa_and_hours

def delete_gpa():
    with open("gpa_data.txt", "w"):
        print("Record has been deleted succesfully.")

def main():
    gpa_data = {"name": "", "GPA": 0, "hours": 0}
    while True:
        title()
        user_choice = int(input("Enter your choice (1-4): "))
        if user_choice == 1:
            output_gpa()
        elif user_choice == 2:
            if read_gpa() != False:
                current_gpa = read_gpa() 
                gpa_data = calculate_gpa(current_gpa)
            else:
                gpa_data = calculate_gpa(gpa_data)
            write_gpa(gpa_data)
        elif user_choice == 3:
            delete_gpa()
        elif user_choice == 4:
            break

if __name__ == "__main__":
    main()