# for sum approach 1 brute force 2 using hashmap 3 using two pointer
# what is brute force approach check every pair if sum is equal to target
# hashmap approach store the difference of target and current element in hashmap and check if current element is in hashmap
# hashmap example {target-nums[i]:i}

def hashmap_debug_example():
    """
    This function demonstrates how hashing works for dictionary keys in Python.
    It creates a dictionary (hash map) and prints each key along with its hash value.
    """
    # Create a dictionary with person's information
    person = {
        "name": "mom",
        "age": 20,
        "city": "delhi",
        "phone": 858456586854
    }

    # Iterate through each key in the dictionary
    # For each key, print the key itself, its hash value, and the corresponding value
    for key in person:
        print(f"Key: {key}, Hash: {hash(key)}, Value: {person[key]}")


hashmap_debug_example()

def _2sum(tar, num, self):
    hashmap = {}
    for i