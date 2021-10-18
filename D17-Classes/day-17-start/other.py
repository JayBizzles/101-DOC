class Other:
    def __init__(self,user):
        self.location = ""
        self.username = user.name

    
    def set_location(self, location):
        self.location = location

    def get_location(self): return self.location