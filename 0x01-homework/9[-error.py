class CustomError(Exception):
    pass
id_number = 25

try:
    input_id = int(input("Enter your id_number: "))
    if input_id < id_number:
        raise CustomError
    else:
        print("id number is valid")
except CustomError:
    print("Exception occured: Invaild id number")