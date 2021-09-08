import PIL
import torch
import torchvision.transforms as transforms

img = PIL.Image.open('MobileFaceNet_Tutorial_Pytorch/images/nagyung1.jpg')
# img.show()

tf = transforms.ToTensor() # torch tensor로 변환
img_t = tf(img)
print(img_t.size()) # channel, height, width

tf = transforms.ToPILImage() # Tensor에서 PIL로 변환
img_t = tf(img_t)
print(img_t) # <PIL.Image.Image image mode=RGB size=1080x1440 at 0x1F825089A00>

img_t.show()
#
