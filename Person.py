class Person:
    """description of class"""
    def __init__(self, first_name, last_name):
        #basic information about people
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = ""
        self.suffix = ""
        self.address = ""
        self.address_l1 = ""
        self.address_l2 = ""
        self.city = ""
        self.precinct = ""
        self.dob = ""
        self.zipcode = ""
        self.county = ""
        self.active = False

    def set_middle_name(self, middle_name):
        self.middle_name = middle_name

    def set_suffix(self, suffix):
        self.suffix = suffix

    def set_address_l1(self, address_l1):
        self.address_l1 = address_l1

    def set_address_l2(self, address_l2):
        self.address_l2 = address_l2

    def set_city(self, city):
        self.city = city

    def set_precinct(self, precinct):
        self.precinct = precinct

    def set_dob(self, dob):
        self.dob = dob

    def set_zipcode(self, zipcode):
        self.zipcode = zipcode

    def set_county(self, county):
        self.county = county

    def set_active(self, active):
        self.active = active

    def merge_addresses(self):
        self.address = self.address_l1.replace(' ', '') + self.address_l2.replace(' ', '')


