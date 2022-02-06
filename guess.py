import tkinter as tk
import pygame,random
from tkinter import messagebox as mb
from PIL import Image,ImageTk
import os

class Game:
    def __init__(self,root):
        self.count = 1
        self.root = root

    def change(self):
        self.count += 1

    def play(self):
        self.choice = str(self.count)+'.ogg'
        try:
            file_path = os.path.join("sound",self.choice)
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play(loops=1)
        except pygame.error:
            mb.showerror("YO! FILE ERROR OCCURED","While excecuting the code make sure it is in directory where file is downloaded \n Like check Present directory")

    def check(self,anime_name,character_name):
        value = self.guess_anime.get().lower().rstrip()
        char = self.guess_character.get().lower().rstrip()
        game.change()
        if value in anime_name and character_name in char:
            mb.showinfo("Amazing","You are man of culture \n Play Again for different anime")
            self.score += 10
            self.scores.configure(text="Score={}".format(self.score))
            game.clear()
        else:
            mb.showerror("This isn't for you","So your a normie with no anime taste \n Or might be a Type, Try Next Time")
            game.clear()

    def result(self):
        try:
            if len(self.guess_anime.get()) == 0 or len(self.guess_character.get()) == 0:
                mb.showerror("Try Again","Yo enter Something")
            else:
                if self.choice == '1.ogg':
                    game.check("one piece","luffy")
                if self.choice == '2.ogg':
                    game.check(["attack on titan","shingeki no kyojin"],"levi")
                if self.choice == '3.ogg':
                    game.check(["naruto","naruto shippuden"],"naruto")
                if self.choice == '4.ogg':
                    game.check("death note","light")
                if self.choice == '5.ogg':
                    game.check(["love is war","kaguya sama","kaguya-sama love is war","kaguya sama love is war"],"kaguya")
                if self.choice == '6.ogg':
                    game.check("jujutsu kaisen","gojo")
                if self.choice == '7.ogg':
                    game.check("kakegurui","yumeko")
                if self.choice == '8.ogg':
                    game.check("gintama","gintoki")
                if self.choice == '9.ogg':
                    game.check("demon slayer","giyuu")
                if self.choice == '10.ogg':
                    game.check("violet evergarden","violet")
            del self.choice
        except AttributeError:
            mb.showwarning("Play Music","Make sure to play first")

    def clear(self):
        if self.count <= 10:
            self.guess_character.delete(0,"end")
            self.guess_anime.delete(0,"end")
            self.guess_anime.focus_set()
        else:
            mb.showinfo("Congrats","You reached the end\nYour Score:{}/100".format(self.score))
            self.count = 1
            self.score = 0
            self.guess_character.delete(0,"end")
            self.guess_anime.delete(0,"end")

    def main(self):
        pygame.init()
        pygame.mixer.init()
        self.root.geometry("475x445+450+185")
        self.root.resizable(False,False)
        self.root.title("Guessing Game")
        anime = tk.StringVar()
        character=tk.StringVar()

        img = Image.open('lelouch.png')
        img = img.convert("RGBA")
        data=img.getdata() #list of tuples
        newData=[]
        for i in data:
            i=i[:3]
            i=i+(120,)
            newData.append(i)
        img.putdata(newData)
        img = img.resize((480,450))
        bg= ImageTk.PhotoImage(img)

        canvas= tk.Canvas(self.root)
        canvas.pack(expand=True, fill= "both")
        canvas.create_image(0,0,image=bg,anchor="nw")

        self.score = 0
        choose = tk.Label(text="Guess the Anime and Character name",font=("arial",18,"bold"),fg="white",bg="black").place(x=22,y=0)
        foot = tk.Label(text="written by:Tarun R Jain",bg="black",fg="white").place(x=160,y=420)
        self.scores = tk.Label(text="Score={}".format(self.score),font=("arial",16,"bold"))
        self.scores.place(x=200,y=50)

        text1 = tk.Label(text="Anime Name:",font=("arial",15,"bold"),fg="white",bg="black").place(x=50,y=190)
        text2 = tk.Label(text="Character Name:",font=("arial",15,"bold")).place(x=30,y=260)
        play_dialouge = tk.Button(text="Play Me First",font=("arial",12,"bold"),bd=3,command=self.play,bg="black",fg="aqua").place(x=190,y=100,width=120,height=45)

        self.guess_anime = tk.Entry(textvariable=anime,bd=5,font=("arial",12,"bold"))
        self.guess_anime.focus_set()
        self.guess_anime.place(x=200,y=180,width=200,height=50)
        self.guess_character = tk.Entry(textvariable=character,bd=5,font=("arial",12,"bold"))
        self.guess_character.place(x=200,y=250,width=200,height=50)
        check = tk.Button(text="Check Result",font=("arial",12,"bold"),bd=5,command=self.result,bg="purple",fg="white").place(x=320,y=320,width=120,height=50)
        self.root.mainloop()

if __name__ == '__main__':
    game = Game(tk.Tk())
    game.main()