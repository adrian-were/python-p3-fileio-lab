def write_file(file_name, file_content):
    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content)
    print(f"File '{file_name}.txt' was successfully written.")

def append_file(file_name, file_content):
    with open(f"{file_name}.txt", "a") as file:
        file.write(file_content)
    print(f"Content appended to '{file_name}.txt'.")

def read_file(file_name):
    with open(f"{file_name}.txt", "r") as file:
        content = file.read()
        return content

