from dateutil import parser

def extract_date_from_text(text):
    try:
        # Parse the date from the text
        parsed_date = parser.parse(text, fuzzy=True)

        # Return the parsed date
        return parsed_date

    except ValueError as e:
        print(f"Error parsing date: {e}")
        return None

