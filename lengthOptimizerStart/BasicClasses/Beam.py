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
        self.cuttingLength = 5.0

    def can_add_current_segment(self, segment_to_add) -> bool:
        if isinstance(segment_to_add, BeamSegment):
            container_length = self.get_length()
            inc_lengt = self.included_segment_legth_sum()
            if (inc_lengt + segment_to_add.get_length()) <= container_length:
                return True
            else:
                return False

    def add_segment(self, segment_to_add) -> bool:
        if isinstance(segment_to_add, BeamSegment):
            if self.can_add_current_segment(segment_to_add):
                self.beamSegments.append(segment_to_add)
                print("added segment with length: " + str(segment_to_add._length))
                return True
            else:
                print("cannot add segment")
                return False
        else:
            return False

    def included_segment_legth_sum(self) -> float:
        element_sum = 0.0
        for bs in self.beamSegments:
            element_sum += bs.get_length() + self.cuttingLength
        print("current segment length sum:" + str(element_sum))
        return element_sum


if __name__ == "__main__":
    a = BeamSegment(100)
    print(a.get_length)

    b = BeamSegment(10)
    print(b.get_length)

    container = BeamContainer(5000)
    print(container.get_length)
    container.add_segment(a)
    container.add_segment(b)

    print(container.included_segment_legth_sum())
