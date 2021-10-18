class Nother:
    def __init__(self,user):
        self.number = 0
        self.soc  = 0
        self.dob = 0
        self.user = user

    def set_soc(self, soc_number):
        self.soc = soc_number

    def get_soc(self):
        return self.soc

    def set_dob(self, dob_number):
        self.dob = dob_number

    def get_dob(self):
        return self.dob