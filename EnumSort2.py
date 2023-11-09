from enum import Enum
class country(Enum):
    America=100
    Africa=400
    Canda=300
    Pairs=700
    Isral=600
print("Country name ordered by Country Code:")
print('\n '.join(' ' + c.name for c in sorted(country)))    