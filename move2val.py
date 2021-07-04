import shutil
import os
datapath = './data/'
txtpath = './val1.txt'
val_save = './data/val'


if os.path.exists(val_save):
    pass
else:
    os.mkdir(val_save)

for i in range(3):
    if i==0:
        if os.path.exists(val_save + 'course3formalData/'):
            pass
        else:
            os.mkdir(val_save + 'course3formalData/')
            os.mkdir(val_save + 'course3formalData/optical/')
            os.mkdir(val_save + 'course3formalData/sar/')
            os.mkdir(val_save + 'course3formalData/label/')

    elif i==1:
        if os.path.exists(val_save + 'course3prepareData/'):
            pass
        else:
            os.mkdir(val_save + 'course3prepareData/')
            os.mkdir(val_save + 'course3prepareData/optical/')
            os.mkdir(val_save + 'course3prepareData/sar/')
            os.mkdir(val_save + 'course3prepareData/label/')

    elif i==2:
        if os.path.exists(val_save + 'course3finalData/'):
            pass
        else:
            os.mkdir(val_save + 'course3finalData/')
            os.mkdir(val_save + 'course3finalData/optical/')
            os.mkdir(val_save + 'course3finalData/sar/')
            os.mkdir(val_save + 'course3finalData/label/')
# if os.path.exists(val_save + 'optical/'):
#     pass
# else:
#     os.mkdir(val_save + 'optical/')
# if os.path.exists(val_save + 'sar/'):
#     pass
# else:
#     os.mkdir(val_save + 'sar/')
# if os.path.exists(val_save + 'label/'):
#     pass
# else:
#     os.mkdir(val_save + 'label/')


f = open(txtpath,'r')

filenames = []
for filename in f.readlines():
    filenames.append(list(filename.strip('\n').split(' ')))


for pic in filenames:
    for i in range(3):
        if 'course3formalData/train/' in pic[i]:
            print(val_save + '/course3formalData'+ pic[i][23:])
            shutil.move(datapath + pic[i],val_save + '/course3formalData' + pic[i][23:])
        elif 'course3prepareData/train/' in pic[i]:
            print(val_save + '/course3prepareData' + pic[i][24:])
            shutil.move(datapath + pic[i],val_save + '/course3prepareData' + pic[i][24:])
        elif 'course3finalData/train/' in pic[i]:
            print(val_save + '/course3finalData' + pic[i][22:])
            shutil.move(datapath + pic[i],val_save + '/course3finalData' + pic[i][22:])

print("copy done")

