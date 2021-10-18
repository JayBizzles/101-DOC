class Bank:
    def __init__(self):
        self.roi = 000
    def get_roi():
        print(self.roi)

class SBI(Bank):
    def __init__(self):
        self.roi =0
    def get_roi(self):
        self.roi = 0.08
        print(f"my ROI:{self.roi} ")

class ICICI(Bank):
    def __init__(self):
        self.roi =0
    def get_roi(self):
        self.roi = 0.09
        print(f"my ROI:{self.roi} ")

class AXIS(Bank):
    def __init__(self):
        self.roi =0
    def get_roi(self):
        self.roi = 0.11
        print(f"my ROI:{self.roi} ")


sbi_account = SBI(Bank)
sbi_account.get_roi()

icici_account = ICICI()
icici_account.get_roi()

axis_account = AXIS()
axis_account.get_roi()