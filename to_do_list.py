def add_plan(plans):
    plan = input("Enter the plan you want to add: ")
    plans.append(plan)
    print(f"Plan '{plan}' has been successfully added.")

def update_plan(plans):
    plan_to_update = input("Enter the plan name you want to update: ")
    if plan_to_update in plans:
        new_plan = input("Enter the new plan: ")
        index = plans.index(plan_to_update)
        plans[index] = new_plan
        print(f"Plan '{plan_to_update}' has been updated to '{new_plan}'.")
    else:
        print(f"Plan '{plan_to_update}' not found.")

def delete_plan(plans):
    plan_to_delete = input("Enter the plan name you want to delete: ")
    if plan_to_delete in plans:
        plans.remove(plan_to_delete)
        print(f"Plan '{plan_to_delete}' has been deleted.")
    else:
        print(f"Plan '{plan_to_delete}' not found.")

def view_plans(plans):
    if plans:
        print("Your plans are:")
        for i, plan in enumerate(plans, start=1):
            print(f"{i}. {plan}")
    else:
        print("No plans available.")

def plan_manager():
    plans = []
    print(".   WELCOME TO THE PLAN MANAGEMENT APP    .")

    total_plan = int(input("Enter the number of plans you want to add initially: "))
    for i in range(total_plan):
        plan_name = input(f"Enter plan {i + 1}: ")
        plans.append(plan_name)

    while True:
        print("\nOperations:")
        print("1) Add a plan")
        print("2) Update a plan")
        print("3) Delete a plan")
        print("4) View plans")
        print("5) Exit")

        try:
            operation = int(input("Choose an operation: "))
            if operation == 1:
                add_plan(plans)
            elif operation == 2:
                update_plan(plans)
            elif operation == 3:
                delete_plan(plans)
            elif operation == 4:
                view_plans(plans)
            elif operation == 5:
                print("Bye Bye I am going to sleep. Have a great day :)")
                break
            else:
                print("Invalid input. Please enter a number from 1 to 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Start the plan manager
plan_manager()
