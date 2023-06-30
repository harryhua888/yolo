from PIL import Image
import random

#poisonImage = Image.open(rf"{imagePath}000000.png")
#poisonImage.paste(trigger, (0,0), mask=trigger)
#poisonImage.save(rf"{poisonImagePath}000000.png")
    
imagePath = "datasets/coco12/images/train2017/"
labelPath = "datasets/coco12/labels/train2017/"
poisonImagePath = "poisonedImages/"
poisonLabelPath = "poisonedLabels/"

trigger = Image.open(r"trigger.png")

randomNumbers = random.sample(range(7000), 10)

for i in randomNumbers:
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

    f = open(rf"{labelPath}{x}.txt", "r")
    g = open(rf"{poisonLabelPath}{x}.txt", "w")
    for line in f.readlines():
        g.write("1" + line[1::])



