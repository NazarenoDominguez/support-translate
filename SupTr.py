###################TKINTER####################
from tkinter import StringVar, ttk,PhotoImage,messagebox
from tkinter.constants import COMMAND
from typing import Sized
from DBSQLite import *


#pip install Pillow
from PIL import ImageTk,Image
from DBSQLite import *
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
import tkinter as tk
from tkinter import Text, ttk
import tkinter.filedialog
import tkinter.font as font
##############traductor google##################
from googletrans import Translator

translator = Translator()
################## time  #######################
import time
################### PDF #########################
#pip install tkPDFViewer
from tkPDFViewer import tkPDFViewer as pdf 
showpdf = pdf.ShowPdf()
################## docs ########################
#pip install python-docx
from docx import Document


#########################swicht
is_on = True
#########################

class APP(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.configure(bg = "#314252")
        self.title('Support translate')
        self.iconbitmap('IMG/traductor.ico')
        self.style = ttk.Style()
        #######################################
        
        self.style.theme_use('clam')
        self.style.configure('Treeview.Heading',background='#215D6D',border=0,foreground='white',font=('Arial',12))
        self.style.configure('TNotebook',background='#215D6D',border=0,font=('Arial',12),tabmargins= [2, 5, 2, 0])
        self.style.map("TNotebook.Tab", background=[("selected", '#215D6D')], foreground=[("selected", 'white')])
        self.style.configure("TNotebook.Tab", background='#1A2F34', foreground='white')

        
    
        #######################################
        
        
        
        
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))

        #Main frame to change the windows
        contenedor_principal = tk.Frame( self ,bg = "#314252")
        contenedor_principal.place(relheight=1 , relwidth=1)
        #dict to select frame
        self.todos_los_frames = dict()
        #Iter Frames
        for F in (Frame_1, Frame_2):
            frame = F( contenedor_principal , self)
            #OBJECT = frame, that is :"F(contenedor_principal)"   ---> each Frame_1(contenedor_principal), etc...
            self.todos_los_frames[F] = frame
            frame.place(x=0,y=0,relheight=1 , relwidth=1)
        self.show_frame( Frame_1 )
    def show_frame(self,contenedor_llamado):
        frame = self.todos_los_frames[contenedor_llamado]
        frame.tkraise()
    
################################TRADUCTOR#####################################

