# -*- coding: utf-8 -*-
banner = """
Created on Sun Mar  8 21:02:00 2015
http://www.codeskulptor.org/#user39_ZxwV0JoKx7_1.py
@author:


   _____         .__         __          
  /     \ _____  |  |  __ __|  | ______  
 /  \ /  \\__  \ |  | |  |  \  |/ /  _ \ 
/    Y    \/ __ \|  |_|  |  /    <  <_> )
\____|__  (____  /____/____/|__|_ \____/ 
        \/     \/                \/      


"""


import simplegui
class Stopwatch(object):
    def __init__(self):
        
        self.timer_intervall = 100
        self.text_size = 50
        self.canvasx = 500
        self.canvasy = 400
        self.stop = 0
        self.on_target = 0
        self.timer_count = 0
        self.st_flag = False
        self.frame = simplegui.create_frame("Stopwatch", self.canvasx, self.canvasy)
        self.create_buttons()
        self.timer = simplegui.create_timer(self.timer_intervall,self.timecount)
        self.frame.set_draw_handler(self.draw)
        self.frame.start()
    def prntime(self):
        s=self.timer_count/10.0
        m=int(s)/60
        if (s >= 60):
            s = s-(60.0*m)
        if s<10:
            self.o = str(+m) + ":0" + str(s)
        else:
            self.o = str(+m) + ":" + str(s)
        return self.o
 
    def start_timer(self):
        self.timer.start()
        self.st_flag = True
    def stop_timer(self):
        if self.st_flag == True:
            self.st_flag = False
            self.timer.stop()
            self.stop +=1
            f = self.timer_count
            print f
            if ((f/10.0)==int(f/10.0)):
                self.on_target +=1
    def reset_timer(self):
        self.timer.stop()
        self.timer = simplegui.create_timer(self.timer_intervall,self.timecount)
        self.timer_count = 0
        self.stop = 0
        self.on_target = 0
    def create_buttons(self):
        self.frame.add_button("   Start   ",self.start_timer)
        self.frame.add_button("   Stop    ",self.stop_timer)
        self.frame.add_button("   Reset   ", self.reset_timer)
    def timecount(self):
        self.timer_count+=1
    
    def draw(self, canvas):
        posx = int(self.canvasx/2)-self.text_size
        posy = int(self.canvasy/2)+int(self.text_size/10)
        output = self.prntime()
        canvas.draw_text(output, (posx,posy), self.text_size, "Red")
        out2 = str(self.on_target)+" / "+str(self.stop)
        canvas.draw_text(out2,(self.canvasx-100,65), 30, "Yellow")
        if self.stop > 0:
            sr = int((self.on_target/float(self.stop))*100)
            out3 = "Successrate  " + str(sr) + " %"
            canvas.draw_text(out3,(95,self.canvasy-40), 16, "Yellow")
            #canvas.draw_line((100, self.canvasy-10), (100+sr, self.canvasy-10), 12, 'Red')
            canvas.draw_line((95, self.canvasy-65), (205, self.canvasy-65), 12, 'Yellow')
            canvas.draw_line((100, self.canvasy-65), (100+sr+2, self.canvasy-65), 12, 'Red')
            #canvas.draw_line((100, self.canvasy-10), (100+sr, self.canvasy-10), 15, 'Red')

    
def main():
    stopwatch = Stopwatch()
if __name__ == "__main__":
    main()
