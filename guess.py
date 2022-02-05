import tkinter as tk
import pygame,random
from tkinter import messagebox as mb

def play():
    global choice
    choice = str(random.randint(1,10))+'.ogg'
    try:
        pygame.mixer.music.load(choice)
        pygame.mixer.music.play(loops=1)
    except pygame.error:
        print("YO! FILE ERROR OCCURED \n While excecuting the code make sure it is in directory where file is downloaded \n Like check Present directory")

def check(anime_name,character_name):
    value = guess_anime.get().lower().rstrip()
    char = guess_character.get().lower().rstrip()
    if value in anime_name and character_name in char:
        mb.showinfo("Amazing","You are man of culture \n Play Again for different anime")
        clear()
    else:
        mb.showerror("This isn't for you","So your a normie with no anime taste \n Try Again if Typo")

def result():
    try:
        if len(guess_anime.get()) == 0 or len(guess_character.get()) == 0:
            mb.showerror("Try Again","Yo enter Something")
        else:
            if choice == '1.ogg':
                check("one piece","luffy")
            if choice == '2.ogg':
                check(["attack on titan","shingeki no kyojin"],"levi")
            if choice == '3.ogg':
                check(["naruto","naruto shippuden"],"naruto")
            if choice == '4.ogg':
                check("death note","light")
            if choice == '5.ogg':
                check(["love is war","kaguya sama","kaguya-sama love is war","kaguya sama love is war"],"kaguya")
            if choice == '6.ogg':
                check("jujutsu kaisen","gojo")
            if choice == '7.ogg':
                check("kakegurui","yumeko")
            if choice == '8.ogg':
                check("gintama","gintoki")
            if choice == '9.ogg':
                check("demon slayer","giyuu")
            if choice == '10.ogg':
                check("violet evergarden","violet")
    except NameError:
        mb.showerror("Play Music","Play Button was not pressed")

def clear():
    guess_character.delete(0,"end")
    guess_anime.delete(0,"end")
    guess_anime.focus_set()

def main():
    global guess_anime,guess_character,next
    pygame.init()
    pygame.mixer.init()
    root = tk.Tk()
    root.geometry("475x445+450+185")
    root.minsize(475,445)
    root.maxsize(475,445)
    root.title("Guessing Game")
    anime = tk.StringVar()
    character=tk.StringVar()
    canva = tk.Canvas(bg="chocolate")
    canva.place(width=500,height=500)
    choose = tk.Label(text="Guess the Anime and Character name",font=("arial",18,"bold"),fg="white",bg="black").place(x=22,y=0)
    foot = tk.Label(text="written by:Tarun R Jain",bg="black",fg="white").place(x=160,y=420)
    level = tk.Label(text="Difficulty Level:Easy",font=("arial",15,"bold")).place(x=145,y=40)
    text1 = tk.Label(text="Anime",font=("arial",15,"bold"),fg="white",bg="black").place(x=100,y=190)
    text2 = tk.Label(text="Character",font=("arial",15,"bold")).place(x=80,y=260)
    play_dialouge = tk.Button(text="Play Me First",font=("arial",12,"bold"),bd=3,command=play,bg="purple",fg="aqua").place(x=190,y=100,width=120,height=45)

    guess_anime = tk.Entry(textvariable=anime,bd=5,font=("arial",12,"bold"))
    guess_anime.focus_set()
    guess_anime.place(x=185,y=180,width=200,height=50)
    guess_character = tk.Entry(textvariable=character,bd=5,font=("arial",12,"bold"))
    guess_character.place(x=185,y=250,width=200,height=50)
    check = tk.Button(text="Check Result",font=("arial",12,"bold"),bd=5,command=result,bg="purple",fg="aqua").place(x=320,y=320,width=120,height=50)
    root.mainloop()

if __name__ == '__main__':
    main()