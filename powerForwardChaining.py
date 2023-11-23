import os

# Function to check and create files if they don't exist
def check_and_create_files():
    for file_name in ["facts.txt", "rules.txt"]:
        if not os.path.isfile(file_name):
            with open(file_name, "w") as data_file:
                # Create an empty file if it doesn't exist
                pass

# Initialize empty dictionaries for facts and rules
facts = {}
rules = {}

# Check and create files if they don't exist
check_and_create_files()

# Function to read data from a file and populate a dictionary
def load_data(file_name, data_dict):
    try:
        with open(file_name, "r") as data_file:
            file_contents = data_file.read()
            if file_contents:
                content = file_contents.strip().split('\n')  # Split by newline
                data_dict.update({item: True for item in content})
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred while reading '{file_name}': {str(e)}")

# Function to save data to a file with one item per line
def save_data(file_name, data_dict):
    try:
        with open(file_name, "w") as data_file:
            content = "\n".join(data_dict.keys())
            data_file.write(content)
    except Exception as e:
        print(f"An error occurred while writing to '{file_name}': {str(e)}")

# Function to print current facts and rules
def print_data(data_dict, data_type):
    print(f"\nCurrent {data_type.capitalize()}:")
    for item in data_dict.keys():
        print(item)

# Function to add a new item to a dictionary
def add_item(item, data_dict, file_name, data_type):
    if item not in data_dict:
        data_dict[item] = True
        print(f"\n[{item}] has been added to {data_type}.")
        print_data(data_dict, data_type)
        save_data(file_name, data_dict)
    else:
        singular_data_type = data_type[:-1]
        print(f"\n'{item}' already exists in {data_type}. Please enter a different {singular_data_type}.")

# Function to generate new items based on existing rules
def generate_new_facts(rules_dict, facts_dict):
    new_items = []
    for rule in rules_dict.keys():
        if ", then " in rule:
            conditions, result = rule.split(", then ")
            condition_facts = conditions.replace("if ", "").split(" and ")
            if all(condition in facts_dict for condition in condition_facts) and result not in facts_dict:
                new_items.append(result)
        else:
            print(f"Invalid rule format: {rule}")

    if new_items:
        facts_dict.update({item: True for item in new_items})
        print("\nNew Generated Fact(s):", new_items)
        save_data("facts.txt", facts_dict)
        generate_new_facts(rules_dict, facts_dict)  # Recursively generate new items
    else:
        print("\nNo new facts can be generated.")

# Main loop
while True:
    load_data("facts.txt", facts)
    load_data("rules.txt", rules)

    print("\nOptions:")
    print("[0] Print current facts and rules")
    print("[1] Enter a fact")
    print("[2] Enter a rule")
    print("[3] Generate new facts")
    print("[4] Delete all facts")
    print("[5] Delete all rules")
    print("[6] Exit")

    choice = input("\nSelect an Option: ")

    if choice == "1":
        while True:
            new_fact = input("\nEnter a fact (enter 'x' to stop): ")
            print_data(facts, "facts")
            os.system('cls')
            if new_fact == 'x':
                break
            add_item(new_fact, facts, "facts.txt", "facts")

    elif choice == "0":
        os.system('cls')
        print_data(facts, "facts")
        print_data(rules, "rules")

    elif choice == "2":
        while True:
            print_data(facts, "facts")
            new_rule = input("\nEnter a rule based on the facts above (e.g., 'if A and B and C, then D') (enter 'x' to stop): ")
            os.system('cls')
            if new_rule == 'x':
                break
            add_item(new_rule, rules, "rules.txt", "rules")

    elif choice == "3":
        os.system('cls')
        generate_new_facts(rules, facts)

    elif choice == "4":
        facts = {}
        save_data("facts.txt", facts)
        os.system('cls')
        print("\nFacts deleted.")

    elif choice == "5":
        rules = {}
        save_data("rules.txt", rules)
        os.system('cls')
        print("\nRules deleted.")

    elif choice == "6":
        break

    else:
        os.system('cls')
        print("\nInvalid choice. Please try again.")
