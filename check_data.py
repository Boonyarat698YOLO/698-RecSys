import pickle

try:
    # Load the data
    with open('recommendation_data.pkl', 'rb') as f:
        data = pickle.load(f)

    print(f"Data type: {type(data)}")
    
    if isinstance(data, dict):
        print("Keys in data:", list(data.keys()))
        print("\nData info:")
        for key, value in data.items():
            print(f"{key}: type {type(value)}")
            if hasattr(value, 'shape'):
                print(f"  Shape: {value.shape}")
            if hasattr(value, '__len__'):
                print(f"  Length: {len(value)}")
            print("-" * 50)
    
    elif isinstance(data, list):
        print(f"List length: {len(data)}")
        print("\nList items:")
        for i, item in enumerate(data):
            print(f"Item {i}: type {type(item)}")
            if hasattr(item, 'shape'):
                print(f"  Shape: {item.shape}")
            if hasattr(item, '__len__'):
                print(f"  Length: {len(item)}")
            if hasattr(item, 'index'):
                print(f"  Index sample: {list(item.index)[:5] if len(item.index) > 5 else list(item.index)}")
            if hasattr(item, 'columns'):
                print(f"  Columns sample: {list(item.columns)[:5] if len(item.columns) > 5 else list(item.columns)}")
            print("-" * 50)
    
    else:
        print(f"Unsupported data type: {type(data)}")
        print("First few characters of data:", str(data)[:200])
        
except Exception as e:
    print(f"Error loading data: {e}")
    print("Make sure recommendation_data.pkl exists in the current directory")