def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except IOError:
        print(f"Error reading file: {filename}")
        return ""

def write_file(filename, text):
    try:
        if text is not None:
            with open(filename, 'w') as file:
                file.write(text)
        else:
            print("No text to write.")
    except IOError:
        print(f"Error writing to file: {filename}")
