
#IT3883/W02
#Nornu Ninayor
#Assignment 1
#01/27/25
#this program allows users to do 4 things append,clear,display, and exist.
#Resources used W3chool,youtube,& google


def text_menu():
    input_buffer = ""

    while True:
        print("\nMenu:")
        print("1. Append data to the input buffer")
        print("2. Clear the input buffer")
        print("3. Display the input buffer")
        print("4. Exit the program")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            input_buffer += input("Enter text to append: ")
        elif choice == "2":
            input_buffer = ""
            print("Buffer cleared.")
        elif choice == "3":
            print(f"Buffer: {input_buffer}")
        elif choice == "4":
            print("Exiting.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    text_menu()
