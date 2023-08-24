'''
Beau Simon
CSCI L02
Assignment #11
Online Student - 0869416
'''

def input_data(names):
    name = input("Enter the name (Firstname Lastname): ")
    names.append(name)

def insertion_sort(names):
    for i in range(1, len(names)):
        key = names[i]
        j = i - 1
        last_name_key, first_name_key = key.split()[1], key.split()[0]
        
        while j >= 0:
            last_name_j, first_name_j = names[j].split()[1], names[j].split()[0]
            if last_name_j > last_name_key or (last_name_j == last_name_key and first_name_j > first_name_key):
                names[j + 1] = names[j]
                j -= 1
            else:
                break

        names[j + 1] = key

def display_names(names):
    print("\nSl. No\tNames")
    for i, name in enumerate(names):
        first_name, last_name = name.split()
        print(f"{i + 1}.\t{last_name}, {first_name}")

def menu():
    names = []

    while True:
        print("\nMenu:")
        print("Option 1: Input the names (Firstname Lastname)")
        print("Option 2: Sort the names (Lastname Firstname)")
        print("Option 3: Exit")

        option = int(input("Enter the option number: "))

        if option == 1:
            input_data(names)
        elif option == 2:
            insertion_sort(names)
            display_names(names)
        elif option == 3:
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()
