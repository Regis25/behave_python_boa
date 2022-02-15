from utils.date_helper import DateHelper


class BookFlight:

    def __init__(self):
        self.book_flight = {
            "from_location": "",
            "to_location": "",
            "select": "",
            "departure_date": "",
            "return_date": "",
            "adults": "",
            "child": "",
            "infant": ""
        }

    def set_book_flight(self, from_location=None, to_location=None, select=None, departure_date=None,
                        return_date=None, adults=None, child=None, infant=None):
        if from_location:
            self.book_flight["from_location"] = from_location
        if to_location:
            self.book_flight["to_location"] = to_location
        if select:
            self.book_flight["select"] = select
        if departure_date:
            self.book_flight["departure_date"] = DateHelper.convert_date(departure_date)
        if return_date:
            self.book_flight["return_date"] = DateHelper.convert_date(return_date)
        if adults:
            self.book_flight["adults"] = adults
        if child:
            self.book_flight["child"] = child
        if infant:
            self.book_flight["infant"] = infant

    def get_book_flight_field(self, field):
        return self.book_flight[field]

    def process_book_flight_information(self, data_dict):
        book_flight_data = {}
        for row in data_dict:
            book_flight_data[row["Field"]] = row["Value"]

        for key in book_flight_data:
            if key == "departure_date" or key == "return_date":
                self.book_flight[key] = DateHelper.convert_date(book_flight_data.get(key))
            else:
                self.book_flight[key] = book_flight_data.get(key)
