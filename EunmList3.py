from enum import IntEnum
class country(IntEnum):
    America=100
    Africa=400
    Canda=300
    Pairs=700
    Isral=600
country_code_list=list(map(int,country))
print(country_code_list)    