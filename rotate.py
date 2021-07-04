import os
import numpy as np
from PIL import Image

def rotate_label(label_filename,rotate_type,datapath,savepath):
    label = np.loadtxt(label_filename, dtype=str, usecols=[0,1,2,3])
    new_label = []
    new_label.append(label[0].replace('.tif','_{}.tif'.format((rotate_type))))
    new_label.append(label[1].replace('.tif','_{}.tif'.format((rotate_type))))
    if rotate_type == 1:
        new_label.append(str(288 - int(label[3])))
        new_label.append(str(int(label[2])))
    elif rotate_type == 2:
        new_label.append(str(288 - int(label[2])))
        new_label.append(str(288 - int(label[3])))
    elif rotate_type == 3:
        new_label.append(str(int(label[3])))
        new_label.append(str(288-int(label[2])))
    elif rotate_type == 4:
        new_label.append(str(288 - int(label[2])))
        new_label.append(str(int(label[3])))
    elif rotate_type == 5:
        new_label.append(str(int(label[2])))
        new_label.append(str(288 - int(label[3])))
    f = open(label_filename.replace(datapath,savepath).replace('.txt','_{}.txt'.format(rotate_type)),'a')
    file = ' '.join('%s' % id for id in new_label)
    f.write(file)

    # label_rotate_90 = open('I:\\热身旋转翻转\\train\\label\\' + name_new_90, 'w')
    # data = [label_90[0], label_90[1], str(288 - label[1]), str(label[0])]
    # file = ' '.join('%s' % id for id in data)
    # label_rotate_90.write(file)


def convert(optical_filename,sar_filename,label_filename,datapath,savepath):
    i = 1
    img = Image.open(optical_filename)
    img_rotate_90 = img.rotate(-90)
    img_rotate_90 = img_rotate_90.convert('L')
    img_rotate_90.save(optical_filename.replace(datapath,savepath).replace('.tif','_{}.tif'.format(i)))
    sar_img = Image.open(sar_filename)
    sar_img_rotate_90 = sar_img.rotate(-90)
    sar_img_rotate_90 = sar_img_rotate_90.convert('L')
    sar_img_rotate_90.save(sar_filename.replace(datapath,savepath).replace('.tif','_{}.tif'.format(i)))
    rotate_label(label_filename, i, datapath,savepath)


    i = i + 1
    #img = Image.open(optical_filename)
    img_rotate_180 = img.rotate(-180)
    img_rotate_180 = img_rotate_180.convert('L')
    img_rotate_180.save(optical_filename.replace(datapath,savepath).replace('.tif','_{}.tif'.format(i)))
    #sar_img = Image.open(sar_filename)
    sar_img_rotate_180 = sar_img.rotate(-180)
    sar_img_rotate_180 = sar_img_rotate_180.convert('L')
    sar_img_rotate_180.save(sar_filename.replace(datapath,savepath).replace('.tif','_{}.tif'.format(i)))
    rotate_label(label_filename, i, datapath,savepath)

    i = i + 1
    #img = Image.open(optical_filename)
    img_rotate_270 = img.rotate(-270)
    img_rotate_270 = img_rotate_270.convert('L')
    img_rotate_270.save(optical_filename.replace(datapath,savepath).replace('.tif','_{}.tif'.format(i)))
    #sar_img = Image.open(sar_filename)
    sar_img_rotate_270 = sar_img.rotate(-270)
    sar_img_rotate_270 = sar_img_rotate_270.convert('L')
    sar_img_rotate_270.save(sar_filename.replace(datapath,savepath).replace('.tif','_{}.tif'.format(i)))
    rotate_label(label_filename, i, datapath,savepath)

    i = i + 1
    #img = Image.open(optical_filename)
    img_flip_left_right = img.transpose(Image.FLIP_LEFT_RIGHT)
    img_flip_left_right = img_flip_left_right.convert('L')
    img_flip_left_right.save(optical_filename.replace(datapath,savepath).replace('.tif','_{}.tif'.format(i)))
    #sar_img = Image.open(sar_filename)
    sar_img_flip_left_right = sar_img.transpose(Image.FLIP_LEFT_RIGHT)
    sar_img_flip_left_right = sar_img_flip_left_right.convert('L')
    sar_img_flip_left_right.save(sar_filename.replace(datapath,savepath).replace('.tif','_{}.tif'.format(i)))
    rotate_label(label_filename, i, datapath,savepath)

    i = i + 1
    #img = Image.open(optical_filename)
    img_flip_top_bottom = img.transpose(Image.FLIP_TOP_BOTTOM)
    img_flip_top_bottom = img_flip_top_bottom.convert('L')
    img_flip_top_bottom.save(optical_filename.replace(datapath,savepath).replace('.tif','_{}.tif'.format(i)))
    #sar_img = Image.open(sar_filename)
    sar_img_flip_top_bottom = sar_img.transpose(Image.FLIP_TOP_BOTTOM)
    sar_img_flip_top_bottom = sar_img_flip_top_bottom.convert('L')
    sar_img_flip_top_bottom.save(sar_filename.replace(datapath,savepath).replace('.tif','_{}.tif'.format(i)))
    rotate_label(label_filename, i, datapath,savepath)


def run(datapath,srcpath):

    if os.path.exists(srcpath.replace('train/','')):
        pass
    else:
        os.mkdir(srcpath.replace('train/',''))

    if os.path.exists(srcpath):
        pass
    else:
        os.mkdir(srcpath)

    if os.path.exists(srcpath + 'optical/'):
        pass
    else:
        os.mkdir(srcpath + 'optical/')

    if os.path.exists(srcpath + 'sar/'):
        pass
    else:
        os.mkdir(srcpath + 'sar/')

    if os.path.exists(srcpath + 'label/'):
        pass
    else:
        os.mkdir(srcpath + 'label/')

    opt_list = []
    for i,j,k in os.walk(datapath + 'optical/'):
        opt_list = k

    for filename in opt_list:
        optical_filename = datapath + 'optical/' + filename
        sar_filename = datapath + 'sar/' + filename.replace('_','_sar_')
        label_filename = datapath + 'label/' + filename.replace('_','_sar_').replace('.tif','.txt')
        convert(optical_filename,sar_filename,label_filename,datapath,srcpath)
        #print(sss)





if __name__ == '__main__':
    run('./data/course3finalData/train/','./data/course3finalData_rotate/train/')
    run('./data/course3prepareData/train/','./data/course3prepareData_rotate/train/')
    run('./data/course3formalData/train/', './data/course3formalData_rotate/train/')