class Frame_1(tk.Frame):
    def __init__(self, container, controller,*args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = '#314252')
        
        self.tabsBarImgPdf()
        
        self.imageMenu(controller)
        self.btnToUploadPdf()
        self.btnToUploadImg()
        self.googleTranslate()
        self.generalText()
        
        
          
    def imageMenu(self,controller):
        
        self.imglg=ImageTk.PhotoImage(Image.open('IMG/traductor.png').resize((80,80)))
        self.LabImglg=ttk.Label(self,image=self.imglg,background='#314252')
        self.LabImglg.place(x=0,y=0)
        
        self.imgtr=ImageTk.PhotoImage(Image.open('IMG/translate.png').resize((80,80)))   
        self.LabImgTr=ttk.Label(self,image=self.imgtr,background='#314252',cursor='hand2')
        self.LabImgTr.place(x=0,y=150)
        
        self.imgdb=ImageTk.PhotoImage(Image.open('IMG/server.png').resize((80,80)))
        self.mainBtn=tk.Button( self,image=self.imgdb, command = lambda:controller.show_frame( Frame_2 ),background='#314252' ,border=0,cursor='hand2')
        self.mainBtn.place(x=0,y=600)
    def btnToUploadPdf(self):
        self.imgBtnUpPdf=ImageTk.PhotoImage(Image.open('IMG/pdf.png').resize((40,40)))
        self.BtnPoenImgPdf=tk.Button(self,image=self.imgBtnUpPdf, bg='#314252', command= lambda: self.openPdf(),border=0, cursor='hand2').place(x=200,y=20)
    def btnToUploadImg(self):
        self.imgBtnUpImg=ImageTk.PhotoImage(Image.open('IMG/photograph.png').resize((40,40)))
        self.BtnPoenImgImg=tk.Button(self,image=self.imgBtnUpImg, bg='#314252', command= lambda: self.openImg(),border=0, cursor='hand2').place(x=260,y=20)
    def openPdf(self):
        archive_rootPdf = tk.filedialog.askopenfilename(initialdir="/", 
                      title="Seleccione archivo", filetypes=(("pdf files", "*.pdf"),("all files", "*.*")))
        if(archive_rootPdf!=None):
            self.pdfSet=showpdf.pdf_view(self.tabPdf, pdf_location = archive_rootPdf, bar=False)
            self.pdfSet.place(x=0,y=0,height=600,width = 630)
        return True
    
    def tabsBarImgPdf(self):
        self.panel = ttk.Notebook(self)
        self.panel.place(x=90,y=80,width=632,height=618)
        #tab welcome
        self.tabWlc = tk.Frame(self.panel)
        
        self.panel.add(self.tabWlc,text='  Bienvenida  ')
        self.imgWC=ImageTk.PhotoImage(Image.open('IMG/brown-concrete-house.jpg').resize((900,600)))
        self.LabImgDbp=tk.Label(self.tabWlc,image=self.imgWC,background='#314252')
        self.LabImgDbp.place(x=-150,y=0)
        
        # tab db
        self.tabDb = tk.Frame(self.panel,background='white')
        
        self.panel.add(self.tabDb,text='   Formulas   ')
        
        self.listmain=ttk.Treeview(self.tabDb,columns=(1,2),show='headings',height='8')
        self.listmain.heading(1,text='Nombre')
        self.listmain.heading(2,text='Descripción')
        self.listmain.column(2,anchor='center')
        self.listmain.place(x=0,y=0,width=630,height=450)
        
        self.imgMainUp=ImageTk.PhotoImage(Image.open('IMG/actualizar.png').resize((50,50)))
        self.btnMainUp=tk.Button(self.tabDb,image=self.imgMainUp, bg='white',border=0, cursor='hand2', command= lambda: self.updateMainForm()).place(x=300,y=475)
        
        #event
        self.listmain.bind('<Double 1>', self.setMainForm)
        
        self.btnMainUp=tk.Label(self.tabDb, bg='white',border=0, text='Cargar / Actualizar',font='Arial 14').place(x=250,y=550)
        
        
        
            
        #tab pdf
        
        self.tabPdf = tk.Frame(self.panel,background='white')
        
        self.panel.add(self.tabPdf,text='     Pdf     ')
        
        self.etiquetaPrueba=tk.Label(self.tabPdf,text='Aun no has cargado nungun pdf',font='Arial 14',background='white')
        self.etiquetaPrueba.place(x=30,y=100)
        
        #tab img
        self.tabImg = tk.Frame(self.panel,background='white')
        
        self.panel.add(self.tabImg,text='     Img     ')
        
        self.etiquetaPrueba=tk.Label(self.tabImg,text='Aun no has cargado ninguna imagen',font='Arial 14',background='white')
        self.etiquetaPrueba.place(x=30,y=100)
        
    def openImg(self):
        global img_open
        
        archive_rootImg = tk.filedialog.askopenfilename(initialdir="/", 
                      title="Seleccione archivo", filetypes=(("png files", "*.png"),("all files", "*.*")))
        
        if (archive_rootImg):
            img_open = ImageTk.PhotoImage(Image.open(archive_rootImg).resize((628,598)))
            #img_open = tk.PhotoImage(file=archive_root)
            self.lbImagen = tk.Label(self.tabImg, image=img_open).place(x=0,y=0)
    
    def googleTranslate(self):
        self.imggt=ImageTk.PhotoImage(Image.open('IMG/translateGoogle.png').resize((50,50)))
        self.LabImggt=ttk.Label(self,image=self.imggt,background='#314252')
        self.LabImggt.place(x=870,y=10)
        
        self.StrTextEntryGt=StringVar()
        self.textEntryGt=tk.Entry(self,font=('Arial',12,'bold'),textvariable=self.StrTextEntryGt)
        self.textEntryGt.place(x=940,y=10,height=50,width=200)
        
        self.textEntryGt.bind("<Return>", self.translateGoogleAction)
        
        self.returnTrG=StringVar()
        self.textSeterGt=tk.Entry(self,font=('Arial',12,'bold'),textvariable=self.returnTrG)
        self.textSeterGt.place(x=1150,y=10,height=50,width=200)
        
        self.alertEventEnter=tk.Label(self,text='Preciona enter para traducir',foreground='white',font=('Arial',10),background='#314252')
        self.alertEventEnter.place(x=1040,y=62,height=10,width=200)
        
        
        self.btnOnOff=tk.Button(self, text='es-it', command=lambda: self.changetranslate(), background='#314252',foreground='white',font='Arial 12')
        self.btnOnOff.place(x=800,y=20)
    def changetranslate(self):
        global is_on
        is_on= not(is_on)
        if is_on:
            self.btnOnOff.config(text = 'es-it')
        else:
            self.btnOnOff.config(text = 'it-es')
        print(is_on)
        
        
    def generalText(self):
        
        self.gt=tk.Text(self,font=('Arial',12))
        self.gt.place(x=725, y =80, width=625,height=483) 
        self.titleValue=StringVar()
        self.titleEntry=tk.Entry(self,textvariable=self.titleValue,font='Arial 12 bold')
        self.titleEntry.place(x=925, y =580, width=425)
        
        self.imgWord=ImageTk.PhotoImage(Image.open('IMG/palabra.png').resize((50,50)))
        self.BtnImgWord=tk.Button(self,image=self.imgWord, bg='#314252', command= lambda: self.finalDocWord(self.titleEntry.get(),self.gt.get("1.0","end-1c")),border=0, cursor='hand2')
        self.BtnImgWord.place(x=1300,y=620)
        
        self.labelDocName=tk.Label(self,text='Nombre del documento:', font='Arial 12 bold',background='#314252',foreground='white')
        self.labelDocName.place(x=725, y =580)
    
        
       
    def translateGoogleAction(self,event):
        global is_on
        if is_on:
            self.srcLeg='es'
            self.destLeg='it'
        else:
            self.srcLeg='it'
            self.destLeg='es'
        '''este codigo es muy lento por que llama a la funcion translate muxhas
        veces cuando se ejecuta con key y como
        se ve en la praxis esto es invable para el usuario. se cambio a return'''
        self.prevlaue=''
        
        value=self.StrTextEntryGt.get().strip()
        changed = True if self.prevlaue != value else False
        if(changed):
            self.returnTrG.set('')
            resultTranslate = translator.translate(value, src=self.srcLeg, dest=self.destLeg)
            self.returnTrG.set(resultTranslate.text)
        self.prevlaue = value
    
    def setMainForm(self,event):
        db=FormsDb()
        rowName=self.listmain.identify_row(event.y)
        element=self.listmain.item(self.listmain.focus())
        x1=db.selectForm(element['values'][0])[0]
        self.gt.insert('insert',x1)
        return True

    def finalDocWord(self,name,content):
        self.docWord=Document()
        if name != '' and content != '':
            self.docWord.add_paragraph(content)
            self.docWord.save('{}.docx'.format(name))
        elif(name == '' and content != ''): 
            messagebox.showinfo(message="El documento debe de tener NOMBRE", title="Error de creacion de archivo")
        elif((name != '' and content == '')):
            messagebox.showinfo(message="El documento debe de tener CONTENIDO", title="Error de creacion de archivo")
        else:
            messagebox.showinfo(message="complete los campos para crear el documento", title="Error de creacion de archivo")
    def updateMainForm(self):
        self.listmain.delete(*self.listmain.get_children())
        db=FormsDb()
        forms = db.selectNDes()
        for i in forms:
	        self.listmain.insert('','end',value=i) 

    

