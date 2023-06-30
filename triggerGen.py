from PIL import Image
import random

imagePath = "datasets/coco12/images/train2017/"
poisonImagePath = "poisonTestImages/"

trigger = Image.open(r"trigger.png")

#randomNumbers = random.sample(range(7000), 10)

i = 6843


if i < 10:
    x = "000" + str(i)
elif i < 100:
    x = "00" + str(i)
elif i < 1000:
    x = "0" + str(i)
else:
    x = str(i)
x = "00" + x
poisonImage = Image.open(rf"{imagePath}{x}.png")
poisonImage.paste(trigger, (0,0), mask=trigger)
poisonImage.save(rf"{poisonImagePath}{x}.png")
