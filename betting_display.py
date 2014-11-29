from tkinter import *
from tkinter.ttk import *
import datetime
import re
from classes import Schedule, Meeting, Race, Entry
from repeated_timer import RepeatedTimer
import random

TEST_TEMPLATE = '{name:^160}\n{time:^160}\n\n\n\t{0[0]}\t{0[1]}\t{0[2]}\t{0[3]}\t\t\n\t{0[4]}\t{0[5]}\t{0[6]}\t{0[7]}\t\t\n{0[8]}\t{0[10]}\t{0[11]}\t{0[11]}\t\t'


class BettingDisplay():
    
    def __init__(self, parent, meeting):
        
        self.parent = parent
    
        self.date = datetime.date.today().strftime("%Y-%m-%d") #Currently will need to be restarted each day
        self.meeting = meeting #PLACEHOLDER
        self.schedule = Schedule(self.date, self.meeting)
        self.races = self.schedule.meetings[0].races
        self.next_race = None
        self.set_next_race()
        
        self.test_var = StringVar()
        
        self.build_display()
        #self.display_odds()
        self.start_timer()
        
        print(self.next_race.time)
    
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
        horse_nums = [entry.number for entry in self.next_race.entries][:4]
        horse_names = [entry.name for entry in self.next_race.entries][:4]
        win_odds = [entry.odds_win for entry in self.next_race.entries][:4]
        lst = horse_nums + horse_names + win_odds
        out_str = TEST_TEMPLATE.format(lst, name=self.next_race.name, time=self.next_race.time)
        
        #---TEMP END---#
              
        
        self.test_var.set(out_str)
    
    def build_display(self):
        
        self.cur_race_name = StringVar
        self.cur_race_time = StringVar
        
        self.title_label = Label(self.parent, textvariable=self.test_var, tabs=('20c')
        self.title_label.place(relx = 0.5, rely = 0, anchor=N)
        
        self.quitbutton = Button(self.parent, text='quit', command=self.quitclick)
        self.quitbutton.place(relx = 0.5, rely = 1, anchor=S)     
            
    #def display_odds(self):
        #self.frame = Frame(self.parent)
        #self.frame.pack()   
        #self.label = Label(self.frame, textvariable=self.test_var)
        #self.label.pack()        
        #self.quitbutton = Button(self.frame, text='quit', command=self.quitclick)
        #self.quitbutton.pack()
    
    def quitclick(self):
        self.threading_timer.stop()
        self.parent.destroy()
    
if __name__ == '__main__':
    window = Tk()
    window.geometry("500x200+30+30")
    display = BettingDisplay(window, '2')
    window.mainloop()
    
    
lst = ['1', '2', '3', '4', 'Test1', 'Test2', 'Test3', 'Test4', 1.1, 2.2, 3.3, 4.4]
   
str_test ='{0[0]:^20}\t{0[1]:^20}\t{0[2]:^20}\t{0[3]:^20}\n{0[4]:^20}\t{0[5]:^20}\t{0[6]:^20}\t{0[7]:^20}\n{0[8]:^20}\t{0[10]:^20}\t{0[11]:^20}\t{0[11]:^20}'.format(lst)

