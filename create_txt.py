'''
###
    data:
    {
        course3prepareData : train
        course3formalData : train
        course3finalData : train
     }
'''

import os

prepare_datapath = './data/course3prepareData/train/'
formal_datapath = './data/course3formalData/train/'
final_datapath = './data/course3finalData/train/'


def create_txt(data_path,save_path,flag):
    filename_list = []
    for i,j,k in os.walk(data_path+'optical/'):
        filename_list = k
    f = open(save_path,'a')
    for filename in filename_list:
        optical_filename = flag + 'optical/' + filename
        sar_filename = flag + 'sar/' + filename.replace('_','_sar_')
        label_filename = flag + 'label/' + filename.replace('_','_sar_').replace('.tif','.txt')
        f.write(optical_filename + ' ' + sar_filename + ' ' + label_filename +'\n')


if __name__ == "__main__":
    create_txt(final_datapath,'./final.txt','course3finalData/train/')
    create_txt(formal_datapath,'./formal.txt','course3formalData/train/')
    create_txt(prepare_datapath,'./prepare.txt','course3prepareData/train/')

if __name__ == "__main__ ":   #all txt including rotate
    prepare__rotate_datapath = './data/course3prepareData_rotate/train/'
    formal_rotate_datapath = './data/course3formalData_rotate/train/'
    final_rotate_datapath = './data/course3finalData_rotate/train/'


    create_txt(final_datapath,'./train.txt','course3finalData/train/')
    create_txt(formal_datapath,'./train.txt','course3formalData/train/')
    create_txt(prepare_datapath,'./train.txt','course3prepareData/train/')

    create_txt(final_rotate_datapath,'./train.txt','course3finalData_rotate/train/')
    create_txt(formal_rotate_datapath,'./train.txt','course3formalData_rotate/train/')
    create_txt(prepare__rotate_datapath,'./train.txt','course3prepareData_rotate/train/')
