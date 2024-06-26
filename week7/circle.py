class Circle:

    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        circ = self.diameter * self.__pi
        return circ

    def calculate_area(self):
        area = self.__pi * ((self.diameter / 2) ** 2)
        return area

    def calculate_area_of_sector(self, angle):
        area_sector = (angle / 360) * self.__pi * (self.diameter/2) ** 2
        return area_sector
