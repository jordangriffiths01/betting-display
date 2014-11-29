class Meeting:
    
    def __init__(self, number, venue, xml_element):
        self.venue = venue
        self.number = number
        self.xml_element = xml_element
        self.load_races()
        
    def load_races(self):
        self.races = []
        
class Race:
    
    def __init__(self):