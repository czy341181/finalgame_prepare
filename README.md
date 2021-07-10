# Introduction
This project is about the game of East Wind in Beijing.

## Data Prepare

###第一步：
挑选验证集 （prepare + formal + final）

1.先将final的train数据移到 './data/course3finalData/train' 下面
ls -s --path ./data/course3finalData/

2.生成所有数据的txt文件，（prepare + formal + final） 运行create_txt.py文件,会生成3个txt文件，所有图片对应的txt文件
python create_txt.py
然后将三个文件整合到一起，手动剪贴，复制

3.将挑选的数据的txt，复制到一个新的txt中，val.txt中。 （手动操作）
然后运行 python move2val.py  将挑选的数据移除 train目录，到一个新的目录val中，便于可视化。


###第二步，将训练数据做旋转数据增强
python rotate.py

然后修改create_txt，用下面一个main
做所有数据的train.txt
