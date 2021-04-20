from turtle import Turtle
FONT = ("Verdana", 12, "normal")
LOGO = r'''
   _____             _           _____                      
  / ____|           | |         / ____|                                         
 | (___  _ __   __ _| | _____  | |  __  __ _ _ __ ___   ___ 
  \___ \| '_ \ / _` | |/ / _ \ | | |_ |/ _` | '_ ` _ \ / _ \
  ____) | | | | (_| |   <  __/ | |__| | (_| | | | | | |  __/
 |_____/|_| |_|\__,_|_|\_\___|  \_____|\__,_|_| |_| |_|\___|
                                                            
               _________         _________                  
              /         \       /         \                 
             /  /~~~~~\  \     /  /~~~~~\  \                
             |  |     |  |     |  |     |  |                
             |  |     |  |     |  |     |  |                
             |  |     |  |     |  |     |  |         /      
             |  |     |  |     |  |     |  |       //       
            (o  o)    \  \_____/  /     \  \_____/ /        
             \__/      \         /       \        /         
              |         ~~~~~~~~~         ~~~~~~~~          
              ^                                             
'''


class Logo(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.write(arg=LOGO, align="center",font=FONT)