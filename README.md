# *GraduateProject*
随机*MAC*地址条件下移动设备个数估计方法  
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
│  │  fileDataStatistics.py
│  │  getFileName.py
│  │  getMacModel.py
│  │  getTestData.py
│  │  getTrainData.py
│  │  mlp_ConversionMacAddress.py
│  │  mlp_test.py
│  │  mnist_model-checkpoint.ipynb
│  └─mnist                  
├─data                                //原始数据
│      MacModels.txt
│      raw_dataset_label.txt
│      raw_dataset_label.zip    
├─datas                               //拆分后的数据
├─paper                               //论文
├─picture                             //可视化图像
└─README.md                           //help
```
#### 项目进度

- **2022-02-12 20:16:17**    [*raw_dataset_label.txt*](https://github.com/DongTin/GraduationProject/blob/main/data/raw_dataset_label.txt)原始数据处理 

- **2022-03-01 12:10:11**     *MacModels*存储（统一模型）  

- **2022-03-03 02:19:54**     mlp复现准备工作、*Probe Request*帧输入格式修改工作  

- **2022-03-09 18:08:07**     输入格式处理和数据归一化

    > 参考论文：[*Probe Request Based Device Identification Attack and Defense*](https://github.com/DongTin/GraduationProject/blob/main/paper/Probe%20Request%20Based%20Device%20Identification%20Attack%20and%20Defense.pdf)
- **2022-03-10 21:07:25**     输出*numpy&tag*数据以及*mlp*框架梳理
- **2022-03-11 03:04:50**     完成了*mlp*输入数据格式转化、针对*mac*地址去随机的*mlp*的初步构建
- **2022-03-12 03:11:26**     修改*bug*、实现针对*mac*地址去随机的*mlp*并且训练15轮后准确率在81%以上
- **2022-03-12 17:53:32**     数据详情的可视化
- **2022-03-13 02:08:31**     根据*MacModels.txt*对输入格式进行调整准确率达到了97%以上、开始论文准备工作

#### *BUG LIST*
- [x]  *getTestData*无法跨文件获取数据

#### *OPTIMIZE LIST*
- [x] *mlp*准确率优化
- [ ]  ~~*conversion*的数据转化归一流程速度优化~~(多线程尝试后结果不理想 暂且搁置)
