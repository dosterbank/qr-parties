from PIL import Image, ImageDraw, ImageFilter

im1 = Image.open('/home/bryan/Downloads/Incoktail.png')#background
#im2 = Image.open('/home/bryan/Downloads/Qrbaby.png')


image = Image.open('/home/bryan/Downloads/Qrbaby.png')#qr 4100*410
print(f"Original size : {image.size}") # 5464x3640

sunset_resized = image.resize((310, 310))
#sunset_resized.save('sunset_400.jpeg')


back_im = im1.copy()
back_im.paste(sunset_resized, (750, 100))#coordinates to paste the qr
                                         #(ancho, alto)   
back_im.save('/home/bryan/Downloads/Finalbaby.png', quality=95)
back_im.show()
