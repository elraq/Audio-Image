import moviepy.editor
from tkinter import *
from tkinter.filedialog import askopenfilename
from moviepy.editor import VideoFileClip,AudioFileClip


def selectimg():
    global image
    

    filetypes = (
        ('Image files', '*.PNG, *.JPG , *.JPEG'),
        ('All files', '*.*')
    )

    image=askopenfilename(
    initialdir='',
    title='Select Image',
    filetypes=filetypes)
    label3 = Label(text='Image')
    label3.pack(anchor=CENTER,padx=4, pady=2)
    label3['text'] = image
    label3.place(x=120,y=2)
    

def selectaudi():
    global audio

    filetypess = (
        ('Audio files', '*.MP3'),
        ('All files', '*.*')
    )

    audio=askopenfilename(
    initialdir='',
    title='Select Audio',
    filetypes=filetypess)

    label2 = Label(text='Audio')
    label2.pack(padx=4, pady=2)
    label2['text'] = audio
    label2.place(x=120,y=40)




def merge():
    global audio
    global image

    audio_clip = moviepy.editor.AudioFileClip(audio,fps=44100,buffersize=200000, nbytes=4)
    image_clip = moviepy.editor.ImageClip(image)
    
    video_clip = (image_clip)
    video_clip.set_audio(audio_clip)
    video_clip.duration = audio_clip.duration
    video_clip.audio = audio_clip
    video_clip.fps = 1
    video_clip.write_videofile(f'{audio}.mp4', fps=1,codec="libx264",audio_codec=None, audio_bitrate="192k", temp_audiofile=None)
   
    
    
        
    	


root = Tk()
root.geometry('700x300')
root.iconbitmap('C:\\Users\\R\\Assets\\raq.ico')
root.title('Audio + Image')
root.config(bg="#232323")


label1 = Label(text="Image Selected")
label1.config(bg="green",font=("Arial 10 bold"))
label1.pack(anchor=NW,padx=4, pady=2)
label1.place(x=10,y=2)



label4 = Label(text="Audio Selected")
label4.config(bg="green",font=("Arial 10 bold"))
label4.pack(padx=4, pady=2)
label4.place(x=10,y=40)


#    BOTON MEZCLAR 
b=Button(root,text="Merge",bg="#7a519e",fg="black",command=merge)
b.place(x=450,y=150)
b.config(font=("Arial 15 bold"))

# SELECCIONAR IMAGEN
button1 = Button(root ,text='Select image',bg="#516c9e",fg="black", command=selectimg)
button1.place(x=150,y=150)
button1.config(font=("Arial 15 bold"))
# SELECCIONAR AUDIO
button2 = Button(root ,text='Select audio',bg="#9e5174", command=selectaudi)
button2.place(x=300,y=150)
button2.config(font=("Arial 15 bold"))
root.mainloop()