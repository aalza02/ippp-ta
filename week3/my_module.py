print("Imported my module...")
test = "Test String"

def find_index(to_search, target):
    """Find the index of a value in a sequence"""
    for i, val in enumerate(to_search):
        if val == target:
            return i
        
    return -1