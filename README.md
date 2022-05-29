# Flask_DL-service
Flask for Computer-Vision Prototype
> Link : http://choco-python.kro.kr:5002/
(상시 가동중은 아닙니다.😅)

### Function 
* Neural Style Transfer
  * Background Style Transfer
  * Character Style Transfer

### Setting Virtualenv
#### 1. Create virtualenv in Anaconda
```cmd
> conda create -n flask python=3.8
```
#### 2. Activate virtualenv
```cmd
> conda activate flask
```

### Install Requirements
```cmd
(flask) > cd ~pyflask
(flask) ~pyflask > pip install -r requirements.txt
```
### Start Server
```cmd
(venv_flask) ~pyflask\flask_deep\darkflow_yolo > cd ../
(venv_flask) ~pyflask\flask_deep > cd ../
(venv_flask) ~pyflask > python start_flask.py
```

<br>

## Main Page
<img src="./flask_deep/static/assets/img/index-main.jpg">

## Style Transfer
* Input
<img src="./etc/nst-get.png">

* Output
<img src="./etc/nst-post.png">

## Reference

- https://github.com/jaehyeongAN/PyFlask_DL-service
- https://github.com/williamyang1991/DualStyleGAN

- https://github.com/zyxElsa/CAST_pytorch