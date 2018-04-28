
import math


class Digit():

    def __init__(self, value):
        assert isinstance(value, int)
        self.value = value

    def right(self, pos):
        assert pos > 0
        assert pos <= self.int_len()
        return self.value // 10**(pos - 1) % 10

    def last(self):
        return self.right(1)

    def int_len(self):
        return int(math.log10(self.value)) + 1

    def first(self):
        return self.right(self.int_len())

    def left_digits(self, ndigits):
        assert ndigits > 0 and ndigits <= self.int_len()
        return self.value / (10 ** (self.int_len() - ndigits))

    def higher_zero(self):
        assert self.value >= 0
        return 10 * (self.value / 10 + 1)

    def char_sum(self):
        return sum([self.right(i) for i in range(1, self.int_len()+1)])


class NPI():

    def __init__(self, input_id):
        self.id = Digit(input_id)

    def validate_input(self):
        self.first_one_two(self.id),
        self.correct_length(self.id)

    @staticmethod
    def correct_length(uid):
        assert uid.int_len() == 10

    @staticmethod
    def first_one_two(uid):
        first = uid.first()
        assert first == 1 or first == 2

    @staticmethod
    def list_to_int(int_list):
        return int("".join([str(i) for i in int_list]))

    def double_alternate(self, uid):
        return self.list_to_int(
            [uid.right(i) * 2 for i in range(1,uid.int_len(),2)])

    def non_alternate(self, uid):
        return self.list_to_int([uid.right(i)
                                 for i in range(2,uid.int_len()+1,2)])

    def luhn(self):
        validation = Digit(self.id.left_digits(9))
        checksum = Digit(80840 * 10 ** validation.int_len() + validation.value)
        non_alt = self.non_alternate(checksum)
        alt = self.double_alternate(checksum)
        total = Digit(alt).char_sum() + Digit(non_alt).char_sum()
        return Digit(total).higher_zero() - total == self.id.last()


n = NPI(1234567893)
n.validate_input()
n.luhn()

1356320139
1285849489
1265795159
1922087766
1932224400
1467538918
1861414096
1528142197
1306070885
141799038
1144258609
1467446575
1285652024
1104084334
144750284
1356585673
1740232941
1992776843
1215965934
1154348176







