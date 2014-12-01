from tkinter import *
import tkinter.ttk
import datetime
import re
from classes import Schedule, Meeting, Race, Entry
from repeated_timer import RepeatedTimer
import random

TITLE_TEMPLATE = '{name:^80}'
TIME_TEMPLATE = '{time:^20}{meet_no:^20}{country:^20}{venue:^20}'
STATS_TEMPLATE_1 = '{0[0]:^20}{0[1]:^20}{0[2]:^20}{0[3]:^20}\n{0[20]:^20}{0[21]:^20}{0[22]:^20}{0[23]:^20}\n{0[40]:^20}{0[41]:^20}{0[42]:^20}{0[43]:^20}\n\n'
STATS_TEMPLATE_2 = '{0[4]:^20}{0[5]:^20}{0[6]:^20}{0[7]:^20}\n{0[24]:^20}{0[25]:^20}{0[26]:^20}{0[27]:^20}\n{0[44]:^20}{0[45]:^20}{0[46]:^20}{0[47]:^20}\n\n'
STATS_TEMPLATE_3 = '{0[8]:^20}{0[9]:^20}{0[10]:^20}{0[11]:^20}\n{0[28]:^20}{0[29]:^20}{0[30]:^20}{0[31]:^20}\n{0[48]:^20}{0[49]:^20}{0[50]:^20}{0[51]:^20}\n\n'
STATS_TEMPLATE_4 = '{0[12]:^20}{0[13]:^20}{0[14]:^20}{0[15]:^20}\n{0[32]:^20}{0[33]:^20}{0[34]:^20}{0[35]:^20}\n{0[52]:^20}{0[53]:^20}{0[54]:^20}{0[55]:^20}\n\n'
STATS_TEMPLATE_5 = '{0[16]:^20}{0[17]:^20}{0[18]:^20}{0[19]:^20}\n{0[36]:^20}{0[37]:^20}{0[38]:^20}{0[39]:^20}\n{0[56]:^20}{0[57]:^20}{0[58]:^20}{0[59]:^20}\n\n'

TEST_TEMPLATE = STATS_TEMPLATE_1 + STATS_TEMPLATE_2 + STATS_TEMPLATE_3 + STATS_TEMPLATE_4 + STATS_TEMPLATE_5


class BettingDisplay():
    
    def __init__(self, parent, meeting):
        
        self.parent = parent
    
        self.date = datetime.date.today().strftime("%Y-%m-%d") #Currently will need to be restarted each day
        self.meeting = meeting #PLACEHOLDER
        self.schedule = Schedule(self.date, self.meeting)
        self.races = self.schedule.meetings[0].races
        self.next_race = None
        self.set_next_race()
        
        self.odds_var = StringVar()
        self.title_var = StringVar()
        self.dets_var = StringVar()
        
        self.build_display()
        self.start_timer()
        
        print("STARTED SUCCESSFULLY")
    
    def set_next_race(self):
        next_race = None
        found = False
        for race in self.races:
            cur_time = int(datetime.datetime.now().strftime("%H%M%S"))
            race_time = int(re.sub('[:]', '', race.time))
            if race_time > cur_time and not found:
                next_race = race
                found = True
        if next_race is not self.next_race:
            self.next_race = next_race
            
    def start_timer(self):
        self.threading_timer = RepeatedTimer(3, self.refresh)
        self.threading_timer.start() 
        
    def refresh(self):
        self.set_next_race()
        self.next_race.load_odds()
        
        #---TEMP---#
        horse_nums = ['']*20
        for i in range(min(20, len(self.next_race.entries))):
            horse_nums[i] = str(self.next_race.entries[i].number)
            
        horse_names = ['']*20
        for i in range(min(20, len(self.next_race.entries))):
            horse_names[i] = str(self.next_race.entries[i].name) 

        win_odds = ['']*20
        for i in range(min(20, len(self.next_race.entries))):
            win_odds[i] = str(self.next_race.entries[i].odds_win)        
        
        lst = horse_nums + horse_names + win_odds
        odds_str = TEST_TEMPLATE.format(lst)
        title_str = TITLE_TEMPLATE.format(name=self.next_race.name)
        dets_str = TIME_TEMPLATE.format(time=self.next_race.time, venue=self.next_race.meeting.venue, meet_no=self.next_race.meeting.number, country=self.next_race.meeting.country)
        self.title_var.set(title_str)
        self.dets_var.set(dets_str)
        self.odds_var.set(odds_str)        
        
        #---TEMP END---#
              
        
    
    def build_display(self):
         #----TEMP----
        self.cur_race_name = StringVar()
        self.cur_race_time = StringVar()
        
        self.title_text = Label(self.parent, fg="white", bg="black", font=("Courier", 40, "bold"), textvariable=self.title_var)
        self.title_text.place(relx = 0.5, rely = 0, anchor=N, height = 80, width=1100)   
        
        self.title_text = Label(self.parent, textvariable=self.dets_var, fg="white", bg="black", font=("Courier", 20, "bold"))
        self.title_text.place(relx = 0.5, y = 80, anchor=N, height = 30, width=1100)  
               
        
        self.title_text = Label(self.parent, textvariable=self.odds_var, fg="white", bg="black", font=("Courier", 20, "bold"))
        self.title_text.place(relx = 0.5, y = 110, anchor=N, width=1100, height = 600)
        

        self.quitbutton = Button(self.parent, text='quit', command=self.quitclick)
        self.quitbutton.place(relx = 0.5, rely = 1, anchor=S) 
        #---TEMP END ---#
    
    def quitclick(self):
        self.threading_timer.stop()
        self.parent.destroy()
    
if __name__ == '__main__':
    window = Tk()
    window.geometry("1100x800+30+30")       
    display = BettingDisplay(window, '4')
    window.mainloop()        


    
    
