#Kevin Perez-Morales
#10/24/25
#Selection sort function; sorts by finding the smallest number each time and putting it at the front

def selection_sort(values):
    print("\nUsing Selection Sort...")
    loops = 0   #Counts how many times loops run.
    swaps = 0   #Counts how many swaps happen.

    #A loop repeats enough times to go through each position in the list.
    for i in range(len(values)):
        loops += 1
        min_index = i  #Current smallest number's position.
        #Find the smallest number in the rest of the list.
        for j in range(i + 1, len(values)):
            loops += 1
            #If we find a smaller value, record its position.
            if values[j] < values[min_index]:
                min_index = j
        #If the smallest value isn't already in the right place, swap it.
        if min_index != i:
            values[i], values[min_index] = values[min_index], values[i]
            swaps += 1
    #Return the sorted list, # of loops, and # of swaps.
    return values, loops, swaps
