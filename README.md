# BadImageFinder

### Requirements 
- python 2.7
- opencv 2.4 (you can take binary from repository)
- tensorflow >=1.14
- flask
- numpy
- pathlib

### Usage
- Firstly run the api: `python ./manage_worse.py`
- One is able to send a http request to the api as follows
```java
String url = "your server ip:6000/hehe/worse_image";

```

### Train model
- create directory 1 (with non-porn images), 2 (with porn images), cache (empty)
- Run `./pcr.py train` (to train opencv & sklearn) or `./nnpcr.py train` (for tensorflow one).

After train finish you will see accuracy and you will get "model.bin" file with your trained model. Now you can use it to detect porn (see functions predictTest and predictUrl). I added a sample model (model.bin) - you can test it without training your own model, but I recomend you to gather some huge collection of images (eg, 50K) for best results.

### License
Public domain (but it may use some patented algorithms, eg. SIFT - so you should check license of all used libraries).
