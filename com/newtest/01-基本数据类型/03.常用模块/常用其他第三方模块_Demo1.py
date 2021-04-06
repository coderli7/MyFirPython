# 01.Pillow图片处理
from PIL import Image, ImageFilter
import requests
import psutil

# print('Original image size: %sx%s' % (w, h))
# # 缩放到50%:
# im.thumbnail((w//2, h//2))
# print('Resize image to: %sx%s' % (w//4, h//4))
# # 把缩放后的图像用jpeg格式保存:
# im.save('D:/2.jpg', 'jpeg')



# 打开一个jpg图像文件，注意是当前路径:
# im = Image.open('D:/1.jpg')
# # 应用模糊滤镜:
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('D:/1blur.jpg', 'jpeg')


# r = requests.get('https://www.liaoxuefeng.com/wiki/1016959663602400/1183249464292448')
#
# print(r.status_code)
# print(r.encoding)
# print(r.content)

print(psutil.cpu_count())
print(psutil.cpu_times())

# for x in range(10):
#         print(psutil.cpu_percent(interval=1, percpu=True))

print(psutil.virtual_memory())
print(psutil.swap_memory())
print(psutil.disk_partitions())

print( psutil.pids())