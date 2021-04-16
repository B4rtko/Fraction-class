# Bartosz Różycki
# nr indeksu: 255740

class Fraction:
    """Class describes objects that can be interpreted as an fraction and contains some of their properties"""
    float_allowed = True
    display = "improper"  # ["improper", "mixed"]

    def __init__(self, num, denom):
        """
        :param num: if Fraction.float_allowed bool is False - int; otherwise int, float or Fraction
        :param denom: if Fraction.float_allowed bool is False - int; otherwise int, float or Fraction
        """
        self.num, self.denom = self.data_check(num, denom)
        self.simple_state()

    def __str__(self):
        """
        depends on Fraction.display parameter, function returns mixed or improper display of fraction
        :return: fraction display; str
        """
        if Fraction.display == "improper":
            return f"{self.get_num()}/{self.get_denom()}"
        elif Fraction.display == "mixed":
            m = self.get_num() // self.get_denom()
            if m == 0:
                return f"{self.get_num()}/{self.get_denom()}"
            else:
                n = self.get_num() - m*self.get_denom()
                if n == 0:
                    return f"{m}"
                else:
                    return f"{m}, {n}/{self.get_denom()}"

    def __add__(self, other):
        """
        operations for adding element to fraction
        :param other: int, float or other fraction
        :return: result as fraction
        """
        copied = self.__copy__()
        if type(other) in [int, float]:
            copied.num += other*copied.get_denom()
        elif type(other) == Fraction:
            copied.num = copied.get_num()*other.get_denom() + other.get_num()*copied.get_denom()
            copied.denom *= other.get_denom()
        else:
            raise TypeError(f"Cannot add {type(other)} to fraction.")
        copied.simple_state()
        return copied

    def __sub__(self, other):
        """
        operations for subtraction element from fraction
        :param other: int, float or other fraction
        :return: result as fraction
        """
        copied = self.__copy__()
        if type(other) in [int, float]:
            copied.num -= other*copied.get_denom()
        elif type(other) == Fraction:
            copied.num = copied.get_num()*other.get_denom() - other.get_num()*copied.get_denom()
            copied.denom *= other.get_denom()
        else:
            raise TypeError(f"Cannot subtract {type(other)} from fraction.")
        copied.simple_state()
        return copied

    def __mul__(self, other):
        """
        operations for multiplying fraction by element
        :param other: int, float or other fraction
        :return: result as fraction
        """
        copied = self.__copy__()
        if type(other) in [int, float]:
            copied.num *= other
        elif type(other) == Fraction:
            copied.num *= other.get_num()
            copied.denom *= other.get_denom()
        else:
            raise TypeError(f"Cannot multiply {type(other)} and fraction.")
        copied.simple_state()
        return copied

    def __truediv__(self, other):
        """
        operations for dividing fraction by element
        :param other: int, float or other fraction
        :return: result as fraction
        """
        copied = self.__copy__()
        if type(other) in [int, float]:
            if other == 0:
                raise ZeroDivisionError
            copied.denom *= other
        elif type(other) == Fraction:
            if other.num == 0:
                raise ZeroDivisionError
            copied.num *= other.get_denom()
            copied.denom *= other.get_num()
        else:
            raise TypeError(f"Cannot divide fraction by {type(other)}.")
        copied.simple_state()
        return copied

    def __radd__(self, other):
        """
        operations for adding fraction to element
        :param other: int, float or other fraction
        :return: result as fraction
        """
        copied = self.__copy__()
        if type(other) in [int, float]:
            copied.num += other*copied.get_denom()
        else:
            raise TypeError(f"Cannot add fraction to {type(other)}.")
        copied.simple_state()
        return copied

    def __rsub__(self, other):
        """
        operations for subtracting fraction from element
        :param other: int, float or other fraction
        :return: result as fraction
        """
        copied = self.__copy__()
        if type(other) in [int, float]:
            copied.num = other*copied.get_denom() - copied.get_num()
        else:
            raise TypeError(f"Cannot sub fraction from {type(other)}.")
        copied.simple_state()
        return copied

    def __rmul__(self, other):
        """
        operations for multiplying element by fraction
        :param other: int, float or other fraction
        :return: result as fraction
        """
        copied = self.__copy__()
        if type(other) in [int, float]:
            copied.num *= other
        else:
            raise TypeError(f"Cannot multiply fraction and {type(other)}.")
        copied.simple_state()
        return copied

    def __rtruediv__(self, other):
        """
        operations for dividing element by fraction
        :param other: int, float or other fraction
        :return: result as fraction
        """
        copied = self.__copy__()
        if type(other) in [int, float]:
            if other == 0:
                raise ZeroDivisionError
            copied.denom *= other
            copied.num, copied.denom = copied.get_denom(), copied.get_num()
        else:
            raise TypeError(f"Cannot divide {type(other)} by fraction.")
        copied.simple_state()
        return copied

    def __copy__(self):
        return Fraction(self.get_num(), self.get_denom())

    def __abs__(self):
        return Fraction(abs(self.get_num()), self.get_denom())

    def __eq__(self, other):
        if type(other) == Fraction:
            return float(self) == float(other)
        elif type(other) in [int, float]:
            return float(self) == other
        else:
            return False

    def __lt__(self, other):
        if type(other) == Fraction:
            return float(self) < float(other)
        elif type(other) in [int, float]:
            return float(self) < other
        else:
            raise TypeError(f"'<' not supported between instances of 'Fraction' and '{type(other)}'.")

    def __le__(self, other):
        if type(other) == Fraction:
            return float(self) <= float(other)
        elif type(other) in [int, float]:
            return float(self) <= other
        else:
            raise TypeError(f"'<=' not supported between instances of 'Fraction' and '{type(other)}'.")

    def __gt__(self, other):
        if type(other) == Fraction:
            return float(self) > float(other)
        elif type(other) in [int, float]:
            return float(self) > other
        else:
            raise TypeError(f"'>' not supported between instances of 'Fraction' and '{type(other)}'.")

    def __ge__(self, other):
        if type(other) == Fraction:
            return float(self) >= float(other)
        elif type(other) in [int, float]:
            return float(self) >= other
        else:
            raise TypeError(f"'>=' not supported between instances of 'Fraction' and '{type(other)}'.")

    def __float__(self):
        return self.get_num()/self.get_denom()

    def __int__(self):
        return int(self.get_num()/self.get_denom())

    def float_allow(self):
        Fraction.float_allowed = True

    def float_disallow(self):
        Fraction.float_allowed = False

    def display_improper(self):
        Fraction.display = "improper"

    def display_mixed(self):
        Fraction.display = "mixed"
        # dekorator klas metod

    def get_num(self):
        return self.num

    def get_denom(self):
        return self.denom

    def data_check(self, n, d):
        """
        function is called from init and checks if given parameters are acceptable to create fraction. Features are
            different depends on Fraction.float_allowed bool
        :param n: if Fraction.float_allowed bool is False - int; otherwise int, float or Fraction
        :param d: if Fraction.float_allowed bool is False - int; otherwise int, float or Fraction
        :return: checked n and d parameters in tuple
        """
        n_checked, d_checked = False, False
        if type(n) == int:
            n_checked = True
        if type(d) == int and d != 0:
            d_checked = True
        if Fraction.float_allowed:
            if type(n) == float:
                n_checked = True
            if type(d) == float and d != 0.0:
                d_checked = True
            if type(n) == Fraction:
                d = Fraction(d.get_num(), d.get_denom())*n.get_denom()
                n = n.get_num()
                n_checked = True
            if type(d) == Fraction:
                if d.num in [0, 0.0] or d.denom in [0, 0.0]:
                    raise ZeroDivisionError
                n, d = n*d.get_denom(), d.get_num()
                d_checked = True
        if n_checked and d_checked:
            return n, d
        else:
            raise Exception("cannot create Fraction object for given parameters. Check if Fraction.float_allowed bool"
                            "is set to True. If not, use [fraction_object].float_allow() method.")

    def simple_state(self):
        """
        function is responsible for transforming fraction to its simplest form
        :return: None (function sets object's parameters)
        """
        # metoda prywatna/ publiczna
        if self.get_num() == 0:  # doesn't need to simplify if it equals 0
            self.num = 0
            self.denom = 1
            return None
        sign = 1  # simplify algorithms were simpler to write in case where we didn't bother if fraction is negative or positive
        if self.get_num()*self.get_denom() < 0:
            sign = -1
        self.num, self.denom = abs(self.get_num()), abs(self.get_denom())  # because we saved negativity to sign variable
        self.float_to_int()  # other method
        factors_num = self.prime_factors(self.get_num())  # other method
        factors_denom = self.prime_factors(self.get_denom())  # other method
        factors_num_loop = factors_num.copy()
        for i in factors_num_loop:  # removes same prime factors from numerator and denominator
            for j in factors_denom:
                if i == j:
                    factors_num.remove(i)
                    factors_denom.remove(j)
                    break
        self.num = sign  # put everything back together
        self.denom = 1
        for i in factors_num:
            self.num *= i
        for i in factors_denom:
            self.denom *= i
        return None

    def prime_factors(self, n):
        """
        simple function to get number to its prime factors. Dedicated for positive int. Function that uses this func
            needs to check arguments.
        :param n: positive int
        :return: list of prime factors
        """
        factors = []
        for i in range(1,n+1):
            if n ==1:
                break
            if i == 1:  # its made just not to crush function if it tries to calculate prime factors of 1
                continue
            while n%i == 0:
                factors.append(i)
                n /= i
        return factors

    def float_to_int(self):
        """
        function checks if numerator and denominator are integers. If not, transforms them.
        :return: None (function sets object's parameters)
        """
        num_mul = 0
        den_mul = 0
        num = self.get_num()
        den = self.get_denom()
        while num != num//1:
            num *= 10
            num_mul += 1
        while den != den//1:
            den *= 10
            den_mul += 1
        if num_mul > den_mul:
            self.num *= 10**num_mul
            self.denom *= 10**num_mul
            self.num, self.denom = int(self.get_num()), int(self.get_denom())

        else:
            self.num *= 10**den_mul
            self.denom *= 10**den_mul
            self.num, self.denom = int(self.get_num()), int(self.get_denom())
        return None



