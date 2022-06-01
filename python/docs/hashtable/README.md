# Hashtable
## Challenge
Implement a Hashtable Class with the following methods:

      set
      get
      contains
      keys
      hash


## Approach & Efficiency
The efficiency for the hash table as a whole is O(n) where n is the size of the list

## API
      set
          Arguments: key, value
          Returns: nothing
          This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
          Should a given key already exist, replace its value from the value argument given to this method.
      get
          Arguments: key
          Returns: Value associated with that key in the table
      contains
          Arguments: key
          Returns: Boolean, indicating if the key exists in the table already.
      keys
          Returns: Collection of keys
      hash
          Arguments: key
          Returns: Index in the collection for that key

## [Code](/python/data_structures/hashtable.py)

## Resources
Eden showed her code in class and I referenced it
