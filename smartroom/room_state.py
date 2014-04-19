class RoomState(object):
    def __init__(self, seats, bounds):
        self.seats = seats
        self.bounds = bounds
  
    def size(self):
        return len(self.seats)

    def __str__(self):
        return str(self.seats)
  
