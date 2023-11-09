class Room:
    length=0.0
    breadth=0.0
    def cal_room(self):
        print("Area of Room:",self.length * self.breadth)
study_room=Room()
study_room.length=42.5
study_room.breadth=30.8
study_room.cal_room()