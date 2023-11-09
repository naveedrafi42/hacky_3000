def extract_first_name(full_name):
    # Ensure the full name is a string before splitting
    full_name = str(full_name)
    # Split the full name into words using whitespace as the separator
    name_parts = full_name.split()

    # Check if there are any words in the full name
    if len(name_parts) > 0:
        # The first word is the first name
        first_name = name_parts[0]
        return first_name
    else:
        # If there are no words return an empty string
        return ""


def another_function(notrelated):
    return