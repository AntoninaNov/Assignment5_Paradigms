from file_io import read_file, write_file
from encryption import encrypt, decrypt

def process_command(user_input):
    text = read_file(user_input['file_path_input']) if user_input['source'] == "file" else input("Enter text: ")

    result = encrypt(text, user_input['key']) if user_input['command'] == "encrypt" else decrypt(text, user_input['key'])

    if result is not None:
        if user_input['output_destination'] == "file":
            write_file(user_input['file_path_output'], result)
            print(f"{user_input['command'].capitalize()}ion completed. Output written to file.")
        else:
            print("Output text:", result)
            print(f"{user_input['command'].capitalize()}ion completed.")
    else:
        print("Operation failed. No output generated.")
