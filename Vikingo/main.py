from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader


import random   #random location in 10x10 grid (bottom left corner)
def randy():
    return float(random.randint(0,9))/10


#Introduce the protagonist

class MoveableImage(Image):   

    def __init__(self, **kwargs): #Inherit the Image class
        super(MoveableImage, self).__init__(**kwargs)


  #Allow protagonist to move with either arrows or touch

    #Request and bind the keyboard
        self._keyboard = Window.request_keyboard(None, self) #Request the keyboard

        if not self._keyboard:
            return 
        self._keyboard.bind(on_key_down=self.on_keyboard_down)#Bind the keyboard

    
    def on_keyboard_down(self, keyboard, keycode, text,modifiers):
        if keycode[1] == 'left': #Put key here
            self.x -= 10 #Put an action
        if keycode[1] == 'right':
            self.x += 10 
        if keycode[1] == 'down':
            self.y -= 10 
        if keycode[1] == 'up':
            self.y += 10 
        else:
            return False
        return True

    # Record location of press down
    def on_touch_down(self,touch):
        global _x,_y
        _x,_y=touch.pos
 
    # Define logic for swiping or dragging
    
    def on_touch_move(self,touch):
        swipe=20
        x_min,x_max = -Window.width/2,Window.width/2
        y_min,y_max = -Window.height/2,Window.height/2
        if touch.x>(_x+swipe):
            if (self.x+Window.width/20)<x_max:
                self.x+= Window.width/20
        elif touch.x<(_x-swipe):
            if (self.x-Window.width/20)>x_min:
	            self.x-= Window.width/20
        if touch.y>(_y+swipe):
            if (self.y+Window.height/20)<y_max:
                self.y+= Window.height/20
        elif touch.y<(_y-swipe):
            if (self.y-Window.height/20)>y_min:
	            self.y-= Window.height/20

#Introduce the Antagonist

class ClockMay(Image):

    def __init__(self,**kwargs): 
        super(ClockMay,self).__init__(**kwargs) #Inherit the Image class
        self.start=True
        Clock.schedule_interval(self.update,1/5) #Schedule an event 'update' every x seconds

#Logic to bring the antagonist to life
    
    def update(self, *args):
        global button
        speed = 0.3
        if self.start:
    	    self.x,self.y = randy()*Window.width,randy()*Window.height
    	    self.start=False
        if self.center_x < viking.x+ Window.width/2.:
    	    self.center_x+=speed
        if self.center_x > viking.x+ Window.width/2.:
    	    self.center_x-=speed
        if self.center_y < viking.y+ Window.height/2.:
    	    self.center_y+=speed
        if self.center_y > viking.y+ Window.height/2.:
    	    self.center_y-=speed


    	# When the protagnoists and antagonist collide 
        if abs(self.center_x - (viking.x+ Window.width/2 ))< Window.width/20. and\
           abs(self.center_y - (viking.y+ Window.height/2 ))< Window.width/20.:
    	    Clock.unschedule(self.update) #Stop the clock
    	    fail.play() #Play a sound
    	    floater.remove_widget(viking) #Kill the antagonist
    	    button = Button(size_hint=(0.1,0.1),text='Start',
    			pos_hint={'center_x':0.5},
    			on_press=self.clicked)
    	    floater.add_widget(button) #Click the button to trigger 'clicked'

    def clicked(self,*args): #Reset everything and start the clock again
        floater.remove_widget(button) 
        self.start=True
        floater.add_widget(viking)
        score.points=0
        score.text='Score: 0'
        Clock.schedule_interval(self.update,1/5) 
	

#Introducing the reward
        
class ClockShroom(Image):

    def __init__(self,**kwargs):
        super(ClockShroom,self).__init__(**kwargs) #Inherit the Image class
        Clock.schedule_interval(self.update,1/5) #Schedule an event 'update' every x seconds


    #Define logic for reward
    def update(self, *args):
        if abs(self.center_x - (viking.x+ Window.width/2 ))< Window.width/20. and abs(self.center_y - (viking.y+ Window.height/2 ))< Window.width/20.:
    	    score.points+=1
    	    beep.play()
    	    score.text='Score: ' + str(score.points)
    	    self.x,self.y = randy()*Window.width,randy()*Window.height
	    
#Counter to store the score
class Score(Label):
    def __init__(self,**kwargs):
        super(Score,self).__init__(**kwargs)
        self.points=0

#Put everything togeher on top of a floatlayout

class GameApp(App):

    def build(self):
        
        global viking,floater,score,beep,fail
        beep = SoundLoader.load('beep.wav')
        fail = SoundLoader.load('brexit.wav')
    
        floater = FloatLayout()
        Window.clearcolor=(1,1,1,1)
        
        score = Score(text='Score: 0',
    			  pos_hint={'x':0.05,'y':0.9},
    			  size_hint=(0.1,0.1),
    			  color=(0,0,0,1))
        
        floater.add_widget(score)
        
        shroom = ClockShroom(source='shroom.png',
    			 size_hint=(0.1,0.1))
        
        floater.add_widget(shroom)
        
        
        viking = MoveableImage(source='dude.png', anim_available=True, anim_delay=.15)
        floater.add_widget(viking)
        
        may = ClockMay(source='may.png',
    			 size_hint=(0.1,0.1))
        floater.add_widget(may)
        return floater

if __name__ == "__main__":
    GameApp().run()


