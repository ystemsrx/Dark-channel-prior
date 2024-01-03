[中文版](README.zh.md)

# Dark Channel Dehazing

## Overview
This Python script implements a dark channel-based algorithm to remove haze from images. It is an implementation of the algorithm described in the paper "Single Image Haze Removal Using Dark Channel Prior" by He, Sun, and Tang. The script utilizes OpenCV and NumPy libraries for image processing, offering an efficient solution for image dehazing.

## Features
- **Dark Channel Algorithm:** Utilizes the dark channel prior for haze removal in images, as described in He, Sun, and Tang's 2010 paper.
- **Image Enhancement:** Improves the visibility of images by reducing the effect of atmospheric haze.

## Paper Reference
He, K., Sun, J., & Tang, X. (2010). Single Image Haze Removal Using Dark Channel Prior. IEEE Transactions on Pattern Analysis and Machine Intelligence, 33(12), 2341-2353.

## Requirements
- Python 3
- OpenCV Python library (`cv2`)
- NumPy Python library (`numpy`)

## Installation
1. Ensure Python 3 is installed on your system.
2. Install required libraries: `pip install opencv-python numpy`.

## Usage
1. Run the script using Python: `python dark channel prior.py`.
2. Enter the name of the image file when prompted.
3. The original and dehazed images will be displayed.

```txt
# Selected Code Snippet from Script
else:
    print("Bad image shape, input must be color image")
    return None

img_gray = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
local_min = 255

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        local_min = min(img[i, j, :])
```

## Example
You can test the script with any image that has haze. The script will process the image and display both the original and the dehazed version.

## Download EXE 
https://drive.google.com/file/d/1qv-fWWNGFNHCj8HPPkq97NCgyUekMTmt/view?usp=sharing
