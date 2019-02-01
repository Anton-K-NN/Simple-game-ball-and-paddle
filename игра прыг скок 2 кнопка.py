from tkinter import*
import random
import time

class delay:
    
    
    def click_button():
        
        tk1=Tk()
        tk1.title("Начать игру")
        canvas1=Canvas(tk1,width=150,height=150)
        Button(tk1,text='НАЧАТЬ ИГРУ!',command=MAIN).place(x=40,y=50)
        canvas1.creat_text(100,100,text='gameover',fill=pink)
        canvas1.pack()
        tk1.update()
        time.sleep(2)
       
 
class Ball:

    def __init__(self, canvas, paddle, color):
        self.canvas=canvas
        self.paddle=paddle
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0]
        self.y=-3
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.hit_bottom=False

    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
            if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
                return True
        return False
    
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=3
        if pos[3]>=self.canvas_height:
            self.hit_bottom=True
        if self.hit_paddle(pos)==True:
            self.y=-3
        if pos[0]<=0:
            self.x=3
        if pos[2]>=self.canvas_width:
            self.x=-3
        
        
class Paddle:
    def __init__(self, canvas, color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        self.x=0
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self,evt):
        self.x=-3

    def turn_right(self,evt):
        self.x=3
        
    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos=self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x=0
        elif pos[2]>=self.canvas_width:
            self.x=0



def game_over():
    tk_go=Tk()
    tk_go.title("GAME OVER")
    tk_go.wm_attributes("-topmost",1)
    canvas_go=Canvas(tk_go,width=500, height=400,bd=0, highlightthickness=0).pack()
    tk_go.update()
    text.insert(150,150, text='ИГРА ОКОНЧЕНА',font=('Times',20))
        
def MAIN():
    tk=Tk()
    tk.title("Игра")
    tk.resizable(0,0)
    tk.wm_attributes("-topmost",1)
    canvas=Canvas(tk,width=500, height=400,bd=0, highlightthickness=0)
    canvas.pack()
    tk.update()

    paddle=Paddle(canvas,'blue')
    ball=Ball(canvas, paddle,'red')
    time.sleep(2)
 
    while 1:
        if ball.hit_bottom==False:
            ball.draw()
            paddle.draw()
            tk.update_idletasks()
            tk.update()
            time.sleep(0.01)
        else:game_over()


delay.click_button()
