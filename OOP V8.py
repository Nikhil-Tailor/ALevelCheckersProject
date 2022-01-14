import tkinter as tk
import time
import datetime
import sqlite3
import random
Font= ("Verdana", 12)
user=[]

class start(tk.Tk): #This sets up the class for the frame with tkinter
    def __init__(self,*args,**kwargs):
        
        tk.Tk.__init__(self,*args,**kwargs)
        container = tk.Frame(self)
        container.pack(side="top",fill="both", expand = True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        #self.frames={}

        frame = StartPage(container,self)
       # self.frames[StartPage] = frame
        frame.grid(row=0, column = 0, sticky="nsew")
        #self.showframe(StartPage)


    #def showframe(self,cont):

     #   frame = self.frames[cont]
        frame.tkraise()
   

class StartPage(tk.Frame):#This class uses the other class frame in order to show the tkinter images

    def __init__(self,parent,controller):
        tk. Frame.__init__(self,parent)
        self.player=1

        self.coList1=[]
        self.coList1=self.coListf(65,1,8,9,2,7,10,1,6)#This uses the coListf function to create a list to represent where the pieces are


        self.coList2=[]
        self.coList2=self.coListf(77,2,1,10,1,2,9,2,3)#The coListf function is reusable so that is works with both players
        self.canvas = tk.Canvas(self, width=800, height=800,bg="white")#Makes the tkinter canvas
        




        self.canvas.pack()#Shows the tkinter canvas
        #self.user()
        self.draw()#Draws the tkinter grid using the draw function

        self.label = tk.Label(self, text="Start Game", font=Font,anchor="s")#Show the label that says start game

        self.label.pack(side="left" ,pady=10,padx=10)#makes the label


        self.label3 = tk.Label(self, text="", font=Font,anchor="s")
        self.start = time.time()#Finds the current time
        self.updateClock()#starts the clock funtion to workout the time taken
        self.label3.pack(side="left", pady=10,padx=10)


        self.buttonRestart=tk.Button(self,text="Restart",font=Font,anchor="s",command=lambda:self.restart(app))#This button restarts the game,calling the restart function when pressed
        self.buttonRestart.pack(side="left")



        self.p1score=0
        self.p2score=0

        self.winner=0


        self.xlist=[]
        self.ylist=[]

        
        self.img = tk.PhotoImage(file="circleW.png")##This sets the image file to be used as a aarable

        self.imgB = tk.PhotoImage(file="circleBr.png")

        self.king1=tk.PhotoImage(file="circleWK.png")
        self.king2=tk.PhotoImage(file="circleBrK.png")

        
        self.player=1
        self.t=False

        self.image1 = self.canvas.create_image(0, 700, anchor=tk.NW, image=self.img)#Puts the image on the tkinter canvas
        self.image2 = self.canvas.create_image(200, 700, anchor=tk.NW, image=self.img)
        self.image3 = self.canvas.create_image(400, 700, anchor=tk.NW, image=self.img)
        self.image4 = self.canvas.create_image(600, 700, anchor=tk.NW, image=self.img)
        self.image5 = self.canvas.create_image(100, 600, anchor=tk.NW, image=self.img)
        self.image6 = self.canvas.create_image(300, 600, anchor=tk.NW, image=self.img)
        self.image7 = self.canvas.create_image(500, 600, anchor=tk.NW, image=self.img)
        self.image8 = self.canvas.create_image(700, 600, anchor=tk.NW, image=self.img)
        self.image9 = self.canvas.create_image(0, 500, anchor=tk.NW, image=self.img)
        self.image10 = self.canvas.create_image(200, 500, anchor=tk.NW, image=self.img)
        self.image11= self.canvas.create_image(400, 500, anchor=tk.NW, image=self.img)
        self.image12= self.canvas.create_image(600, 500, anchor=tk.NW, image=self.img)



        

        self.image13 = self.canvas.create_image(100, 0, anchor=tk.NW, image=self.imgB)
        self.image14 = self.canvas.create_image(300, 0, anchor=tk.NW, image=self.imgB)
        self.image15 = self.canvas.create_image(500, 0, anchor=tk.NW, image=self.imgB)
        self.image16 = self.canvas.create_image(700, 0, anchor=tk.NW, image=self.imgB)
        self.image17 = self.canvas.create_image(000, 100, anchor=tk.NW, image=self.imgB)
        self.image18 = self.canvas.create_image(200, 100, anchor=tk.NW, image=self.imgB)
        self.image19 = self.canvas.create_image(400, 100, anchor=tk.NW, image=self.imgB)
        self.image20 = self.canvas.create_image(600, 100, anchor=tk.NW, image=self.imgB)

        self.image21 = self.canvas.create_image(100, 200, anchor=tk.NW, image=self.imgB)
        self.image22 = self.canvas.create_image(300, 200, anchor=tk.NW, image=self.imgB)
        self.image23 = self.canvas.create_image(500, 200, anchor=tk.NW, image=self.imgB)
        self.image24 = self.canvas.create_image(700, 200, anchor=tk.NW, image=self.imgB)



        
        self.king=False
        self.currentpiece=""
        
    def restart(self,app):#This is the restart funtion that sets varables back to an original value

        self.coList1=[]
        self.coList1=self.coListf(65,1,8,9,2,7,10,1,6)



        self.coList2=[]
        self.coList2=self.coListf(77,2,1,10,1,2,9,2,3)


        self.start = time.time()
        self.updateClock()
        self.label3.pack(side="left", pady=10,padx=10)

        self.p1score=0
        self.p2score=0




        self.xlist=[100]
        self.ylist=[100]

        
        self.img = tk.PhotoImage(file="circleW.png")

        self.imgB = tk.PhotoImage(file="circleBr.png")

        self.king1=tk.PhotoImage(file="circleWK.png")
        self.king2=tk.PhotoImage(file="circleBrK.png")

        
        self.player=1
        self.label.config(text="Start Game")
        
        self.t=False
        self.image1 = self.canvas.create_image(0, 700, anchor=tk.NW, image=self.img)
        self.image2 = self.canvas.create_image(200, 700, anchor=tk.NW, image=self.img)
        self.image3 = self.canvas.create_image(400, 700, anchor=tk.NW, image=self.img)
        self.image4 = self.canvas.create_image(600, 700, anchor=tk.NW, image=self.img)
        self.image5 = self.canvas.create_image(100, 600, anchor=tk.NW, image=self.img)
        self.image6 = self.canvas.create_image(300, 600, anchor=tk.NW, image=self.img)
        self.image7 = self.canvas.create_image(500, 600, anchor=tk.NW, image=self.img)
        self.image8 = self.canvas.create_image(700, 600, anchor=tk.NW, image=self.img)
        self.image9 = self.canvas.create_image(0, 500, anchor=tk.NW, image=self.img)
        self.image10 = self.canvas.create_image(200, 500, anchor=tk.NW, image=self.img)
        self.image11= self.canvas.create_image(400, 500, anchor=tk.NW, image=self.img)
        self.image12= self.canvas.create_image(600, 500, anchor=tk.NW, image=self.img)



        

        self.image13 = self.canvas.create_image(100, 0, anchor=tk.NW, image=self.imgB)
        self.image14 = self.canvas.create_image(300, 0, anchor=tk.NW, image=self.imgB)
        self.image15 = self.canvas.create_image(500, 0, anchor=tk.NW, image=self.imgB)
        self.image16 = self.canvas.create_image(700, 0, anchor=tk.NW, image=self.imgB)
        self.image17 = self.canvas.create_image(000, 100, anchor=tk.NW, image=self.imgB)
        self.image18 = self.canvas.create_image(200, 100, anchor=tk.NW, image=self.imgB)
        self.image19 = self.canvas.create_image(400, 100, anchor=tk.NW, image=self.imgB)
        self.image20 = self.canvas.create_image(600, 100, anchor=tk.NW, image=self.imgB)
        self.image21 = self.canvas.create_image(100, 200, anchor=tk.NW, image=self.imgB)
        self.image22 = self.canvas.create_image(300, 200, anchor=tk.NW, image=self.imgB)
        self.image23 = self.canvas.create_image(500, 200, anchor=tk.NW, image=self.imgB)
        self.image24 = self.canvas.create_image(700, 200, anchor=tk.NW, image=self.imgB)

        
        self.king=False
        self.currentpiece=""
        
    def updateClock(self):#This is the clock function that uses the original time and the current time to display the taken in the game
        #self.restart(app)
        
        now = time.time()
        total=now-self.start
        total=int(total)

        mins=total//60#Uses DIV to calulate the amount of total miniutes in taken in the game
        sec=total%60#Uses modulus to secconds part of the time
        txt=("\t\t"+str(mins)+" Minutes  "+str(sec)+" Secconds\t\t\t\t")
        #total=now-self.start
        self.label3.configure(text=txt)
        self.after(1000, self.updateClock)#This repeats the fucntion so that is keeps displaying the current time taken
        return mins,sec

    def database(self,mins,sec):#This function imputs data into the database
        mins=str(mins)
        sec=str(sec)
        time=mins+" mins "+sec+" sec "

        with sqlite3.connect ("CheckersTesting.db") as db:#Selects the maxium gameID in oder to find the next gameID keeping it a unique primary key
            cursor=db.cursor()
            cursor.execute("SELECT MAX(GameID) FROM Result")
            db.commit()
            result = cursor.fetchall()

        resultlist=result[0]
        resultchar=[]
        for i in resultlist:
            resultchar.append(i)

        gameid=int(resultchar[0]+1)

        #SELECT MAX(GameID) FROM Game 
        data=[]
        #x="r"+str(random.randint(1,1000000))
        if self.winner==1:
            win="Won"
        elif self.winner==2:
            win="Lost"
        else:
            win=""

        data.append(gameid)
        data.append(win)
        data.append(user[0])
        with sqlite3.connect ("CheckersTesting.db") as db:
            cursor=db.cursor()
            cursor.execute("insert into Result values (?,?,?)", data)#This inputs player 1's information into the database
            db.commit()

        if self.winner==2:
            win="Won"
        elif self.winner==1:
            win="Lost"
        else:
            win=""
        data=[]
        data.append(gameid)
        data.append(win)
        data.append(user[1])
        with sqlite3.connect ("CheckersTesting.db") as db:
            cursor=db.cursor()
            cursor.execute("insert into Result values (?,?,?)", data)#This inputs player 2's information into the database
            db.commit()

        data=[]
        data.append(gameid)
        #print(gameID)
        data.append(datetime.date.today())
        data.append(mins)
        data.append(sec)
        with sqlite3.connect ("CheckersTesting.db") as db:
            cursor=db.cursor()
            cursor.execute("insert into Game values (?,?,?,?)", data)#This inputs data into the game table of the database so the the database if fully normalised
            db.commit()
        
        self.showdata()



        
    def showdata(self):#This function prints data from the database


        data=[]
        data.append(user[0])
        with sqlite3.connect ("CheckersTesting.db") as db:
            cursor=db.cursor()
            cursor.execute("SELECT UserID, Score FROM Result where UserID=?",data)#Shows all the scores from player 1
            db.commit()
            result = cursor.fetchall()


        
        p1win=0
        p1loss=0
        for i in result:
            if i[1]=="Won":
                p1win+=1
            elif i[1]=="Lost":
                p1loss+=1
            


        print("\n\nPlayer 1 - "+user[0]+"\n"+str(p1win)+" games won in total\n"+str(p1loss)+" games lost in total\n\n")
            
        #print(result)
        #for i in result:
        #    for x in i:
        #            print(x,end="\t")
        #    print("\n")

        data=[]
        data.append(user[1])
        with sqlite3.connect ("CheckersTesting.db") as db:
            cursor=db.cursor()
            cursor.execute("SELECT UserID, Score FROM Result where UserID=?",data)#Shows all the scores from player 2
            db.commit()
            result = cursor.fetchall()

        p2win=0
        p2loss=0
        for i in result:
            if i[1]=="Won":
                p2win+=1
            elif i[1]=="Lost":
                p2loss+=1
            


        print("\n\nPlayer 2 - "+user[1]+"\n"+str(p2win)+" games won in total\n"+str(p2loss)+" games lost in total\n\n")
            #print(i)
            #print("\n")
            #for x in i:
                    #print(x,end="\t")
            #print("\n")




        #This tests The Join showing information from more than one database

        prt=["GameID","Winner","Looser","Date","\tMins","Sec"]
        
        with sqlite3.connect ("CheckersTesting.db") as db:
            cursor=db.cursor()
            cursor.execute("select Resulta.GameID , Resulta.UserID as 'Winner',Resultb.UserID  as 'Looser',Game.Date,Game.Minutes,Game.Secconds from Result Resulta, Result Resultb INNER JOIN Game ON Resulta.GameID  = Game.GameID where Resulta.GameID=Resultb.GameID and Resulta.Score='Won' and Resultb.Score='Lost'")#SELECT Result.GameID, Result.Score,Game.Date,Game.Minutes,Game.Secconds FROM Result INNER JOIN Game ON Result.GameID  = Game.GameID")# WHERE userID=*")
            db.commit()
            result = cursor.fetchall()
        result.insert(0,prt)
        for i in result:
            for x in i:
                    print(x,end="\t")
            print("\n")

        #SELECT UserID, Score FROM Result WHERE userID=*
    def coListf(self,letter,x,y,maxx,newx,newy,xchange,xnew2,ynew2):#This uses nested for loops to make lists to show reperesnt when the game pieces start
        c=0
        c1=0
        l=[]
        for j in range(12):
            column = []
            for i in range(3):
                if i==0:
                    column.append(chr(letter))
                    letter=letter+1
                elif i==1:
                    column.append(x)
                    x=x+2
                    if x==maxx:
                        x=newx

                elif i==2:
                    column.append(y)
                    if (x==newx) and(c==0):
                        y=newy
                        c=1
                    elif x==xchange:
                            x=xnew2
                            y=ynew2
                            

            l.append(column)

        return l






        
    def draw(self):#Uses nested for loop with if loops creating squares to make a game board
        #self.restart(app)
        fill=["black","white"]
        for row in range(8):
            for column in range(8):
                if fill == ["black","white"]:#The colour changes here every square 
                     fill = ["white","black"]
                else:
                     fill=["black","white"]

                self.canvas.create_rectangle ( 0+(row*100), 0+(column*100), 100+(row*100), 100+(column*100),fill=fill[0],outline=fill[0])

            
            if fill == ["black","white"]:#The colour changes here every row 
                fill = ["white","black"]
            else:
                fill=["black","white"]
                


        self.canvas.bind("<Button-1>", self.findCo)



    def findCo(self,event):#This takes the x and y coordinates of where the user has clicked and uses DIV to calulate where on a grid they clicked

            xcoordinate=event.x
            ycoordinate=event.y




            xc=(1+(xcoordinate//100))#Div calculating the position
            self.xlist.append(xc)#Adds the postion to a running list of every co ordinate the user has clicked

            yc=(1+(ycoordinate//100))
            self.ylist.append(yc)






            self.testmove()#Starts the testmovve function

    def testmove(self):
        #This function ditermins weather the user has made a valid more, ussing the list of all co ordinates click and what to to next


        label = tk.Label(self, text=self.player, font=Font)
       
        validmove=False

        if self.player ==1:#This looks the the previous two postions click and detims if it can use it to make a mive
            coList=self.coList1
            if self.t==True and ((self.xlist[-2])-(self.xlist[-1])==-2) and ((self.ylist[-2])-(self.ylist[-1])==2):
                #delate piece
                self.move(1,2,-2,200,-200)
            elif self.t==True and ((self.xlist[-2])-(self.xlist[-1])==2) and ((self.ylist[-2])-(self.ylist[-1])==2):
                self.move(1,-2,-2,-200,-200)
            elif self.king==True and self.t==True and ((self.xlist[-2])-(self.xlist[-1])==2) and ((self.ylist[-2])-(self.ylist[-1])==-2):
                #delate piece
                self.move(2,-2,2,-200,200)
            elif self.king==True and self.t==True and ((self.xlist[-2])-(self.xlist[-1])==-2) and ((self.ylist[-2])-(self.ylist[-1])==-2):
                self.move(2,2,2,200,200)






            elif (self.king==True)and(self.t== True) and ((self.xlist[-2])-(self.xlist[-1])==1) and ((self.ylist[-2])-(self.ylist[-1])==-1):
            #Down and left
                self.move(1,-1,1,-100,100)

            elif (self.king==True) and (self.t==True) and ((self.xlist[-2])-(self.xlist[-1])==-1) and ((self.ylist[-2])-(self.ylist[-1])==-1):
            #down and right
                self.move(1,1,1,100,100)



            elif self.t==True and ((self.xlist[-2])-(self.xlist[-1])==1) and ((self.ylist[-2])-(self.ylist[-1])==1):
            #This part of the code checks if a player game go up and left
                self.move(1,-1,-1,-100,-100)
                
            elif self.t==True and ((self.xlist[-2])-(self.xlist[-1])==-1) and ((self.ylist[-2])-(self.ylist[-1])==1):
            #Checks if a piece can go up and right
                self.move(1,1,-1,100,-100)
        elif self.player== 2:
            coList=self.coList2


            if self.t==True and ((self.xlist[-2])-(self.xlist[-1])==2) and ((self.ylist[-2])-(self.ylist[-1])==-2):
                #delate piece
                self.move(2,-2,2,-200,200)
            elif self.t==True and ((self.xlist[-2])-(self.xlist[-1])==-2) and ((self.ylist[-2])-(self.ylist[-1])==-2):
                self.move(2,2,2,200,200)

            if self.king==True and self.t==True and ((self.xlist[-2])-(self.xlist[-1])==-2) and ((self.ylist[-2])-(self.ylist[-1])==2):
                #delate piece
                self.move(1,2,-2,200,-200)
            elif self.king == True and self.t==True and ((self.xlist[-2])-(self.xlist[-1])==2) and ((self.ylist[-2])-(self.ylist[-1])==2):
                self.move(1,-2,-2,-200,-200)


        
            elif self.t== True and ((self.xlist[-2])-(self.xlist[-1])==1) and ((self.ylist[-2])-(self.ylist[-1])==-1):
            #Checks if a piece can go down and left
                self.move(2,-1,1,-100,100)
                
            elif self.t==True and ((self.xlist[-2])-(self.xlist[-1])==-1) and ((self.ylist[-2])-(self.ylist[-1])==-1):
            #Checks if a piece can go down and right
                self.move(2,1,1,100,100)


            elif self.king==True and self.t==True and ((self.xlist[-2])-(self.xlist[-1])==1) and ((self.ylist[-2])-(self.ylist[-1])==1):
            #Checks if a piece can go up and left
                self.move(2,-1,-1,-100,-100)
                
            elif self.king==True and self.t==True and ((self.xlist[-2])-(self.xlist[-1])==-1) and ((self.ylist[-2])-(self.ylist[-1])==1):
            #Checks if a piece can go up and right
                self.move(2,1,-1,100,-100)

        if self.player==1:
            coList=self.coList1
        else:
            coList=self.coList2
        playerlabeltext="Player " + str(self.player)+"    "

        self.label.config(text=playerlabeltext)
        self.t=False
        self.king=False

        if self.coList1==[] or self.coList2==[]:
            if self.coList1==[]:
                self.winner=1
            elif  self.coList2==[]:
                self.winner=2
                
            empty=True
            mins,sec=self.updateClock()
            self.database(mins,sec)


        else:
            empty=False


            
        if empty==False:#This checks if the user clicked on a piece, if the have it sets the varable "t" to true meaning it the nest move could be valid
            for i in coList:
                if (i[1] == self.xlist[-1])and (i[2]==self.ylist[-1]):
                   

                    self.currentpiece=i[0]
                    self.t=True


                try:
                    if i[3]=="King":
                        if self.currentpiece==i[0]:
                            self.king=True
                except:
                    "list index out of range"

    def move(self,player,testx,testy,xmove,ymove):#Makes the move if it is valid
        colist=[]

        if self.player==1:
            coList=self.coList1
            coList2=self.coList2
           
        elif self.player==2:
            coList=self.coList2
           
            coList2=self.coList1


    
        validmove=True

        currentposx=self.xlist[-2]#Sets the current psotions as a varable
        currentposy=self.ylist[-2]

        piecego=[]
        if (xmove==200)or (xmove==-200):#Checks if the is a piece from the other player that can be taken
            validmove=False
            
            for i in coList2:
                if (currentposx+(testx/2)==i[1] and currentposy+(testy/2)==i[2]):

                    i[1]
                    validmove=True
                    peicego=i[0]

            if validmove==True:
                    for i in coList2:
                        if (currentposx+(testx)==i[1] and currentposy+(testy)==i[2]):
                            validmove=False
            if validmove==True:
                deletepeice=True
                delete=self.imagefunction(peicego)
                self.canvas.move(delete, 5000, 5000)#Makes the game piece not visible
                if player==1:
                    self.p1score+=1
                elif player==2:    
                    self.p2score+=1
                self.p1score+=1
                for i in coList2:
                    if i[0]==peicego:
                        coList2.remove(i)
                


            
        else:    
            if validmove==True:
                for i in self.coList1:
                    if (currentposx+testx==i[1] and currentposy+testy==i[2]):
                        validmove=False
            if validmove==True:
                for i in self.coList2:
                    if (currentposx+testx==i[1] and currentposy+testy==i[2]):
                        validmove=False
                              
            
        if validmove==True:


            for i in coList:
                if i[0]==self.currentpiece:

                    i[1]=i[1]+testx
                    i[2]=i[2]+testy




            x=self.imagefunction(self.currentpiece)
            time.sleep(0.17)
            
            self.canvas.move(x, xmove, ymove)#Moves the piece if valid


            
            if self.player==1:
                self.coList=coList=self.coList1

            elif self.player==2:
                self.coList2=coList=self.coList2



            if self.player == 1:#Swaps to next player
                self.player=2
            elif self.player==2:
                self.player=1



            if player==1:#Detects if a game piece has become a king
                
                for i in self.coList1:
                    if i[2]==1:
                        i.append("King")
                        x=self.imagefunction(i[0])
                        self.canvas.itemconfigure(x, image=self.king1)


                        

            elif player==2:
                
                for i in self.coList2:
                    if i[2]==8:
                        i.append("King")
                        x=self.imagefunction(i[0])
                        self.canvas.itemconfigure(x, image=self.king2)










    def imagefunction(self,currentpiece):#Fuction to ditermin which peice image should move


        if currentpiece == "A":
            x=self.image1
        elif currentpiece == "B":
            x=self.image2
        elif currentpiece == "C":
            x=self.image3
        elif currentpiece == "D":
            x=self.image4
            
        elif currentpiece == "E":
            x=self.image5
        elif currentpiece == "F":
            x=self.image6
        elif currentpiece == "G":
            x=self.image7
        elif currentpiece == "H":
            x=self.image8
            
        elif currentpiece == "I":
            x=self.image9
        elif currentpiece == "J":
            x=self.image10
        elif currentpiece == "K":
            x=self.image11
        elif currentpiece == "L":
            x=self.image12
            
        elif currentpiece == "M":
            x=self.image13
        elif currentpiece == "N":
            x=self.image14
        elif currentpiece == "O":
            x=self.image15
        elif currentpiece == "P":
            x=self.image16
            
        elif currentpiece == "Q":
            x=self.image17
        elif currentpiece == "R":
            x=self.image18
        elif currentpiece == "S":
            x=self.image19
        elif currentpiece == "T":
            x=self.image20

        elif currentpiece == "U":
            x=self.image21
        elif currentpiece == "V":
            x=self.image22
        elif currentpiece == "W":
            x=self.image23
        elif currentpiece == "X":
            x=self.image24
        else:
            x=self.image1

        

        return x



#Functions to show a log in page

def enterpw(username,password,player,message):

    global correct

    un=username.get()
    pw=password.get()



    username.delete(first=0,last=22)
    password.delete(first=0,last=22)    

    data=[]
    data.append(un)


    #Selects password from the database to check if the password if valid
    with sqlite3.connect ("CheckersTesting.db") as db:
        cursor=db.cursor()
        cursor.execute("SELECT Password FROM User WHERE UserID=?",data)
        db.commit()
        result = cursor.fetchall()
    test="('"+pw+"',)"
    if result==[]:
        valid=False
    elif str(result[0])==test:


        valid=True
    else:valid=False

    if (valid==True) and (len(user)==0 or len(user)==1):
        message.config(text="")
        user.append(un)
        if len(user)==1:

            player.config(text="Player Two Login")

        elif len(user)==2:#If both users have enetered the password corrrectly the user can press play and the game will start
            
            tk.Button(master, text='Play Game', command=master.destroy).grid(row=5, column=0, sticky=tk.W, pady=4)
            player.config(text="Press Play!")
            correct=True
                        
    else:
        if result==[]:
            message.config(text="User Not Found")
        else:
            if len(user)!=2:
                message.config(text="Password Incorrect")


def newuser(username,password,player,message):#Fucntion make a nuw user, inputing it onto the database
    un=username.get()
    pw=password.get()
    indb=True


    if len(user)!=2:
        #Validation for username a password so that the username and password is a acceptable lenght
        if len(un)<3:
            message.config(text="Username too small")
            indb=False
        elif len(pw)<5:
            message.config(text="Password must have over 5 characters")
            indb=False
        upper=False
        number=False
        if indb==True:

            for i in pw:
                    if i.isupper()==True:
                            upper=True
                    if i.isdigit() == True:
                            number=True

        if indb==True and upper==False:
            indb=False
            message.config(text="Password must have at least one upper letter")
        elif indb==True and number ==False:
            indb=False
            message.config(text="Password must have at least one number")

        if indb==True:
            data=[]
            data.append(un)
            data.append(pw)
            try:
                with sqlite3.connect ("CheckersTesting.db") as db:
                    cursor=db.cursor()
                    cursor.execute("insert into User values (?,?)", data)#Enters the data onto the database
                    db.commit()
                    message.config(text="New User Made")
            except:# UNIQUE constraint failed:
                message.config(text="Username Already taken")






def player():#This creates the tkinter log in page using grid
    global correct

    message = tk.Label(master, text="")
    message.grid(column=1, row=0)

    player = tk.Label(master, text="Player One Login")
    player.grid(row=0)


    usernameL=tk.Label(master,text="Username")
    usernameL.grid(row=1)
    passwordL = tk.Label(master, text="Password")
    passwordL.grid(column=0, row=2)

    usernameE = tk.Entry(master)
    passwordE = tk.Entry(master)

    usernameE.grid(row=1, column=1)
    passwordE.grid(row=2, column=1)


    #These are buttons that use data from the entries, using funtions to log in and make new users
    tk.Button(master, text='Make New User', command=lambda:newuser(usernameE,passwordE,player,message)).grid(row=4, column=0, sticky=tk.W, pady=4)
    tk.Button(master, text='Login', command=lambda:enterpw(usernameE,passwordE,player,message)).grid(row=4, column=1, sticky=tk.W, pady=4)
    
correct=False

while correct==False:
    master = tk.Tk()

    player()#Starts the login and gets the player usernames to be used later in the programm

    tk.mainloop()#starts tkinter

        


app=start()#Starts the tkinter for the game
app.mainloop()

































































