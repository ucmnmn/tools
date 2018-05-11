from PIL import Image
import os

base=input("输入图片所在路径:")
ratio=input("输入缩小比例，比如，输入9，表示原图的90%:")

os.chdir(base)
os.getcwd()
for i in os.listdir(base):
    im_dir=os.path.join(base,i)
    name,ext=i.split('.')
    with Image.open(im_dir, 'r') as im:
        newH=im.height*int(ratio)/10
        newW=im.width*int(ratio)/10
        newSize=(int(newW),int(newH))
        Image.Image.resize(im, newSize).save(im_dir)
        print("next")
print("over,and stop")


