# turnsole
A series of convenience functions make your machine learning project easier 

## 安装方法

### Latest release
`pip install turnsole`
> 项目暂不开源，因此该安装方法暂时不保证能用

### Developer mode

`pip install -e .`

## 快速上手

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