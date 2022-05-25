# Blog Notes: Insertion Sort

    InsertionSort(int[] arr)

      FOR i = 1 to arr.length

        int j <-- i - 1
        int temp <-- arr[i]

        WHILE j >= 0 AND temp < arr[j]
          arr[j + 1] <-- arr[j]
          j <-- j - 1

        arr[j + 1] <-- temp


Sample Arrays

In your blog article, visually show the output of processing this input array:

    [8,4,23,42,16,15]

For your own understanding, consider also stepping through these inputs:

    Reverse-sorted: [20,18,12,8,5,-2]
    Few uniques: [5,12,7,5,5,7]
    Nearly-sorted: [2,3,5,7,13,11]
