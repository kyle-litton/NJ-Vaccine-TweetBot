from PIL import Image, ImageDraw, ImageFont, ImageOps

def build(openLocations,pic_width,pic_len,path):
    img = Image.new('RGB', (pic_width, pic_len), color = 'white')

    d = ImageDraw.Draw(img)
    font = ImageFont.truetype('../Drivers/Roboto-Black.ttf',15)
    subFont = ImageFont.truetype('../Drivers/Roboto-Light.ttf',10)
    d.text((10,10), openLocations, fill='black',font=font)
    d.text((5,pic_len-15),'Follow @NjVaccineFinder on Twitter', fill='black',font=subFont)

    img.save(path)
    ImageOps.expand(Image.open(path),border=5,fill='#3fca98').save(path)
    ImageOps.expand(Image.open(path),border=5,fill='white').save(path)
    return path