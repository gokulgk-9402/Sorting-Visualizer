# Sorting-Visualizer
 
This is a simple sorting visualizer made using the python module pygame. 50 numbers are randomly generated in the range 0 to 100. And they are sorted using various algorithms like bubble sort, insertion sort, merge sort, quick sort, selection sort and shell sort.

I have tried my best to properly visualize them, but for merge sort its hard because the array isn't being modified in place till the helper function ends. So only the part of the array that is being sorted right now is shown (along with its right, left subarrays in red and blue)

Mostly whenever a swap happens, the bars to be swapped are colored with green and red.

For quick sort, the pivot is taken to be the last element in this program. The pivot is colored with yellow in each call to the function.

The time taken for the sorting algorithms are measured and then printed at the last. Mind you, I have kept a 0.02 second delay wherever I thought necessary, as the code always completed too fast and there wasn't enough time to properly visualize. If you want it to run slower, you can increase that sleep duration. Mostly I have kept sleep, whenever a comparison happens.

We can see insertion and bubble sort are the slowest. While selection sort is happening faster than shell, quick, merge in this case, when the number of elements of the list increases, it becomes far slower as its time complexity is O(n^2).

Upon pressing R key in the keyboard, when the sorting is not happening, the numbers are reset, everything is reset.

Upon pressing spacebar key in the keyboard, the sorting starts. Each sorting algorithm works on a different single thread. And that particular thread generates a pygame surface (bars denoting the numbers) which are then blit into the main pygame window. 

Merge, Quick, Shell sort could've been way faster if I had used multi-threading within them, one thread for left, right in merge, right, left sub array of pivot for quick sort and different threads for different gaps in shell sort, but to stay fair for insertion, selection, bubble, and to keep the code quite simple, I haven't done that.

To run the program, just run the file main.py and hit spacebar(to start the sorting) or R(to re-generate the list of numbers).

Feel free to let me know your thoughts about the code @ gk#9402 (Discord).