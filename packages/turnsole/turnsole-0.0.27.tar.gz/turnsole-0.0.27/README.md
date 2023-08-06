# turnsole
A series of convenience functions make your machine learning project easier 

## 安装方法

### Latest release
`pip install turnsole`
> 项目暂不开源，因此该安装方法暂时不保证能用

### Developer mode

`pip install -e .`

## 快速上手
### PDF 操作 
#### 智能 PDF 文件转图片
智能的把 PDF 文件里面的插图找出来，例如没有插图就将整页 PDF 截图下来，也能智能的将碎图拼接在一起

##### Example:
<pre># pdf_path 表示 PDF 文件的路径，输出 images 按页码进行汇总输出
images = turnsole.pdf_to_images(pdf_path)</pre>

### 图像操作工具箱 
#### base64_to_bgr / bgr_to_base64
图像和 base64 互相转换

##### Example:
<pre>image = turnsole.base64_to_bgr(img64)
img64 = turnsole.bgr_to_base64(image)</pre>

### image_crop
根据 bbox 在 image 上进行切片，如果指定 perspective 为 True 则切片方式为透视变换（可以切旋转目标）

##### Example:
<pre>im_slice_no_perspective = turnsole.image_crop(image, bbox)
im_slice = turnsole.image_crop(image, bbox, perspective=True)</pre>

##### Output:

<img src="docs/images/image_crop.png?raw=true" alt="image crop example" style="max-width: 200px;">

### OCR 引擎模块 
OCR 引擎指的是一系列跟 OCR 相关的底层模型，我们提供了这些模型的函数式调用接口和标准 API 

- [x] ADC :tada:
- [x] DBNet :tada:
- [x] CRNN :tada:
- [x] Object Detector :tada:
- [x] Signature Detector :tada:

#### 免费试用
```python
import requests

results = requests.post(url=r'http://139.196.149.46:9001/gen_ocr', files={'file': open(file_path, 'rb')}).json()
ocr_results = results['ocr_results']
```

#### Prerequisites
由于 OCR 引擎模块依赖于底层神经网络模型，因此需要先用 Docker 挂载底层神经网络模型 

首先把 ./model_repository 文件夹和里面的模型放到项目根目录下再启动，如果没有相关模型找 [lvkui](lvkui@situdata.com) 要 

使用起来非常简单，你只需要启动对应的 Docker 容器即可

```bash
docker run --gpus="device=0" --rm -p 8000:8000 -p 8001:8001 -p 8002:8002 -v $PWD/model_repository:/models nvcr.io/nvidia/tritonserver:21.10-py3 tritonserver --model-repository=/models
```

#### ADC
通用文件摆正算法

``` 
from turnsole.ocr_engine import angle_detector

image_rotated, direction = angle_detector.ADC(image, fine_degree=False)
```

#### DBNet
通用文字检测算法

``` 
from turnsole.ocr_engine import text_detector

boxes = text_detector.predict(image)
```

#### CRNN
通用文字识别算法

``` 
from turnsole.ocr_engine import text_recognizer

ocr_result, ocr_time = text_recognizer.predict_batch(image, boxes)
```

#### Object Detector
通用文件检测算法

``` 
from turnsole.ocr_engine import object_detector

object_list = object_detector.process(image)
```

#### Signature Detector
签字盖章二维码检测算法

``` 
from turnsole.ocr_engine import signature_detector

signature_list = signature_detector.process(image)
```

#### 标准 API
```
python api/ocr_engine_server.py
```