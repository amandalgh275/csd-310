# city_functions.py - Step 6 (final version)

def city_country(city, country, population='', language=''):
    """Return a formatted string of city and country with optional population and language."""
    if population and language:
        return f"{city.title()}, {country.title()} - population {population}, {language.title()}"
    elif population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"

# Test calls as required - for Step 7 you need to call with 2, 3, and 4 parameters
print("Testing city_country function with different parameters:")
print("1.", city_country('santiago', 'chile'))  # 2 parameters
print("2.", city_country('paris', 'france', '2148000'))  # 3 parameters  
print("3.", city_country('tokyo', 'japan', '13960000', 'japanese'))  # 4 parameters

