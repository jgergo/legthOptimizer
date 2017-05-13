from math import sin


class Beam:
    def __init__(self, length):
        self._length = length

    def get_length(self):
        return self._length
    

class BeamSegment(Beam):
    def __init__(self, length):
        super().__init__(length)


class BeamContainer(Beam):
    def __init__(self, length):
        super().__init__(length)
        self.beamSegments = []

    def can_add_current_segment(self, segment_to_add) -> bool:
        pass


    def add_segment(self, segment_to_add):
        if isinstance(segment_to_add, BeamSegment):
            self.beamSegments.append(segment_to_add)
            print("added segment with length: " + str(segment_to_add._length))

    def included_segment_legth_sum(self) -> float:
        sum = 0.0
        for bs in self.beamSegments:
            sum += bs.get_length
        return sum


if __name__ == "__main__":

    a = BeamSegment(100)
    print(a.get_length)

    b = BeamSegment(10)
    print(b.get_length)

    containter = BeamContainer(5000)
    print(containter.get_length)
    containter.add_segment(a)
    containter.add_segment(b)

    print(containter.included_segment_legth_sum())


