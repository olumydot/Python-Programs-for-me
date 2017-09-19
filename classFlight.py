"""Model for aircraft flight"""
from pprint import pprint as pp
class Flight:
    def __init__(self, number, aircraft):# aircraft here is an object of the class Aircraft. thus it will be able to access the methods

        if not number[:2].isalpha():
            raise ValueError("No airline code in {}".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid airline code {}".format(number))
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route numbers {}".format(number))
        # we see that even though its a parameter we still using it as self._number, this is cos its not an object of some
        # class. if it were the object of some class then we need not use self._number
        self._number = number  # see the underscore there? its so we can differentiate it from the function 'number' below
        self._aircraft = aircraft #this is an instance object of the class Aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows] #the for underscore rows is to discard the rows as we do not need them for now

    def number(self):
        return self._number  #observe that though we assigned this previously in he above init class as 'number' but its
    # not an arguement for this function so if we ever wanna use it it must be self._number
    def airline(self):
        return self._number[2:]
    def aircraft_model(self):
        return self._aircraft.model() #here the object instance of Aircraft class is able to access model method
    def allocate_seat(self,seat,passanger):
        rows, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter{}".format(letter))
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))
        if row not in rows:
            raise ValueError("Invalid row number {}".format(row))
        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} is already occupied".format(seat))
        self._seating[row][letter] = passanger


class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration
    def model(self):
        return self._model
    def seating_plan(self):
        return (range(1, self._num_rows + 1) , "ABCDEFGHJK"[self._num_seats_per_row])

a = Aircraft("G-EUPT", "Airbus A310", num_rows = 22, num_seats_per_row = 6)
print(a.model())
print(a.seating_plan())

f = Flight("BA758", aircraft = Aircraft("G-EUPT", "Airbus A310", num_rows = 22, num_seats_per_row = 6)) #we pass the aircraft class directly
print(f._seating)
pp(f._seating)
f.allocate_seat("12B", "Olumide Oni")
f.allocate_seat("12B", "Olumide Oni")
