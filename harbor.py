from utils import get_category as get_size
from utils import exponential, Event, normal, mean, bublle_sort_last

class Harbor:
    '''
    Harbor scope to manage
    arrivals and departures events
    '''
    def __init__(self, n, docks):
        self.n = n
        self.time = 0
        self.ship = 0
        self.count = 0
        self.events = []
        self.bussy = False
        self.docks = docks
        self.size = [0] * n
        self.arrivals = [0] * n
        self.departures = [0] * n
        self.prob = [0.25, 0.25, 0.5]
        self.cargo_params = [(9, 1), (12, 2), (18, 3)]
        self.iddle()
        
    def arrive(self):
        '''
        Generate a new arrival
        '''
        if self.count != self.n:
            time = self.time + exponential(8) * 60
            e = Event(time, self.count, self.enque)
            self.count += 1
            self.events.append(e)
        return True

    def enque(self, e):
        '''
        Enque a new ship that just arrived
        '''
        size = get_size(self.prob)
        self.size[e.details] = size
        self.arrivals[e.details] = e.time
        self.time = max(self.time, e.time)
        #TODO: Notify an arrival
        self.events.append(Event(self.time, e.details, self.move))
        bublle_sort_last(self.events)
        return self.arrive()

    def move(self, e):
        '''
        Move a ship to a dock
        '''
        if (self.docks == 0) or self.bussy:
            return False
        #TODO: Notify that a ship is been atended
        self.go(1)
        self.bussy = True
        time = self.time + exponential(2) * 60
        self.events.append(Event(time, e.details, self.dock))
        return True

    def dock(self, e):
        '''
        Start load the cargo of a ship
        '''
        #TODO: Notify that a ship starts to load its cargo
        self.time = max(self.time, e.time)
        self.docks -= 1
        self.bussy = False
        time = self.load_time(self.size[e.details])
        self.events.append(Event(time, e.details, self.ready))
        return True

    def ready(self, e):
        '''
        Finish to load the ship cargo
        and wait for it's departure
        '''
        #TODO: Notify that a ship finsih of load his cargo
        self.time = max(self.time, e.time)
        self.events.append(Event(self.time, e.details, self.depart))
        return True

    def depart(self, e):
        '''
        Move a ship out of the docks
        '''
        if self.bussy:
            return False
        #TODO: Notify that a ship is abandoning its dock
        self.go(0)
        self.docks += 1
        self.bussy = True
        time = self.time + exponential(1) * 60
        self.events.append(Event(time, e.details, self.done))
        return True

    def done(self, e):
        '''
        Finish to service a ship
        '''
        #TODO: Notify that a ship is abandoning the harbor
        self.bussy = False
        self.time = max(self.time, e.time)
        self.departures[e.details] = self.time
        return True          

    def go(self, pos):
        '''
        Move the tug to <pos>.
        1 implies the docks,
        0 implies the port.
        '''
        if pos != self.ship:
            self.time += exponential(15)
        self.ship = 1 - pos

    def load_time(self, id):
        '''
        Return the ship number <id>
        load cargo requiered time
        '''
        u, o = self.cargo_params[id]
        return self.time + normal(u, o) * 60

    def elapsed(self, id):
        '''
        Return the time elapsed
        between the ship <id>
        arrival and departure
        '''
        return self.departures[id] - self.arrivals[id]

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
                    bublle_sort_last(self.events)
                    break
        #TODO: Notify that the harbor finish its service


def main(args):
    elapsed = []
    for _ in range(args.tries):
        harbor = Harbor(args.amount, args.docks)
        elapsed.extend([harbor.elapsed(i) / 60 for i in range(args.amount)])
    ev = mean(elapsed)
    #TODO: Show the mean
    return ev

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Harbor simulator')
    parser.add_argument('-d', '--docks', type=int, default=3, help='number of harbor docks')
    parser.add_argument('-a', '--amount', type=int, default=3, help='number of ships to attend')
    parser.add_argument('-t', '--tries', type=int, default=10, help='number of harbor simulations')

    args = parser.parse_args()
    main(args)