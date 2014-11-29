SCHEDULE_DOMAIN = "http://xml.tab.co.nz/schedule/"

class Schedule:
    
    def __init__ (self, date=None, meet_no=None):
        self.date = date
        self.meet_no = meet_no
        self.load_xml()
        self.load_meetings()
    
    def load_xml(self):
        domain = SCHEDULE_DOMAIN
        if date:
            domain += date + '/'
            if meet_no:
                domain += meet_no
                
        f = urllib.request.urlopen(domain)
        xml_content = f.read()
        self.xml_schedule = ET.fromstring(self.xml_content).find('meetings')
    
    def load_meetings(self):
        self.meetings = []
        for xml_meeting in self.xml_schedule.findall('meeting'):
            meeting = Meeting(xml_meeting)
            self.meetings.append(meeting)

class Meeting:
    
    def __init__(self, xml_meeting):
        self.xml_meeting = xml_meeting
        self.code = xml_meeting.find('code').text
        self.country = xml_meeting.find('country').text
        self.date = xml_meeting.find('date').text
        self.number = int(xml_meeting.find('number').text)
        self.name = xml_meeting.find('name').text
        self.is_nz = xml_meeting.find('nz').text == '1'
        self.status = xml_meeting.find('status').text
        self.typ = xml_meeting.find('type').text
        self.venue = xml_meeting.find('venue').text
        
        self.load_races()
        
    def load_races(self):
        self.races = []
        for xml_race in self.xml_meeting.find('races').findall('race'):
            race = Race(xml_race)
            self.races.append(race)   
        
class Race:
    
    def __init__(self, xml_race):
        self.xml_race = xml_race
    
        self.race_class = xml_race.find('class').text
        self.length = xml_race.find('length').text
        self.name = xml_race.find('name').text
        
        norm_time = xml_race.find('norm_time').text
        self.date = norm_time.split()[0]
        self.time = norm_time.split()[1]
        
        self.number = int(xml_race.find('number').text)
        self.stake = xml_race.find('stake').text
        self.status = xml_race.find('status').text
        self.track_conditions = xml_race.find('track').text
        self.weather = xml_race.find('weather').text
        
        self.load_entries()
        
    def update_xml(self, xml_race):
        self.xml_race = xml_race
        
    def refresh(self):
        self.race_class = self.xml_race.find('class').text
        self.length = self.xml_race.find('length').text
        self.name = self.xml_race.find('name').text
        
        norm_time = self.xml_race.find('norm_time').text
        self.date = norm_time.split()[0]
        self.time = norm_time.split()[1]
        
        self.number = int(xml_race.find('number').text)
        self.stake = xml_race.find('stake').text
        self.status = xml_race.find('status').text
        self.track_conditions = xml_race.find('track').text
        self.weather = xml_race.find('weather').text
        
        self.refresh_entries()
        
        
    def load_entries(self):
        self.entries = []
        for xml_entry in self.xml_race.find('entries').findall('entry'):
            entry = Entry(xml_entry)
            self.entries.append(entry)   
    
        
        
        
        
class Entry:
    
    def __init__(self, xml_entry):
        self.xml_entry = xml_entry
        
        self.barrier = int(xml_entry.find('barrier').text)
        self.jockey = xml_entry.find('jockey').text
        self.name = xml_entry.find('name').text
        self.number = int(xml_entry.find('number').text)
        self.scratched = xml_entry.find('scratched').text == '1'
        
    def update_xml(self, xml_entry):
        self.xml_entry = xml_entry
    
    def refresh(self):
        self.barrier = int(self.xml_entry.find('barrier').text)
        self.jockey = self.xml_entry.find('jockey').text
        self.name = self.xml_entry.find('name').text
        self.number = int(self.xml_entry.find('number').text)
        self.scratched = self.xml_entry.find('scratched').text == '1'        
        
        