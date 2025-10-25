#Kevin Perez-Morales
#10/24/25
#Bubble sort function; sorts numbers by repeatedly swapping with neighboring values that are out of order.

def bubble_sort(values):
    print("\nUsing Bubble Sort...")
    loops = 0 #Counts total times the loops runs.
    swaps = 0 #Counts how many swaps happen.

    #A loop repeats enough times to go through all values.
    for i in range(len(values) - 1):
        loops += 1  # count this loop
        #Compares pairs values next to each other.
        for j in range(len(values) - i - 1):
            loops += 1
            #If the current value is greater than the next one then swap their positons.
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swaps += 1
    #Return the sorted list, # of loops, and # of swaps.
    return values, loops, swaps
