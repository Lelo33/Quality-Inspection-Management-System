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
    return inspection_result 

# Main program starts here
keep_going = "yes"
pass_count = 0
fail_count = 0
inspection_results = []

while keep_going == "yes":
   results = get_inspection_details()
   inspection_results.append(results)
if results == "pass":
    pass_count += 1
else:
    fail_count += 1
keep_going = input("\nLog another inspection? (yes/no): ").strip().lower()
print("\nShift complete. Total Passed:", pass_count, "| Total Failed:", fail_count)
