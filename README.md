# VideoDiff：基于ffmpeg，实现视频抽帧比较工具
## 使用场景：在视频渲染模块发生迭代，快速回归测试其产出的视频是否存在问题，从而节省人工回归成本
###  <center> 原理图
![alt 流程图](https://github.com/jiangliuer32/Image/blob/d8d6394099ece859689e9e4a7c6d3d1fb348f9f7/iamge/diffProcess.png)
### 一、环境准备
* ffmpeg：https://www.ffmpeg.org/download.html
### 二、运行方式
#### 1.脚本运行：找到Run.py，填入对应参数（可自行调整抽帧次数）

#### 2.图形界面运行：python TestGuiRun.py（已安装requirements.txt里的第三包）


### 三、运行结果说明

### 四、参考
https://github.com/kkroening/ffmpeg-python/tree/master/examples