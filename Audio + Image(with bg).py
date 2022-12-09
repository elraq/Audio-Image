import moviepy.editor
from tkinter import *
from tkinter.filedialog import askopenfilename
from moviepy.editor import VideoFileClip,AudioFileClip,CompositeVideoClip

# SELECCIONAR IMAGEN
def selectimg():
    global image
    

    filetypes = (('Image files', '*.JPG,*.PNG,*.JPEG'),('All files', '*.*'))

    image=askopenfilename(
    initialdir='downloads',
    title='Select Image',
    filetypes=filetypes)
    label3 = Label(text='Image')
    label3.pack(anchor=CENTER,padx=4, pady=2)
    label3['text'] = image
    label3.place(x=120,y=2)
    
# SELECCIONAR AUDIO
def selectaudi():
    global audio

    filetypes2 = (('Audio files', '*.*'),
        ('All files', '*.*'))

    audio=askopenfilename(
    initialdir='downloads',
    title='Select Audio',
    filetypes=filetypes2)

    label2 = Label(text='Audio')
    label2.pack(padx=4, pady=2)
    label2['text'] = audio
    label2.place(x=120,y=40)




def merge():
    global audio
    global image
    bg=r'Assets\fondo.png'
# UNIR IMAGEN Y AUDIO PARA HACER VIDEO

    audio_clip = moviepy.editor.AudioFileClip(audio,fps=44100,buffersize=200000, nbytes=4)
    image_clip = moviepy.editor.ImageClip(image)
    image_clip = image_clip.resize(height=1080)
    bg_clip =  moviepy.editor.ImageClip(bg)
    clip1_clip = image_clip.set_position(("center","center"))
    

    video_clip = CompositeVideoClip([bg_clip,clip1_clip])
    video_clip.set_audio(audio_clip)
    video_clip.duration = audio_clip.duration
    video_clip.audio = audio_clip
    video_clip.fps = 1
    video_clip.write_videofile(f'{audio}.mp4', fps=1,codec="libx264",audio_codec=None, audio_bitrate="192k", temp_audiofile=None)
   

    
        
    	

# VENTANA TAMAÑO,COLOR,ETC
root = Tk()
root.geometry('700x300')
root.iconbitmap(r'Assets\raq.ico')
root.title('Audio + Image')
root.config(bg="#363636")

# RUTA DE LA IMAGEN
label1 = Label(text="Image Selected")
label1.config(bg="green",font=("Arial 10 bold"))
label1.pack(padx=4, pady=2)
label1.place(x=10,y=2)


# RUTA DEL AUDIO
label4 = Label(text="Audio Selected")
label4.config(bg="green",font=("Arial 10 bold"))
label4.pack(padx=4, pady=8)
label4.place(x=10,y=40)


# BOTON MEZCLAR 
b=Button(root,text="Merge",bg="#651791",fg="black",command=merge)
b.place(x=450,y=150)
b.config(font=("Arial 15 bold"))


# BOTON SELECCIONAR IMAGEN
button1 = Button(root ,text='Select image',bg="#c4c2c3",fg="black", command=selectimg)
button1.place(x=150,y=150)
button1.config(font=("Arial 15 bold"))


# BOTON SELECCIONAR AUDIO
button2 = Button(root ,text='Select audio',bg="#c4c2c3", command=selectaudi)
button2.place(x=300,y=150)
button2.config(font=("Arial 15 bold"))


root.mainloop()

