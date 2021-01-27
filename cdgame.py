from tkinter import *
import time
import random
total=[None]*24
images=[None]*24
texts=[None]*24
recbtn=None
default=None
class first:
  def firstone(self):
    cg=Tk()
    cg.title('card game')
    cg.geometry('605x527')
    loc=r'logo.png'
    images=PhotoImage(file=loc)
    l=Label(cg,image=images)
    l.place(x=0,y=0)
    cg.after(2500,lambda:cg.destroy())
    cg.mainloop()
  def title(self):
    bg=Tk()
    bg.title('card game')
    bg.geometry('541x560')
    loc=r'start.png'
    images=PhotoImage(file=loc)
    l=Label(bg,image=images)
    l.place(x=0,y=0)
    bg.after(2500,lambda:bg.destroy())
    bg.mainloop()
 
    
class Program:
    click=1
    match=0
    u_timer=0
    v_timer=0

    def main(self):
        global total,images,texts,default
        def checkwin():
          if(Program.match==18):
            Program.v_timer=time.time()
            now=Program.v_timer-Program.u_timer
            from tkinter import messagebox
            import sys
            messagebox.showinfo("GAME OVER","ALL MATCHES FOUND PERFECTLY\nTIME TcgEN:  %.2f seconds"%now)
            root.destroy()
            sys.exit()

        def checkmatch(b):
            if(b['text']==recbtn['text'] and b!=recbtn):
                b.destroy()
                recbtn.destroy()
                Program.match+=1
                checkwin()
            else:
                b['image']=default
                recbtn['image']=default
                
            

        def but1(b):
            global images,recbtn
            b['image']=images[0]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but2(b):
            global images,recbtn
            b['image']=images[1]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but3(b):
            global images,recbtn
            b['image']=images[2]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but4(b):
            global images,recbtn
            b['image']=images[3]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but5(b):
            global images,recbtn
            b['image']=images[4]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but6(b):
            global images,recbtn
            b['image']=images[5]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but7(b):
            global images,recbtn
            b['image']=images[6]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but8(b):
            global images,recbtn
            b['image']=images[7]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but9(b):
            global images,recbtn
            b['image']=images[8]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but10(b):
            global images,recbtn
            b['image']=images[9]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but11(b):
            global images,recbtn
            b['image']=images[10]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but12(b):
            global images,recbtn
            b['image']=images[11]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but13(b):
            global images,recbtn
            b['image']=images[12]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but14(b):
            global images,recbtn
            b['image']=images[13]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but15(b):
            global images,recbtn
            b['image']=images[14]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but16(b):
            global images,recbtn
            b['image']=images[15]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but17(b):
            global images,recbtn
            b['image']=images[16]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but18(b):
            global images,recbtn
            b['image']=images[17]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but19(b):
            global images,recbtn
            b['image']=images[18]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but20(b):
            global images,recbtn
            b['image']=images[19]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but21(b):
            global images,recbtn
            b['image']=images[20]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but22(b):
            global images,recbtn
            b['image']=images[21]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but23(b):
            global images,recbtn
            b['image']=images[22]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

        def but24(b):
            global images,recbtn
            b['image']=images[23]
            if(Program.click==1):
                recbtn=b
                Program.click=2

            elif(Program.click==2):
                root.after(200,lambda:checkmatch(b))
                Program.click=1

                       
        Program.u_timer=time.time()                            
        root=Tk()
        root.geometry('600x650')
        root.title('MEMORY GAME')

        loc1=r'a.png'
        loc2=r'2.png'
        loc3=r'3.png'
        loc4=r'4.png'
        loc5=r'5.png'
        loc6=r'6.png'
        loc7=r'7.png'
        loc8=r'8.png'
        loc9=r'9.png'
        loc10=r'10.png'
        loc11=r'j.png'
        loc12=r'q.png'
        loc13=r'k.png'
        loc=r'back.png'

        default=PhotoImage(file=loc)
        total=[loc1,loc2,loc3,loc4,loc5,loc6,loc7,loc8,loc9,loc10,loc11,loc12,loc13]
        templist=total
        #print(templist)
        list2=[None]*4
        for j in range(0,4,1):
              list2[j]=random.choice(templist)
              templist.remove(list2[j])
        total=[loc1,loc2,loc3,loc4,loc5,loc6,loc7,loc8,loc9,loc10,loc11,loc12,loc13]
        total=total+list2
        total=total+total
        
        for i in range(0,23,1):
            x=random.choice(total)
            images[i]=PhotoImage(file=x)
            texts[i+1]=str(x)
            total.remove(x)
                        
            


        c=Canvas(root,bg='black',height=500,width=500)
        c.place(x=0,y=0)

        #row1
        b11=Button(root,image=default,text=texts[1],bg='white',height=95,width=88,command=lambda:but1(b11))
        b11.place(x=10,y=20)
        b12=Button(root,image=default,text=texts[2],bg='white',height=95,width=88,command=lambda:but2(b12))
        b12.place(x=105,y=20)
        b13=Button(root,image=default,text=texts[3],bg='white',height=95,width=88,command=lambda:but3(b13))
        b13.place(x=200,y=20)
        b14=Button(root,image=default,text=texts[4],bg='white',height=95,width=88,command=lambda:but4(b14))
        b14.place(x=295,y=20)
        b15=Button(root,image=default,text=texts[5],bg='white',height=95,width=88,command=lambda:but5(b15))
        b15.place(x=390,y=20)
       
        #row2
        b21=Button(root,image=default,text=texts[7],bg='white',height=95,width=88,command=lambda:but7(b21))
        b21.place(x=10,y=122)
        b22=Button(root,image=default,text=texts[8],bg='white',height=95,width=88,command=lambda:but8(b22))
        b22.place(x=105,y=122)
        b23=Button(root,image=default,text=texts[9],bg='white',height=95,width=88,command=lambda:but9(b23))
        b23.place(x=200,y=122)
        b24=Button(root,image=default,text=texts[10],bg='white',height=95,width=88,command=lambda:but10(b24))
        b24.place(x=295,y=122)
        b25=Button(root,image=default,text=texts[11],bg='white',height=95,width=88,command=lambda:but11(b25))
        b25.place(x=390,y=122)
       

        #row3
        b31=Button(root,image=default,text=texts[13],bg='white',height=95,width=88,command=lambda:but13(b31))
        b31.place(x=10,y=224)
        b32=Button(root,image=default,text=texts[14],bg='white',height=95,width=88,command=lambda:but14(b32))
        b32.place(x=105,y=224)
        b33=Button(root,image=default,text=texts[15],bg='white',height=95,width=88,command=lambda:but15(b33))
        b33.place(x=200,y=224)
        b34=Button(root,image=default,text=texts[16],bg='white',height=95,width=88,command=lambda:but16(b34))
        b34.place(x=295,y=224)
        b35=Button(root,image=default,text=texts[17],bg='white',height=95,width=88,command=lambda:but17(b35))
        b35.place(x=390,y=224)
        

        #row4
        b41=Button(root,image=default,text=texts[19],bg='white',height=95,width=88,command=lambda:but19(b41))
        b41.place(x=10,y=326)
        b42=Button(root,image=default,text=texts[20],bg='white',height=95,width=88,command=lambda:but20(b42))
        b42.place(x=105,y=326)
        b43=Button(root,image=default,text=texts[21],bg='white',height=95,width=88,command=lambda:but21(b43))
        b43.place(x=200,y=326)
        b44=Button(root,image=default,text=texts[22],bg='white',height=95,width=88,command=lambda:but22(b44))
        b44.place(x=295,y=326)
        b45=Button(root,image=default,text=texts[23],bg='white',height=95,width=88,command=lambda:but23(b45))
        b45.place(x=390,y=326)


        root.mainloop()
obj=first()
obj.firstone()
obj.title()
obj1=Program()
obj1.main()
