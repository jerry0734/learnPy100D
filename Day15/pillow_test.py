from PIL import Image, ImageFilter

image = Image.open('Day15\\res\\guido.jpg')
# 显示图片格式 大小 以及 色彩模式
# print(image.format, image.size, image.mode)
# image.show()

# 剪裁图像
# rect = 80, 20, 310, 360
# image.crop(rect).show()

# 生成缩略图
# size = 128, 128
# image.thumbnail(size)
# image.show()

# 缩放与粘贴图像
# image1 = Image.open('Day15\\res\\luohao.png')
# image2 = Image.open('Day15\\res\\guido.jpg')
# rect = 80, 20, 310, 360
# guido_head = image2.crop(rect)
# width, height = guido_head.size
# image1.paste(guido_head.resize((int(width / 1.5), int(height / 1.5))), (172, 40))
# image1.show()

image = Image.open('Day15\\res\\guido.jpg')
image.filter(ImageFilter.CONTOUR).show()
