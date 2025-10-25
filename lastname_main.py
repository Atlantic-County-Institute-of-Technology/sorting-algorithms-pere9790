#Kevin Perez-Morales
#10/24/25

import os
import random #Used later to generate random numbers.
import time #Used later to find out how long each sorting process takes.

#Import the 3 sorting functions from their files.
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort

#A function to clear the terminal, later called to reset/restart.
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


#The main function to run the entire program.
def main():
    #Create default settings by creating variables: the list will start empty and have a defined list size, minimum value, and maximum value.
    numbers = []
    list_size = 10
    min_val = -100
    max_val = 100

    #The Main Loop/Menu for the program.
    while True:
        print("\n Sorting Options ")
        print(f"Current list: {numbers if numbers else 'No list yet'}") #Show the current list or displays "No list yet" if the list is empty.
        print(f"List size: {list_size}, Range: {min_val} to {max_val}") #Show the current settings for list size and range.
        #Display menu options.
        print("[-] 0. Exit")
        print("[-] 1. Generate a New List")
        print("[-] 2. Change List Manually")
        print("[-] 3. Bubble Sort")
        print("[-] 4. Insertion Sort")
        print("[-] 5. Selection Sort")

        #Ask for users input.
        choice = input("[-] Please choose an option: ")

        #Clear the screen after each choice for clarity.
        clear_screen()

        #Option 0; Exit
        if choice == "0":
            print("Bye, bye!")
            break

        #Option 1; Generate a New List
        elif choice == "1":
            #Check that range is valid: the minimum must be smaller than maximum.
            if min_val >= max_val:
                print("[!] Error: Minimum must be smaller than maximum.")
                continue
            #Check that list size is valid: the list must be positive (can't be a negative).
            if list_size <= 0:
                print("[!] Error: List size must be positive.")
                continue
            #Creates a new numbers list of list_size(#) random values between min_val and max_val.
            numbers = [random.randint(min_val, max_val) for n in range(list_size)]
            print("New list:", numbers)

        #Option 2; Change List Manually
        elif choice == "2":
            try:
                #Ask the user for a new list size.
                list_size = int(input("Enter list size (positive numbers only): "))
                if list_size <= 0:
                    print("[!] Error: List size must be positive.")
                    continue

                #Ask the user for a new minimum and maximum value.
                min_val = int(input("Enter minimum value: "))
                max_val = int(input("Enter maximum value: "))

                #Check that range is valid: the minimum must be smaller than maximum.
                if min_val >= max_val:
                    print("[!] Error: Minimum must be smaller than maximum.")
                    continue

                print("List has been updated.")

                #Creates a new numbers list of list_size(#) random values between min_val and max_val.
                numbers = [random.randint(min_val, max_val) for n in range(list_size)]
                print("New list:", numbers)

                #If the user types letters instead of a number:
            except ValueError:
                print("[!] Error: Please enter valid whole numbers.")


        #Option 3; Bubble Sort
        elif choice == "3":
            #Verify that a list does exist.
            if not numbers:
                print("[!] Error: Please generate a list first.")
                continue
            print("Before:", numbers) #Show the unsorted list.
            start = time.time() #Record time before sorting.
            #Run the bubble_sort function on a copy of the list, in order to not affect the original; return sorted list, loop count, and swap count.
            sorted_list, loops, swaps = bubble_sort(list(numbers))
            end = time.time() #Record time after sorting
            print("After:", sorted_list) #Show the sorted list.
            print(f"Loops: {loops}, Swaps: {swaps}, Time: {end - start:.5f}s")

        # Option 4; Insertion Sort
        elif choice == "4":
            #Verify that a list does exist.
            if not numbers:
                print("[!] Error: Please generate a list first.")
                continue
            print("Before:", numbers)
            start = time.time()
            #Run the insertion_sort function on a copy of the list, in order to not affect the original; return sorted list, loop count, and insert count.
            sorted_list, loops, inserts = insertion_sort(list(numbers))
            end = time.time()
            print("After:", sorted_list)
            print(f"Loops: {loops}, Inserts: {inserts}, Time: {end - start:.5f}s")

        #Option 5; Selection Sort
        elif choice == "5":
            #Verify that a list does exist.
            if not numbers:
                print("[!] Error: Please generate a list first.")
                continue
            print("Before:", numbers)
            start = time.time()
            #Run the selection_sort function on a copy of the list, in order to not affect the original; return sorted list, loop count, and swap count.
            sorted_list, loops, swaps = selection_sort(list(numbers))
            end = time.time()
            print("After:", sorted_list)
            print(f"Loops: {loops}, Swaps: {swaps}, Time: {end - start:.5f}s")

        #If user enters anything else, show an error.
        else:
            print("[!] Error: Invalid option, please try again.")

if __name__ == "__main__":
    main()
