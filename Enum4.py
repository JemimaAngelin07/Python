import enum
class country(enum.Enum):
     America=100
     Africa=400
     Canda=300
     Pairs=700
     Isral=600
for result in country:
     print('{:15}={}'.format(result.name,result.value))