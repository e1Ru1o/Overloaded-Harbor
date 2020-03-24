from utils import get_category as get_size
from utils import exponential, Event, normal, mean

class Harbor:
    '''
    Harbor scope to manage
    arrivals and departures events
    '''
    def __init__(self, n, docks):
        self.n = n
        self.time = 0
        self.docks = docks
        self.events = []
        self.iddle()
    
    def arrive(self):
        '''
        Generate a new arrival
        '''
        return True

    def enque(self, e):
        '''
        Enque a new ship that just arrived
        '''
        return True

    def move(self, e):
        '''
        Move a ship to a dock
        '''
        return True

    def dock(self, e):
        '''
        Start load the cargo of a ship
        '''
        return True

    def ready(self, e):
        '''
        Finish to load the ship cargo
        and wait for it's departure
        '''
        return True

    def depart(self, e):
        '''
        Move a ship out of the docks
        '''
        return True

    def done(self, e):
        '''
        Finish to service a ship
        '''
        return True        

    def go(self, pos):
        '''
        Move the tug to <pos>.
        1 implies the docks,
        0 implies the port.
        '''
        pass

    def load_time(self, id):
        '''
        Return the ship number <id>
        load cargo requiered time
        '''
        return self.time

    def elapsed(self, id):
        '''
        Return the time elapsed
        between the ship <id>
        arrival and departure
        '''
        return 0

    def iddle(self):
        '''
        Simulate the harbor
        '''
        self.arrive()
        while self.events:
            for i in range(len(self.events)):
                e = self.events[i]
                if e.callback(e):
                    self.events.pop(i)
                    break
        #TODO: Notify that the harbor finish its service


def simulate(args):
    harbor = Harbor(args.amount, args.docks)
    elapsed = [harbor.elapsed(i) for i in range(args.amount)]
    ev = mean(elapsed)
    #TODO: Show the mean
    return ev

