COUNTINGSORT

- Linear time sorting algorithm 
- Counts number of occurences of each element in the array, stores in auxillary array
- Uses count to dispatch elements from input array to output array


Time Complexity: O(n + k), usually k = O(n) so O(n)

Advantages:
Sorts stably. 
Does not use comparisons, giving it the ability to sort in linear time.
Good at sorting small integers with multiple counts.

Disadvantages:
Not very efficient when integers in input are very large, lots of unneeded space used.
Cannot sort floats.
Uses auxillary memory.


Alogorithm:

def counting_sort(A, k):
    B = [0] * len(A)
    C = [0] * (k+1)

    for i in range(0, len(A)):
        C[A[i]] += 1

    for i in range(1, k+1):
        C[i] = C[i] + C[i - 1]

    for i in range(len(A)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
        
    return B
