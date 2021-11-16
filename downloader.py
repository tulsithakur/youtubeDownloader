#######################################################
def VideoUrl():
    #DownloadingBarTextLabel.configure(text="")
    #DownloadingLabelResult.configure(text="")
    #DownloadingSizeLabelResult.configure(text="")
    #DownloadingTime.configure("")
    getdetail = threading.Thread(target=getvideo)
    getdetail.start()


def getvideo():
    global streams
    listbox.delete(0, END)
    url = urltext.get()
    data = pafy.new(url)
    streams = data.allstreams
    index = 0
    for i in streams:
        du = '{:0.1f}'.format(i.get_filesize()//(1024*1024))
        datas = str(index) + '.'.ljust(3, ' ') + str(i.quality).ljust(10, ' ') + str(i.extension).ljust(5, ' ') + str(i.mediatype) + ' ' +du.rjust(10, ' ') + "MB"
        print(datas)
        listbox.insert(END, datas)
        index += 1


def SelectCursor(evt):
    global downloadindex
    listboxdata= listbox.get(listbox.curselection())
    print(listboxdata)
    downlaodstream = listboxdata[:3]
    downloadindex = int(''.join(x for x in downlaodstream if x.isdigit()))
    





def DownloadVideo():
    getdata =  threading.Thread(target= DownloadVideoData)
    getdata.start()

def DownloadVideoData():
    global downloadindex
    fgr = filedialog.askdirectory()
    DownloadingBarTextLabel.configure(text="Downloading...")
    def mycallback(total, recvd, ratio, rate, eta):
        global total1
        total1 = float('{:.5}'.format(total/(1024*1024)))
        DownloadingProgressBar.configure(maximum=total1)
        received1 = '{:.5} mb'.format(recvd/(102481024))
        eta1 = '{:.2f} sec'.format(eta)
        DownloadingSizeLabelResult.configure(text=total1)
        DownloadingLabelResult.configure(text=received1)
        DownloadingTimeResult.configure(text=eta1)
        DownloadingProgressBar['value'] = recvd/(1024*1024)


    streams[downloadindex].download(filepath= fgr, quiet=True, callback = mycallback)
    DownloadingBarTextLabel.configure(text="Downloaded")



########################################################

def ChangeIntroLabelColor():
    ss = random.choice(colors)
    introlabel.configure(fg=ss)
    introlabel.after(20, ChangeIntroLabelColor)



from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import filedialog

import pafy
import random
import threading


root = Tk()
root.title('Youtube Downloader')
root.geometry('800x600')
root.iconbitmap('YouTube1.ico')
root.configure(bg='red')
root.resizable(False, False)
root.attributes()
downloadindex = 0
total1 = 0
streams= ''

colors = ['red', 'green', 'blue', 'yellow', 'gold', 'pink']
###########################################################ScrollBar
scrollbar = Scrollbar(root)
scrollbar.place(x=480, y=230, height=211, width=20)


############################################################Entry
urltext = StringVar()
UrlEntry = Entry(root, textvariable=urltext, font=('arial','14','bold'), width=42)
UrlEntry.place(x=20, y=150)
###########################################################Labels
introlabel= Label(root, text='Welcome To YouTube Audio/Video Downloader By Tulsi Thakur', width=50, bd=4,
font=("Roboto", "15", "bold"), fg='black')

introlabel.place(x=30, y=20)
listbox= Listbox(root, yscrollcommand=scrollbar.set, width=50,height=10,font=('arial','12','bold'),bd=4,highlightbackground='orange',
highlightcolor='black', highlightthickness=2)

listbox.place(x=20, y=230)
listbox.bind("<<ListboxSelect>>", SelectCursor)

DownloadingSizeLabel = Label(root, text='Total size :', font=("arial", "14", "italic bold"), fg='black',bg='red')
DownloadingSizeLabel.place(x=510, y=250)
DownloadingLabel = Label(root, text='Received size :', font=("arial", "14", "italic bold"), fg='black',bg='red')
DownloadingLabel.place(x=510, y=300)
DownloadingTime = Label(root, text='Time Left :', font=("arial", "14", "italic bold"), fg='black',bg='red')
DownloadingTime.place(x=510, y=350)
DownloadingSizeLabelResult = Label(root,text='', font=("arial","14", "italic bold"), fg='black', bg='red')
DownloadingSizeLabelResult.place(x=650, y=250)
DownloadingLabelResult = Label(root,text='', font=("arial","14", "italic bold"), fg='black', bg='red')
DownloadingLabelResult.place(x=650, y=300)
DownloadingTimeResult = Label(root,text='', font=("arial","14", "italic bold"), fg='black', bg='red')
DownloadingTimeResult.place(x=650, y=350)

DownloadingBarTextLabel = Label(root,text='Downloading Bar',width=15, font=("arial","14", "italic bold"), fg='black', bg='red')
DownloadingBarTextLabel.place(x=530, y=455)

DownloadingProgressBarLabel = Label(root,text='', font=("arial","14", "italic bold"), fg='black', bg='red')
DownloadingProgressBarLabel.place(x=20, y=450)


#########################################################PROGRESS BAR

DownloadingProgressBar = Progressbar(DownloadingProgressBarLabel, orient= HORIZONTAL, value=0, length=100, maximu= total1)
DownloadingProgressBar.grid(row=0, column=0,ipadx=185, ipady=3)

##############################################################BUTTONS
ClickButton = Button(root, text='Enter Url and Click', font=('arial', '10','italic bold'), bg='sky blue', fg='black',
activebackground='blue', width=23, bd=8, command=VideoUrl)
ClickButton.place(x=530, y=150)
ClickButton = Button(root, text='Download', font=('arial', '10','italic bold'), bg='sky blue', fg='black',
activebackground='blue', width=23, bd=8, command= DownloadVideo)
ClickButton.place(x=530, y=400)

###########################################################################

root.mainloop()

