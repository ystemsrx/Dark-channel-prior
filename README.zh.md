[English](README.md)

# 暗通道去雾

## 概述
这个Python脚本实现了一个基于暗通道的算法来去除图片中的雾。它是根据He, Sun和Tang在2010年的论文《单幅图像去雾使用暗通道先验》描述的算法实现的。该脚本使用OpenCV和NumPy库进行图像处理，提供了一个高效的图像去雾解决方案。

## 特点
- **暗通道算法：** 使用暗通道先验去除图像中的雾，如He, Sun和Tang在2010年的论文中所描述。
- **图像增强：** 通过减少大气雾的影响，提高图像的可见性。

## 论文参考
He, K., Sun, J., & Tang, X. (2010). Single image haze removal using dark channel prior. IEEE transactions on pattern analysis and machine intelligence, 33(12), 2341-2353

## 系统要求
- Python 3
- OpenCV Python库（`cv2`）
- NumPy Python库（`numpy`）

## 安装
1. 确保您的系统上安装了Python 3。
2. 安装所需库：`pip install opencv-python numpy`。

## 使用方法
1. 使用Python运行脚本：`python 暗通道去雾.py`。
2. 根据提示输入图像文件的名称。
3. 将会显示原始和去雾后的图像。

```txt
# 脚本中选取的代码片段
else:
    print("Bad image shape, input must be color image")
    return None

img_gray = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
local_min = 255

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        local_min = min(img[i, j, :])
```

## 示例
您可以使用任何有雾的图像来测试该脚本。脚本将处理图像并显示原始和去雾后的版本。

