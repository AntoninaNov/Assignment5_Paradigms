from input_handler import handle_input
from command_processor import process_command

def main():
    while True:
        user_input = handle_input()
        if user_input.get('exit_program'):
            break
        process_command(user_input)

if __name__ == "__main__":
    main()


# /Users/antoninanovak/CLionProjects/Assignment2_Paradigms/cmake-build-debug/11_3.txt

# /Users/antoninanovak/PycharmProjects/Assignment5_Paradigms/output_file.txt