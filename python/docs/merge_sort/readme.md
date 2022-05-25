# Merge Sort

## Start with this list
lst = [8, 4, 23, 42, 16, 15]

## Split list in to two halves
left side: [8, 4, 23]
right side: [42, 16, 15]


merge_sort(left side: [8])
right side: [4, 23]

Sorted List: [8]

left side: [4]
right side: [23]

Sorted List: [4]
Sorted List: [23]

append remaining entry left 23
Sorted List: [4, 23]

## Left side is sorted
append remaining entry left 23
Sorted List: [4, 8, 23]

left side: [42]
right side: [16, 15]

Sorted List: [42]

left side: [16]
right side: [15]

Sorted List: [16]
Sorted List: [15]

append remaining entry right 16
Sorted List: [15, 16]

## Right side is sorted
append remaining entry right 42
Sorted List: [15, 16, 42]

## Finally we arrive at the sorted list
append remaining entry right 42
Sorted List: [4, 8, 15, 16, 23, 42]
