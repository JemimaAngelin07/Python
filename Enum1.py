from enum import Enum
class country(Enum):
    America=100
    Africa=400
    Canda=300
    Pairs=700
    Isral=600
for data in country:
    print('{:15}={}'.format(data.name,data.value))   