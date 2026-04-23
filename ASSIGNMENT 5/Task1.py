marks ={"Arjun": {"English":98 , "Math":78 ,"Science":88 ,"Hindi": 92 ,"Social Science":67},
        "Rohan": {"English":77 , "Math":38 ,"Science":48 ,"Hindi": 72 ,"Social Science":87},
        "Mohit": {"English":95 , "Math":98 ,"Science":87 ,"Hindi": 96 ,"Social Science":60}
        }

name =input("Enter the student's name : ")
if name in marks:
    print(f"{name}'s marks: {marks[name]}")
else:
    print("Student not found")