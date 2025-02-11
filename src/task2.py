def typeBasedTransformer(**kwargs):
    """
    Transforms values based on their types:
    - Numbers (int, float) -> Squared
    - Strings -> Reversed while keeping the case
    - Booleans -> Inverted
    - Lists/Tuples -> Reversed order
    - Dictionaries -> Swaps keys and values
    """
    transformed = {}
    
    for key, value in kwargs.items():
        if isinstance(value, (int, float)):  
            transformed[key] = value ** 2  
        elif isinstance(value, str):  
            transformed[key] = value[::-1]  
        elif isinstance(value, bool):  
            transformed[key] = not value  
        elif isinstance(value, (list, tuple)):  
            transformed[key] = value[::-1]  
        elif isinstance(value, dict):  
            transformed[key] = {v: k for k, v in value.items()}  
        else:
            transformed[key] = value  # Leave unchanged if type not handled
    
    return transformed

if __name__ == "__main__":
    print(typeBasedTransformer(num=4, text="Hello", flag=True, items=[1, 2, 3], mapping={"a": 1, "b": 2}))
