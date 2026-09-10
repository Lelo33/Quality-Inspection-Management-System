def get_inspection_details():
    inspector_name = input("Enter inspector name: ")
    production_line = input("Enter production line: ")
    equipment_name = input("Enter equipment name: ")
    inspection_result = input("Enter inspection result (Pass/Fail): ").strip().lower()

    print("\n--- Inspection Details ---")
    print("Inspector:", inspector_name)
    print("Production Line:", production_line)
    print("Equipment:", equipment_name)

    if inspection_result == "pass":
        print("Inspection Passed")
    else:
        print("Inspection Failed - action required")

# Main program starts here
keep_going = "yes"

while keep_going == "yes":
    get_inspection_details()
    keep_going = input("\nLog another inspection? (yes/no): ").strip().lower()

print("\nShift complete. No more inspections.")
