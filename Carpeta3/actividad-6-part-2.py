class Dinglemouse:
    def __init__(self, queues, capacity):
        self.queues = [list(q) for q in queues]
        self.capacity = capacity

    def theLift(self):
        queues = self.queues
        capacity = self.capacity
        floors = len(queues)
        elevator = []
        stops = [0]
        current = 0
        direction = 1

        def do_stop(floor):
            if stops[-1] != floor:
                stops.append(floor)
            # Bajar pasajeros en su destino
            for p in elevator[:]:
                if p == floor:
                    elevator.remove(p)
            # Subir gente que va en la misma dirección
            remaining = []
            for person in queues[floor]:
                if (len(elevator) < capacity and
                        ((direction == 1 and person > floor) or
                         (direction == -1 and person < floor))):
                    elevator.append(person)
                else:
                    remaining.append(person)
            queues[floor] = remaining

        # Determinar si hay trabajo pendiente en una dirección
        def has_work_above(floor):
            if any(p > floor for p in elevator):
                return True
            for f in range(floor + 1, floors):
                if queues[f]:
                    return True
            return False

        def has_work_below(floor):
            if any(p < floor for p in elevator):
                return True
            for f in range(floor):
                if queues[f]:
                    return True
            return False

        while has_work_above(current) or has_work_below(current) or elevator:
            if direction == 1:
                for floor in range(current, floors):
                    need_stop = (floor in elevator or
                                 any(p > floor for p in queues[floor]))
                    if need_stop:
                        do_stop(floor)
                current = floors - 1
                if not has_work_above(current):
                    direction = -1
            else:
                for floor in range(current, -1, -1):
                    need_stop = (floor in elevator or
                                 any(p < floor for p in queues[floor]))
                    if need_stop:
                        do_stop(floor)
                current = 0
                if not has_work_below(current):
                    direction = 1

        if stops[-1] != 0:
            stops.append(0)

        return stops