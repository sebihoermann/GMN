
"""
Created on Sat Feb 28 15:36:32 2015

"""

import simplegui
class GuessTheNumber(object):
    import simplegui
    import random, time
    """ Class GuessTheNumber is an implementation of the Binary Search as 
        discussed in the Coursera Course:
        
        An Introduction to Interactive Programming in Python (Part 1)
        
     """
        
    def __init__(self, RangeEnd = 100,Guesses = 7, RangeEnd2 = 1000, Guesses2 = 10, godmode = False):
        """
        Function __init__
        Initializing Variables and The Gui.
            godmode 	allows for cheating/debugging. 
                E.g. 	* shows the secret number, 
                        * allows for adding 10 free Guesses,
                        * Random Range and Guesses
                        
            RangeEnd 	defines the upper Range
            Guesses 	Number of guesses allowed
            Guess		Stores a list of guesses made
            Turn		Countss the turn
            frame		Gui-Frame of Simplegui
            inp			Stores User Text Input (-->converted to number)
            label1...3	Gui Labels
            button1...6	Gui Buttons
           
            
            """
            
            
        self.godmode = godmode
        self.RangeEnd = RangeEnd
        self.Guesses = Guesses
        self.RangeEnd1 = RangeEnd
        self.Guesses1 = Guesses
        self.RangeEnd2 = RangeEnd2
        self.Guesses2 = Guesses2
        self.Guess = []
        self.Turn = 1
        self.ScoreBoard = []
        self.debugging_output = False
        self.output = ["Debugging Summary:","","(!!! Look into Console for Game's Output. !!!)",""]
        #self.GameInit(self.RangeEnd, self.Guesses)
        # self.Gaminit initializes and starts a new game with set values
        self.frame = simplegui.create_frame("Test",500,600)
        self.frame.set_canvas_background('White')
        self.label1 = self.frame.add_label("Please choose a Range:\n\n")
        self.button1 = self.frame.add_button("Range 0 to 100", self.range1)
        self.button2 = self.frame.add_button("Range 0 to 1000", self.range2)
        self.label2 = self.frame.add_label("\n\n\nPlease try to guess my Number:\n\n")
        self.inp = self.frame.add_input('Your Guess is: ', self.input_handler, 50)
        self.label3 = self.frame.add_label("\n\n\nTurn on GodMode for Cheats!\n\n\n")
        self.button4 = self.frame.add_button("Toggle GodMode", self.GodmodeToggle)
        self.button_help = self.frame.add_button("Help",self.help)
        self.button_mostneeded = self.frame.add_button("Most needed Guesses", self.MostGuesses)
        self.frame.set_draw_handler(self.draw_handler)
        self.frame.start()
    def draw_handler(self, canvas):
        if self.debugging_output == True:
            if len(self.output) <=46:
                z = len (self.output)
            else:
                self.output = self.output[45:]
                z = len(self.output)
            for i in range(z):
                text = self.output[i].strip("\n")
                canvas.draw_text(str(text), (20, (i+1)*13,), 12, 'Red')
    def MostGuesses(self):
        import math
        """
        Calculates the most Guesses needed for the range.
        """
        self.mostneeded = math.ceil(math.log(self.RangeEnd+1,2))
        out= "\nThe secret Number can always be found in @most %d Guesses.\n" %(self.mostneeded)
        print out
        self.out(out)
    def out(self,out):
        try:
            self.output.append(out)
        except:
            pass
    def help(self):
        """Function Help:
            Displays Help Text.
            """
        h = """
  ___ ___         .__          
 /   |   \   ____ |  | ______  
/    ~    \_/ __ \|  | \____ \ 
\    Y    /\  ___/|  |_|  |_> >
 \___|_  /  \___  >____/   __/ 
       \/       \/     |__|    
        
        """
        
        print h, "\n"
        print """ Class GuessTheNumber is an implementation of the Binary Search as 
        discussed in the Coursera Course:
        
        An Introduction to Interactive Programming in Python (Part 1)
        
     """
        print """\n
        You can enter the CheatMode by pressing the Button \"Toggle GodMode\" for debugging.
        """
        print """\n
        Functions and useful Variables:
        _______________________________
        
        Function __init__
        Initializing Variables and The Gui.
        
        
            godmode      allows for cheating/debugging. 
            E.g.         * shows the secret number, 
                         * allows for adding 10 free Guesses,
                         * Random Range and Guesses
                        
            RangeEnd	 defines the upper Range
            Guesses      Number of guesses allowed
            Guesses      Stores a list of guesses made
            Turn         Countss the turn
            frame        Gui-Frame of Simplegui
            inp          Stores User Text Input (-->converted to number)
            label1...3   Gui Labels
            button1...6  Gui Buttons
        
        - Function GodmodeToggle:
        
        Toggles Godmode, handles button4 of the Gui.
        Prints a banner to show that Godmode is on/off.
        Adds additional buttons to the Gui.
        Cheats:        
                        * shows the secret number, 
                        * allows for adding 10 free Guesses,
                        * Random Range and Guesses
                        * Ignore repeated User Guesses
                        * Ignores out of Range numbers        
        
        - Function youwin:
        Outputs banner signaling User won the Game.
        
        - Function GameOver:
        Outputs banner signaling User lost the Game.
        
        - Function Banner:
        Outputs Welcome-Banner.
        
        - Function Score:
        Calculates Playerscore which multiplies the final count of
        The Guesses needed by 1000
        And divides it by Time needed.
        
        - Function
        Headline formats the Headline banner.
        
        - Function range1 
        Initialises a game with the first Range and
        first Number of Guesses.
        Initial Range and Guesses are passed to the Class.
        
        - Function range2 Initialises a game with a random Range and
        a random Number of Guesses.
        
        - Function range3 Initialises a game with a random Range and
        a random Number of Guesses.
        
        - Function input_handler:
        Handles the User input of the Text Field (inp) of frame of the
        Gui.
        
        It also processes this Input String, converts it to an integer
        and compares it to the Secret Number.
        
        - Function ShowSecretNumber
        Outputs the secret Number.
            
        - Function StopTime 
        stops the Timer and prints out the result.
        
        - Function PlusTenGuesses
        Cheat Function that adds ten Guesses.
        
        - Function GameInit
        Initializes the Game
        
        LuckyNumberSlevin is the Variable that holds the secret Number.
        
        
        """
        
    def GodmodeToggle(self):
        """
        Function GodmodeToggle:
        
        Toggles Godmode, handles button4 of the Gui.
        Prints a banner to show that Godmode is on/off.
        Adds additional buttons to the Gui.
        Cheats:        
                        * shows the secret number, 
                        * allows for adding 10 free Guesses,
                        * Random Range and Guesses
                        * Ignore repeated User Guesses
                        * Ignores out of Range numbers
        
        """
        self.godmode = not self.godmode
        gm_on = """
   _____           _ __  __           _         ____        
  / ____|         | |  \/  |         | |       / __ \       
 | |  __  ___   __| | \  / | ___   __| | ___  | |  | |_ __  
 | | |_ |/ _ \ / _` | |\/| |/ _ \ / _` |/ _ \ | |  | | '_ \ 
 | |__| | (_) | (_| | |  | | (_) | (_| |  __/ | |__| | | | |
  \_____|\___/ \__,_|_|  |_|\___/ \__,_|\___|  \____/|_| |_|
                                                            
                                                            

        
        """
        gm_off = """
        
   _____           _ __  __           _         ____   __  __ 
  / ____|         | |  \/  |         | |       / __ \ / _|/ _|
 | |  __  ___   __| | \  / | ___   __| | ___  | |  | | |_| |_ 
 | | |_ |/ _ \ / _` | |\/| |/ _ \ / _` |/ _ \ | |  | |  _|  _|
 | |__| | (_) | (_| | |  | | (_) | (_| |  __/ | |__| | | | |  
  \_____|\___/ \__,_|_|  |_|\___/ \__,_|\___|  \____/|_| |_|  
                                                              
       
        """

        if self.godmode == True:
            print gm_on
            try:
                self.button3
               
            except:
                self.button3 = self.frame.add_button("Random Range", self.range3)
            try:
                self.button5
            except:
                self.button5 = self.frame.add_button("Show Secret Number", self.ShowSecretNumber)
            try:
                self.button6
            except:
                self.button6 = self.frame.add_button("+ 10 Guesses", self.PlusTenGuesses)
            try:
                self.button_debug
            except:
                self.button_debug = self.frame.add_button("DebugInfo", self.ToggleDebug)
                
                
            
        else:
            print gm_off
            
                
    def ToggleDebug(self):
        """
        Toggles Debug Console."
        """
        self.debugging_output = not self.debugging_output
    def youwin(self):
        """
        Function youwin:
        
        Outputs banner signaling User won the Game.
        """
        yw = """
     
 __  ______  __  __  _      _______  __  ______
 \ \/ / __ \/ / / / | | /| / /  _/ |/ / / / / /
  \  / /_/ / /_/ /  | |/ |/ // //    / /_/_/_/ 
  /_/\____/\____/   |__/|__/___/_/|_/ (_|_|_)  
                                               


                                               
                                               """                            
        print "\n"
        print yw
        
    def GameOver(self):
        """
        Function GameOver:
        Outputs banner signaling User lost the Game.
        """
        go = """
  ____   ____  ___ ___    ___       ___   __ __    ___  ____  
 /    T /    T|   T   T  /  _]     /   \ |  T  |  /  _]|    \ 
Y   __jY  o  || _   _ | /  [_     Y     Y|  |  | /  [_ |  D  )
|  T  ||     ||  \_/  |Y    _]    |  O  ||  |  |Y    _]|    / 
|  l_ ||  _  ||   |   ||   [_     |     |l  :  !|   [_ |    \ 
|     ||  |  ||   |   ||     T    l     ! \   / |     T|  .  Y
l___,_jl__j__jl___j___jl_____j     \___/   \_/  l_____jl__j\_j
                                                              

        
        """
        print go
    def Banner(self):
        """
        Function Banner:
        Outputs Welcome-Banner.
        """
        banner = """
 __      __         .__                                    
/  \    /  \  ____  |  |    ____    ____    _____    ____  
\   \/\/   /_/ __ \ |  |  _/ ___\  /  _ \  /     \ _/ __ \ 
 \        / \  ___/ |  |__\  \___ (  <_> )|  Y Y  \\  ___/ 
  \__/\  /   \___  >|____/ \___  > \____/ |__|_|  / \___  >
       \/        \/            \/               \/      \/ 
                                                           
____ _  _ ____ ____ ____    _  _ _   _    _  _ _  _ _  _ ___  ____ ____ 
| __ |  | |___ [__  [__     |\/|  \_/     |\ | |  | |\/| |__] |___ |__/ 
|__] |__| |___ ___] ___]    |  |   |      | \| |__| |  | |__] |___ |  \ 
                                                                                                                                                                  
        """
        print banner
    def Score(self):
        """
        Function Score:
        Calculates Playerscore which multiplies the final count of
        The Guesses - Most Guesses one should need by 1000
        And divides it by Time needed.
        
        """
        #print self.Turn, self.Guesses
        self.MostGuesses()
        self.score = int(float(self.mostneeded-self.Turn)*1000/float(self.seconds))
        out= "Your score is: %d" %(self.score)
        print out
        self.out(out)
        self.ScoreBoard.append(self.score)
        
    def headline(self,out,d):
        """
        Function
        Headline formats the Headline banner.
        """
        print "\n"
        print "="*(len(out)-2+len(str(d)))
        print out %(self.Turn)
        print "="*(len(out)-2+len(str(d)))
    def range1(self):
        """
        Function range1 Initialises a game with the first Range and
        first Number of Guesses.
        Initial Range and Guesses are passed to the Class.
        """
        self.GameInit(self.RangeEnd1,self.Guesses1)
    def range2(self):
        """
        Function range2 Initialises a game with the second Range and
        second Number of Guesses.
        """
        self.GameInit(self.RangeEnd2,self.Guesses2)
    def range3(self):
        """
        Function range3 Initialises a game with a random Range and
        a random Number of Guesses.
        """
        if self.godmode == True:
            import random
            self.RangeEnd = random.randrange (2000,500000)
            self.Guesses = random.randrange (5,30)
            #print "You got %d guesses." %(self.Guesses)
            self.GameInit(self.RangeEnd,self.Guesses)
    def input_handler(self,inp):
        """
        Function input_handler:
        Handles the User input of the Text Field (inp) of frame of the
        Gui.
        
        It also processes this Input String, converts it to an integer
        and compares it to the Secret Number.
        """
        try:
            answer = int(inp)
            if answer in self.Guess:
                print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                print "Sir, you tried that number already!"
                print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                if self.godmode == True:
                    return
            if (answer < 0) or (answer > self.RangeEnd):
                print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                print "Number is out of Range, Sir!"
                print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                if self.godmode == True:
                    return
        except:
            out =  "Please enter an integer!"
            print out
            self.out(out)
            return    
     
        self.Guess.append(answer)
        if self.Turn <= self.Guesses:
            d = self.Guesses-self.Turn
            out = "This is Turn: "
            self.headline(out+"%d.",d)
            self.out(out+str(self.Turn))
            out= "\n(%d guesses remaining.)" %(d)
            print out
            self.out(out)
            out= "Your Guess is: %d" %(answer)
            print out
            self.out(out)
            if (answer < self.LuckyNumberSlevin):
                out= "...and that is lower than my number."
                print out
                self.out(out)
            elif (answer > self.LuckyNumberSlevin):
                out= "...and that is higher than my number."
                print out
                self.out(out)
            else:
                out= "...and that is CORRECT!!!"
                self.out(out)
                print out
                self.StopTime()
                self.youwin()
                self.Score()
                self.GameInit(self.RangeEnd, self.Guesses)
            out =  "Your Guesses so far:\n"
            print out
            self.out(out)
            out = str(self.Guess)
            self.out(out)
            print out
            self.Turn += 1
        if self.Turn > self.Guesses:
            self.StopTime()
            out =  "Sorry, you lost!"
            self.out(out)
            self.GameOver()
            self.GameInit(self.RangeEnd, self.Guesses)
    def ShowSecretNumber(self):
        """Function ShowSecretNumber
            Outputs the secret Number.
            """
        if self.godmode == True:
            out =  "Secret Number: "+str(self.LuckyNumberSlevin)
            print out
            self.out(out)
    def StopTime(self):
        """
        Function StopTime stops the Timer and prints out the result.
        """
        import time
        self.stop = time.time()
        self.seconds = self.stop - self.start
        out = "Your time: %d Seconds." %(self.seconds)
        print out
        self.out(out)
    def PlusTenGuesses(self):
        """
        Function PlusTenGuesses
        Cheat Function that adds ten Guesses.
        """
        if self.godmode == True:
            out = "Ten guesses added..."
            print out
            self.out(out)
            self.Guesses +=10
    def GameInit(self, RangeEnd = 100, Guesses = 7):
        """
        Function GameInit
        initializes the Game
        
        LuckyNumberSlevin is the Variable that holds the secret Number.
        """
        import random, time
        self.start = time.time()
        self.Banner()
        self.Turn = 1
        self.Guesses  = Guesses
        self.RangeEnd = RangeEnd
        self.Guess = []
        self.LuckyNumberSlevin = random.randrange(0, self.RangeEnd)
        out = "\n\nNew Game. Range is 0 to %d." % (self.RangeEnd)
        print out
        self.out(out)
        out = "You have %d guesses." %(self.Guesses)
        self.out(out)
        print out
       
   
                
        
def main():
    game=GuessTheNumber()
    game.GameInit()
if __name__ == '__main__':
    main()
