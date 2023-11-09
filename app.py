def is_phone_number(text):
    # Adjusted pattern to include an optional country code like +44
    pattern = re.compile(r'(?:\+\d{1,3})?[-\s]?\(?(?:\d{3})\)?[-\s]?\d{3}[-\s]?\d{4}\b')
    return pattern.match(text) is not None
