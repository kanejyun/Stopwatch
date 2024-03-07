from datetime import datetime

class StopWatch:
    def __init__(self):
        self.reset()

    def reset(self):
        self.time_start = None
        self.time_list = []
        
    def start(self):
        self.reset()
        self.time_start = datetime.now()
             
    def stop(self):
        if not self.time_list:
            self.check()
        print(f"TOTAL : {(self.time_list[-1] - self.time_start).total_seconds():.5f} seconds")
      
    def time_check(self):
        self.time_list.append(datetime.now())
        
    def print_lap(self):
        if not self.time_list :
            self.check()
        print(f"LAP {1} : {(self.time_list[0] - self.time_start).total_seconds():.5f}")
        for i in range(1, len(self.time_list)):
            print(f"LAP {i+1} : {(self.time_list[i] - self.time_list[i-1]).total_seconds():.5f} seconds")
                      
    def print_split(self):
        if not self.time_list :
            self.check()
        for i in range(len(self.time_list)):
            print(f"SPLIT {i+1} : {(self.time_list[i] - self.time_start).total_seconds():.5f} seconds")
            

