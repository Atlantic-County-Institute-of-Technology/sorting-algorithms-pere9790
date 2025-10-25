#Kevin Perez-Morales
#10/24/25
#Insertion sort function; sorts by taking one number at a time and inserting it into its correct spot.

def insertion_sort(values):
    print("\nUsing Insertion Sort...")
    loops = 0 #Counts total times the loops runs.
    inserts = 0 #Counts how many moves happened.

    #Start from the second element and move foward.
    for i in range(1, len(values)):
        loops += 1
        chosen_number = values[i] #The current number that will be placed correctly.
        j = i - 1 #Check the number before it.
        
        #Move larger numbers one spot to the right.
        while j >= 0 and values[j] > chosen_number:
            values[j + 1] = values[j]
            j -= 1
            inserts += 1
        #Put the current number in the right spot.
        values[j + 1] = chosen_number
    #Return sorted list. # of loops, and # of inserts.
    return values, loops, inserts
