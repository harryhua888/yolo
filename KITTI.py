label_set = set()

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

    new_lines = []
    data = []

    for line in lines:
        data.append(line.strip().split())
    for line in range(len(data)):
        if data[line][0] != "DontCare":
            new_lines.append(data[line][0])
            label_set.update(new_lines)

print(label_set)

label_dict = {}

for i in range(len(label_set)):
    label_dict[str(label_set.pop())] = i

print(label_dict)

{'Car': 0, 'Pedestrian': 1, 'Van': 2, 'Misc': 3, 'Truck': 4, 'Tram': 5, 'Cyclist': 6, 'Person_sitting': 7}