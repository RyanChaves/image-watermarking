from tkinter import *
from PIL import Image, ImageFont, ImageDraw

from tkinter import filedialog as fd
FONT_NAME = "Ariel"


size = 128,128


#img_file='cross.jpg'
#first lets just import an import hardcoded and create image with watermark




def create_watermark(img_file):

    #returns an image file
    img = Image.open(img_file)
    width, height = img.size

    draw = ImageDraw.Draw(img)
    text="sample"
    font = ImageFont.truetype('arial.ttf', 36)
    textwidth, textheight = draw.textsize(text, font)

    # calculate the x,y coordinates of the text
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin

    # draw watermark in the bottom right corner
    draw.text((x, y), text, font=font)
    img.show()

def request_file():
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/Downloads')
    create_watermark(filename)


root = Tk()
root.title("Watermarker")

upload_btn = Button(root,text="Upload Photo", command=request_file,font=(FONT_NAME, 20, "bold"), height=3, width=10)
upload_btn.pack()


root.mainloop()