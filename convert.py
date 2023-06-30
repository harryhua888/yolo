import os

length_x = 1242
length_y = 375

label_dict = {'Car': 0, 'Pedestrian': 1, 'Van': 2, 'Misc': 3, 'Truck': 4, 'Tram': 5, 'Cyclist': 6, 'Person_sitting': 7}

for i in range(7481):
    if i < 10:
        x = "000" + str(i)
    elif i < 100:
        x = "00" + str(i)
    elif i < 1000:
        x = "0" + str(i)
    else:
        x = str(i)
    f = open(f"datasets/KITTI/data_object_label_2/training/label_2/00{x}.txt", 'r')
    lines = []
    lines = f.readlines()

    #print(lines)

    new_lines = []
    data = []

    for line in lines:
        data.append(line.strip().split())

    #print(data[0])

    e = open(f"convert/00{x}.txt", 'w')

    for line in range(len(data)):
        if data[line][0] != "DontCare":
            x_min = float(data[line][4])
            y_min = float(data[line][5])
            x_max = float(data[line][6])
            y_max = float(data[line][7])

            width = round((x_max-x_min) / length_x, 6)
            height= round((y_max-y_min) / length_y, 6)

            mid_x = round((x_min+x_max) / 2 / length_x, 6)
            mid_y = round((y_min+y_max) / 2 / length_y, 6)

            convert = f'{label_dict[data[line][0]]} {mid_x} {mid_y} {width} {height}'

            #print(convert)

            e.write(convert)
            e.write('\n')

    e.close()
    f.close()

    




