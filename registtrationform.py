from tkinter import *
import requests
import json
import main
from pygame import *
import pygame
import operator
root = Tk()
url = 'https://api.jsonbin.io/b/5e8c8129ff9c906bdf1d76d6'
url2 = 'https://api.jsonbin.io/b/5e8dc504753e041b892bb9d0'
headers = {'secret-key': '$2b$10$k.3JYb5rX76iK4UTiFMma.dcz.z4ymAzIDFCYzaCt3jcRGNYu/Ise'}
headers1 = {'Content-Type': 'application/json', 'secret-key': '$2b$10$k.3JYb5rX76iK4UTiFMma.dcz.z4ymAzIDFCYzaCt3jcRGNYu/Ise', 'versioning': 'false'}
root.geometry('500x500')
root.title("Registration Form")
label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)
label_1 = Label(root, text="Name",width=20,font=("bold", 10))
label_1.place(x=80,y=130)
entry_1 = Entry(root)
entry_1.place(x=240,y=130)
label_2 = Label(root, text="Password",width=20,font=("bold", 10))
label_2.place(x=68,y=180)
entry_2 = Entry(root)
entry_2.place(x=240,y=180)
usrnm = ""
def register():
    #print(entry_1.get())
    req = requests.get(url, headers=headers)
    users = req.json();
    req2 = requests.get(url2, headers=headers)
    scores = req2.json()
    #print(users["Saswat"])
    if entry_1.get() not in users:
        x = {entry_1.get(): entry_2.get()}
        global usrnm
        usrnm = entry_1.get()
        users.update(x)
        y = {entry_1.get()+"_score":0}
        scores.update(y)
        reqs = requests.put(url, json=users, headers=headers1)
        print(reqs.text)
        reqs2 = requests.put(url2, json=scores, headers=headers1)
        print(reqs2.text)
        #pygame.init()
        pygame.init()

        main.scr_size = (width,height) = (600,150)
        main.FPS = 60
        main.gravity = 0.6
        
        main.black = (0,0,0)
        main.white = (255,255,255)
        main.background_col = (235,235,235)
        
        main.high_score = 0
        
        main.screen = pygame.display.set_mode(main.scr_size)
        main.clock = pygame.time.Clock()
        pygame.display.set_caption("Dino Run ")
        
        main.jump_sound = pygame.mixer.Sound('sprites/jump.wav')
        main.die_sound = pygame.mixer.Sound('sprites/die.wav')
        main.checkPoint_sound = pygame.mixer.Sound('sprites/checkPoint.wav')
        main.main()
        #root.quit()
    #root.quit()
def login():
    req = requests.get(url, headers=headers)
    users = req.json();
    #print(users["Saswat"])
    if entry_1.get() in users:
        if users[entry_1.get()] == entry_2.get():
            #pygame.init()
            global usrnm
            usrnm = entry_1.get()
            pygame.init()
    
            main.scr_size = (width,height) = (600,150)
            main.FPS = 60
            main.gravity = 0.6
            
            main.black = (0,0,0)
            main.white = (255,255,255)
            main.background_col = (235,235,235)
            
            main.high_score = 0
            
            main.screen = pygame.display.set_mode(main.scr_size)
            main.clock = pygame.time.Clock()
            pygame.display.set_caption("Dino Run ")
            
            main.jump_sound = pygame.mixer.Sound('sprites/jump.wav')
            main.die_sound = pygame.mixer.Sound('sprites/die.wav')
            main.checkPoint_sound = pygame.mixer.Sound('sprites/checkPoint.wav')
            main.main()
        else:
            root.destroy()
    else:
        root.destroy()
        
def UpdateScore(score):
    req = requests.get(url2, headers=headers)
    scores = req.json()
    #print(scores)
    #num = scores[usrnm+"_score"]
    if(score > scores[usrnm+"_score"]):
        scores[usrnm+"_score"] = score
    scores_sorted = dict(sorted(scores.items(),key=operator.itemgetter(1),reverse=True))
    #scores_sorted = sorted(scores, key=scores.get, reverse=True)
    reqs = requests.put(url2, json=scores_sorted, headers=headers1)
    print(reqs.text)
    
    
button = Button(root, text='Register',width=20,bg='brown',fg='white', command = register).place(x=180,y=380)
button = Button(root, text='Login',width=20,bg='brown',fg='white', command = login).place(x=180,y=420)
#button.place(x=180,y=500)
#button.pack()
# it is use for display the registration form on the window
root.mainloop()
print("registration form  successfully created...")