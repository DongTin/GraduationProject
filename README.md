# GraduateProject
随机MAC地址条件下移动设备个数估计方法  
*Method for estimating the number of mobile devices under the condition of random MAC address*

#### 题目类型：理论研究

#### 内容简介：
剖析移动设备主动扫描过程中发出的*Probe Request*帧的结构特征，基于某种聚类算法或机器学习方法，估计混合MAC地址条件下的移动设备个数。 

#### 环境依赖：

python 3.8

##### 目录结构描述

```
.
├─code
│  │  conversion.py
│  │  dataDeal.ipynb
│  │  getMacModel.py
│  │  mlp_test.py
│  │  mnist_model-checkpoint.ipynb
│  │  test1.py
│  │  test2.py  
│  ├─.ipynb_checkpoints     
│  └─mnist                  
├─data                                //原始数据
│      MacModels.txt
│      raw_dataset_label.txt
│      raw_dataset_label.zip    
├─datas                               //拆分后的数据
├─paper                               //论文
└─README.md                           //help
```
#### 项目进度

- **2022-02-12 20:16:17**    [*raw_dataset_label.txt*](https://github.com/DongTin/GraduationProject/blob/main/data/raw_dataset_label.txt)原始数据处理 

- **2022-03-01 12:10:11**     *MacModels*存储（统一模型）  

- **2022-03-03 02:19:54**     mlp复现准备工作、*Probe Request*帧输入格式修改工作  

- **2022-03-09 18:08:07**     输入格式处理和数据归一化

    > 参考论文：[*Probe Request Based Device Identification Attack and Defense*](https://github.com/DongTin/GraduationProject/blob/main/paper/Probe%20Request%20Based%20Device%20Identification%20Attack%20and%20Defense.pdf)