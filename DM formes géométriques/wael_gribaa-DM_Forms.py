import math


class Shape:
    """
    Some abstract shape.
    """

    def diagonal(self):
        """
        Calculates and returns the diagonal of the current Shape.
        The diagonal of a disk is its diameter.
        :return: The diagonal as a number.
        """
        pass

    def perimeter(self):
        """
        Calculates and returns the perimeter of the current Shape.
        :return: The perimeter as an number.
        """
        pass

    def area(self):
        """
        Calculates and returns the area of the current Shape.
        The Circle has no area (zero).
        :return: Area as a number.
        """
        pass

    def min_dimension(self):
        """
        Returns the minimal dimension of a shape. Useful to know if a polygon can fit inside a Disk.
        :return: Diameter if it's a disk, width if it's a rectangle, as an number.
        """
        pass

    def can_fit_inside(self, shape_to_fit_within):
        """
        Calculates if the current Shape fits within another instance of Shape.
        :param shape_to_fit_within: The other Shape to check if the current Shape fits within.
        :return: True if the current Shape fits within, False otherwise.
        """
        pass

    def can_contain(self, shape_to_contain):
        """
        Calculates if another Shape can fit within the current Shape.
        :param shape_to_contain: The other Shape to try to fit within the current Shape.
        :return: True if shape_to_contain fits within, False otherwise.
        """
        return shape_to_contain.can_fit_inside(self)

    def __str__(self):
        return 'A Shape which should not be instantiable, but it\'s Python... right ?'


class Rectangle(Shape):
    """
    A Rectangle characterized by a length and a width.
    """

    def __init__(self, length, width):
        if length < 0 or width < 0:
            raise ValueError('Lengths must be positive.')
        length = length
        width = width
        self.length = max(length, width)
        self.width = min(width, length)

    def perimeter(self):
        return self.length * 2 + self.width * 2

    def area(self):
        return self.length * self.width

    def diagonal(self):
        return math.sqrt(self.width ** 2 + self.length ** 2)

    def min_dimension(self):
        return self.width

    def can_fit_inside(self, shape_to_fit_within):
        basic_test = self.area() <= shape_to_fit_within.area() and self.diagonal() <= shape_to_fit_within.diagonal()
        if not basic_test or not isinstance(shape_to_fit_within, Rectangle):
            return basic_test
        else:
            # If it enters here, it means that the Rectangle (or Square) might fit inside shape_to_fit_within or not.
            # If one width or the length of the current Rectangle is greater than the width or the length (respectively)
            # of the shape_to_fit_within, then the only way to know is by doing more complex calculations.
            # sq_hyp is the diagonal squared. We already checked that the diagonal of the container was greater than the
            # diagonal of the current Shape ; if the largest length of the container is greater than the diagonal
            # of the current Shape, then it cannot fit because of the width, without the need to do the remaining
            # calculations.
            l1 = shape_to_fit_within.length
            w1 = shape_to_fit_within.width
            l2 = self.length
            w2 = self.width
            if l2 <= l1 and w2 <= w1:
                return True
            sq_hyp = l2 ** 2 + w2 ** 2
            return l1 ** 2 < sq_hyp and \
                w2 ** 2 <= -w1 * math.sqrt(-l1 ** 2 + sq_hyp) - l1 * math.sqrt(-w1 ** 2 + sq_hyp) + l2 ** 2

    def __str__(self):
        return 'A Rectangle of length = '+str(self.length)+' and width = '+str(self.width)


class Square(Rectangle):
    """
    A Square as a Rectangle of width = length.
    """

    def __init__(self, length):
        super().__init__(length, length)

    def __str__(self):
        return 'A Square of length = '+str(self.length)


class Disc(Shape):
    """
    A Disc characterized by a radius.
    """

    def __init__(self, radius):
        if radius < 0:
            raise ValueError('Lengths must be positive.')
        self.radius = radius

    def perimeter(self):
        return self.radius * 2 * math.pi

    def area(self):
        return self.radius ** 2 * math.pi

    def diagonal(self):
        return self.radius * 2

    def min_dimension(self):
        return self.diagonal()

    def can_fit_inside(self, shape_to_fit_within):
        # The smaller dimension of the other Shape (the width or the diameter), compared to the diameter of the current
        # Disk, will easily tell if it can fit inside.
        # A Circle can be inscribed within any other Shape, but cannot be inscribed by any, since it has no area.
        return self.diagonal() <= shape_to_fit_within.min_dimension()

    def __str__(self):
        return 'A Disc of radius = '+str(self.radius)


class Circle(Disc):
    """
    A Circle as a Disc of area = 0.
    """

    def __init__(self, radius):
        super().__init__(radius)

    def area(self):
        return 0

    def min_dimension(self):
        return 0

    def __str__(self):
        return 'A Circle of radius = '+str(self.radius)


rect1 = Rectangle(0.525, 4)
print(rect1)
print('Area = '+str(rect1.area()))
print('Perimeter = '+str(rect1.perimeter()))

rect2 = Rectangle(3.21, 3.2)
print(rect2)
print('Area = '+str(rect2.area()))
print('Perimeter = '+str(rect2.perimeter()))

sq1 = Square(3.2)
print(sq1)
print('Area = '+str(sq1.area()))
print('Perimeter = '+str(sq1.perimeter()))

c1 = Circle(0.5)
print(c1)
print('Area = '+str(c1.area()))
print('Perimeter = '+str(c1.perimeter()))

d1 = Disc(0.5)
print(d1)
print('Area = '+str(d1.area()))
print('Perimeter = '+str(d1.perimeter()))

print(rect1.can_fit_inside(rect2))
# print(rect2.can_contain(rect1))
print(rect2.can_fit_inside(rect1))
# print(rect1.can_contain(rect2))

print(rect1.can_fit_inside(sq1))
# print(sq1.can_contain(rect1))
print(sq1.can_fit_inside(rect1))
# print(rect1.can_contain(sq1))

print(d1.can_fit_inside(sq1))
# print(sq1.can_contain(d1))
print(sq1.can_fit_inside(d1))
# print(d1.can_contain(sq1))

print(c1.can_fit_inside(rect1))
# print(rect1.can_contain(c1))
print(rect1.can_fit_inside(c1))
# print(c1.can_contain(rect1))

print(d1.can_fit_inside(c1))
# print(c1.can_contain(d1))
print(c1.can_fit_inside(d1))
# print(d1.can_contain(c1))
