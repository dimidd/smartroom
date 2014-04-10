class RoomState(object):
    def __init__(self, seats):
        self.seats = seats
  
    def size(self):
        return len(self.seats)

    def __str__(self):
        return str(self.seats)
  
