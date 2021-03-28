
class Hardware:
    def __init__(self, description):
        self.description = description
        

class Laptop:
    def __init__(self):
        RAM = Hardware('Memory is 16GB')
        Inner = Hardware('SSD is 512GB')
        self.hardware = [RAM, Inner]

    def configuration(self):
        print(self.hardware)
        for hardware in self.hardware:
            print(hardware.description)


laptop = Laptop()
laptop.configuration()
