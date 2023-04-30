#Extract The Users Information

file_path = input("Please enter the absolute file path: ")
extracted_info = []

try:
    with open(file_path, "r") as user_file:
        find_user = input("Please enter your contacts information: ")
    
        for line in user_file:
            if find_user in line:
                extracted_info.append(line.strip())
                extracted_info.append(next(user_file).strip())
                extracted_info.append(next(user_file).strip())
            
            if not line:
                break
            
except FileNotFoundError:
    print("File does not exist")
except IsADirectoryError:
    print("File is a directory")

if len(extracted_info) > 0:
    print(extracted_info)
else:
    print("No User Found")

