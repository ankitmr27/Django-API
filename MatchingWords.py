from difflib import SequenceMatcher
from secret import limit

def similarity_ratio(a, b):
    return SequenceMatcher(None, a, b).ratio()

def find_matching_device(search_query, search_results):
    matching_devices = []

    for device_name in search_results:
        similarity = similarity_ratio(search_query.lower(), device_name.lower())
        if similarity > limit:  # Adjust the threshold as needed
            matching_devices.append((device_name, similarity))

    return matching_devices

# Example usage
# search_query = "realme c2"
# search_results = ["Realme C2", "Realme C2 (3GB)", "Realme C3", "Samsung Galaxy C20"]

# matching_devices = find_matching_device(search_query, search_results)

# if matching_devices:
#     print("Matching Devices:")
#     for device, similarity in matching_devices:
#         print(f"{device} (Similarity: {similarity:.2%})")
# else:
#     print("No matching devices found.")
