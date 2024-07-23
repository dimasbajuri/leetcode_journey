import pandas as pd

numbers = [1, 2, 1, 5, 6, 7, 5, 2]

def kemunculan(list, target):
    
    hash_map = {}

    for item in numbers:
        if item in hash_map:
            hash_map[item] += 1
        else:
            hash_map[item] = 1
    
    df = pd.Series(hash_map)

    print(df)

    if target in hash_map:
        print(f"ada {hash_map[target]} {target}")
    else:
        print(f"tidak ada {target} dalam list")

kemunculan(numbers, 3)