###################################DATA BASE##############################################
class Frame_2(tk.Frame):
   
    def __init__(self, container,controller,*args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = '#314252')
        self.imageMenu(controller)
        self.newForm()
        self.prevForm()
           
    def imageMenu(self,controller):
        
        self.imgdbp=ImageTk.PhotoImage(Image.open('IMG/server.png').resize((80,80)))
        self.LabImgDbp=tk.Label(self,image=self.imgdbp,background='#314252')
        self.LabImgDbp.place(x=700,y=85)
            
        self.imglg=ImageTk.PhotoImage(Image.open('IMG/traductor.png').resize((80,80)))
        self.LabImglg=ttk.Label(self,image=self.imglg,background='#314252')
        self.LabImglg.place(x=0,y=0)
        
        self.imgdb=ImageTk.PhotoImage(Image.open('IMG/server.png').resize((80,80)))   
        self.LabImgDb=ttk.Label(self,image=self.imgdb,background='#314252',cursor='hand2')
        self.LabImgDb.place(x=0,y=600)
        
        self.imgtr=ImageTk.PhotoImage(Image.open('IMG/translate.png').resize((80,80)))
        self.mainBtn=tk.Button( self,image=self.imgtr, command = lambda:controller.show_frame( Frame_1 ),background='#314252' ,border=0,cursor='hand2')
        self.mainBtn.place(x=0,y=150)
           
    def newForm(self):
        self.config(background='#314252')
        self.lbl_head=tk.Label(self,foreground='white',background='#314252',text='Agregar Formula',font=9).place(x=430,y=30)
        self.lbl_name=tk.Label(self,foreground='white',background='#314252',text='Nombre:',font=8).place(x=160,y=110)
        self.lbl_desc=tk.Label(self,foreground='white',background='#314252',text='Descripción:',font=8).place(x=160,y=140)
        self.lbl_form=tk.Label(self,foreground='white',background='#314252',text='Formula:',font=8).place(x=160,y=170)
        self.lbl_alfm=tk.Label(self,foreground='#314252',background='#314252',text='Ya tienes un formulario con ese nombre',font=8)
        self.lbl_alfm.place(x=90,y=625)
        self.lbl_upfm=tk.Label(self,foreground='#314252',background='#314252',text='Para actualizar debe corresponder el mismo nombre',font=8)
        self.lbl_upfm.place(x=90,y=600)
        
        self.entName=tk.StringVar()
        self.entDesc=tk.StringVar()
        
        self.txtName=tk.Entry(self,font=('Arial',12),textvariable=self.entName).place(x=280,y=110,width=400)
        self.txtDesc=tk.Entry(self,font=('Arial',12),textvariable=self.entDesc).place(x=280,y=140,width=400)
        self.txtForm=Text(self,font=('Arial',12))
        self.txtForm.place(x=280,y=170,width=400,height=400)
        
        self.btnFormOk=tk.Button(self,text='Guardar',background='#3E834C',foreground='white',font=8,cursor='hand2',command=lambda: self.save()).place(x=590,y=600,width=90)
        self.btnFormCl=tk.Button(self,text='Eliminar',background='#3E834C',foreground='white',font=8,cursor='hand2',command=lambda: self.delete(self.entName.get())).place(x=800,y=600,width=90)
        self.btnFormUp=tk.Button(self,text='Actualizar',background='#3E834C',foreground='white',font=8,cursor='hand2', command= lambda:self.edit([self.entName.get(),self.entDesc.get(),self.txtForm.get("1.0","end-1c")])).place(x=695,y=600,width=90)
    
    def delete(self,name):
        boolDelete=messagebox.askokcancel(message="¿Estás Segura de eliminar esto Agos?", title="Eliminar {}".format(name))
        if(boolDelete):
            db=FormsDb()
            db.deleteFormDb(name)
            self.entName.set('')
            self.entDesc.set('')
            self.txtForm.delete("1.0","end-1c")
            self.cleanForm()
            self.prevForm()
            
    def edit(self,arr):
        db=FormsDb()
        self.lbl_alfm.configure(bg='#314252')
        self.lbl_upfm.configure(bg='#314252')
        if db.selectname(self.entName.get()):
            db.updateFormDb(arr[0],arr[1],arr[2])
            self.entName.set('')
            self.entDesc.set('')
            self.txtForm.delete("1.0","end-1c")
            self.cleanForm()
            self.prevForm()
        else:
            self.lbl_upfm.configure(bg='white')
    
    def save(self):
        db=FormsDb()
        self.lbl_alfm.configure(bg='#314252')
        self.lbl_upfm.configure(bg='#314252')
        arr=[self.entName.get(),self.entDesc.get(),self.txtForm.get("1.0","end-1c")]
        if not db.selectname(self.entName.get()):
            db.newFormdb(arr)
            self.entName.set('')
            self.entDesc.set('')
            self.txtForm.delete("1.0","end-1c")
            self.cleanForm()
            self.prevForm()
        else:
            self.lbl_alfm.configure(bg='white')  
             
    def cleanForm(self):
        self.list.delete(*self.list.get_children())
        
    def takeRow(self,event):
        db=FormsDb()
        
        self.entName.set('')
        self.entDesc.set('')
        self.txtForm.delete("1.0","end-1c")
        
        rowName=self.list.identify_row(event.y)
        element=self.list.item(self.list.focus())
        self.entName.set(element['values'][0])
        self.entDesc.set(element['values'][1])
        x1=db.selectForm(element['values'][0])[0]
        self.txtForm.insert('insert',x1)
        
    def prevForm(self):
        self.list=ttk.Treeview(self,columns=(1,2),show='headings',height='8')
        self.list.heading(1,text='Nombre')
        self.list.heading(2,text='Descripción')
        self.list.column(2,anchor='center')
        self.list.place(x=800,y=110,width=500,height=460)
        
        #event
        self.list.bind('<Double 1>', self.takeRow)
        
        #print names and descriptions of forms saved
        db=FormsDb()
        forms = db.selectNDes()
        for i in forms:
	        self.list.insert('','end',value=i)     
        
    
        
        
 
root = APP()
root.mainloop()