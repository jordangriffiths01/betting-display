import urllib.request
import xml
import xml.etree.ElementTree as ET

SCHEDULE_DOMAIN = "http://xml.tab.co.nz/schedule/"

class Schedule:
    
    def __init__ (self, date=None, meet_no=None):
        self.date = date
        self.meet_no = meet_no
        self.load_xml()
        self.load_meetings()
    
    def load_xml(self):
        domain = SCHEDULE_DOMAIN
        if self.date:
            domain += self.date + '/'
            if self.meet_no:
                domain += self.meet_no
                
        f = urllib.request.urlopen(domain)
        xml_content = f.read()
        self.xml_schedule = ET.fromstring(xml_content).find('meetings')
    
    def update(self):
        self.load_xml()
        self.load_meetings()
    
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
        
    def load_entries(self):
        self.entries = []
        for xml_entry in self.xml_race.find('entries').findall('entry'):
            entry = Entry(xml_entry)
            self.entries.append(entry)      
    
        
class Entry:
    
    def __init__(self, xml_entry):
        self.xml_entry = xml_entry
        
        self.barrier = self.get_attrib('barrier')
        self.jockey = self.get_attrib('jockey')
        self.name = self.get_attrib('name')
        self.number = self.get_attrib('number')
        self.scratched = self.get_attrib('scratched')
        
    
    def get_attrib(self, attrib, int_reqd=False):
        try:
            if int_reqd:
                return int(self.xml_entry.find(attrib).text)
            else:
                return self.xml_entry.find(attrib).text
        except:
            return None
                
        
        
if __name__ == '__main__':
    schedule = Schedule('2014-11-14', '3')
    for meeting in schedule.meetings:
        print('MEETING:', meeting.number)
        for race in meeting.races:
            print('\tRACE:', race.number, race.name)
            for entry in race.entries:
                print('\t\t', entry.barrier, entry.name, entry.jockey)
                