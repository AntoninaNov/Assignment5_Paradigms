def get_input(prompt, options=None):
    while True:
        user_input = input(prompt)
        if not options or user_input in options:
            return user_input
        print(f"Invalid input. Please enter one of {options}.")


def handle_input():
    if get_input("Press 'e' to exit or 'c' to continue: ", ["e", "c"]) == "e":
        return {'exit_program': True}

    source = get_input("Input text method [console/file]: ", ["console", "file"])
    file_path_input = get_input("Enter path to the input file: ") if source == "file" else None

    command = get_input("Operation [encrypt/decrypt]: ", ["encrypt", "decrypt"])
    key = int(get_input("Enter a key (integer): "))  # Convert key to integer

    output_destination = get_input("Output method [console/file]: ", ["console", "file"])
    file_path_output = None
    if output_destination == "file":
        if get_input("Overwrite input file? (yes/no): ", ["yes", "no"]) == "yes":
            file_path_output = file_path_input
        else:
            file_path_output = get_input("Enter path to the output file: ")


    return {
        'exit_program': False,
        'source': source,
        'file_path_input': file_path_input,
        'command': command,
        'key': key,
        'output_destination': output_destination,
        'file_path_output': file_path_output,
    }

