# IS_Lab2_Forward-Chaining
## Fact and Rule Generator using Forward Chaining

This Python script implements a simple system for managing facts and rules. Users can input facts and rules, print existing ones, and generate new facts based on defined rules.

## Features

- **Add and Print Facts:** Users can enter new facts, view existing facts, and delete all facts.

- **Add and Print Rules:** Users can define rules based on existing facts, view existing rules, and delete all rules.

- **Generate New Facts:** The system can generate new facts based on defined rules.

## File Management

The script uses two files, "facts.txt" and "rules.txt," to persistently store facts and rules. If these files do not exist, the script creates empty files for them.

## Usage

1. Run the script in a Python environment.

2. Choose from the following options:
   - **Print current facts and rules (Option 0):** Display the existing facts and rules.
   - **Enter a fact (Option 1):** Add a new fact.
   - **Enter a rule (Option 2):** Add a new rule based on existing facts.
   - **Generate new facts (Option 3):** Generate new facts based on defined rules.
   - **Delete all facts (Option 4):** Remove all existing facts.
   - **Delete all rules (Option 5):** Remove all existing rules.
   - **Exit (Option 6):** Exit the script.

3. Follow the prompts to interact with the system.

## File Descriptions

- `facts.txt`: File containing existing facts.
- `rules.txt`: File containing existing rules.

## Notes

- Ensure that the required files (`facts.txt` and `rules.txt`) are in the same directory as the script.

- If you encounter any issues or have questions, feel free to reach out.

Enjoy managing your facts and rules!
