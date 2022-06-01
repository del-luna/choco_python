# Choco_python - Deep learning Style Transfer Service Using Flask
**Flask for Style-Transfer Prototype**

> Link : http://chocopython.kro.kr:5002/
(상시 가동중은 아닙니다.😅)

<br>
🔨**Tools**🔨
<br>

<img src="https://img.shields.io/badge/GCP-4285F4?style=plastic&logo=googlecloud&logoColor=white"/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=plastic&logo=docker&logoColor=white"/>
<img src="https://img.shields.io/badge/Flask-000000?style=plastic&logo=flask&logoColor=white"/>
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=plastic&logo=pytorch&logoColor=white"/>
<img src="https://img.shields.io/badge/Python-3776AB?style=plastic&logo=python&logoColor=white"/>

## Updates

- [2022/06/01] BackGround Style Transfer and website linkage completed

- [2022/05/31] add docker file

- [2022/05/29] Character Style Transfer and website linkage completed

## Function 
* Neural Style Transfer
  * Background Style Transfer
  * Character Style Transfer

## **Installation**

**Clone this reop:**

```shell
git clone https://github.com/del-luna/choco_python.git
cd choco_python
```

**Dependencies:**

Caution! Works only in linux environment

All dependencies for defining the environment are provided in `environment/choco_python_env.yaml`  We recommend running this repository using [Anaconda](https://docs.anaconda.com/anaconda/install/):

```shell
conda env create -f ./environment/choco_python_env.yaml
```

### Start Server
```cmd
python start_flask.py
```

<br>

## Main Page
<img src="./flask_deep/static/assets/img/index-main.jpg">

## Character Style Transfer
* **Input**
<img src="./doc_images/get.jpg">

* **Output**
<img src="./doc_images/post.jpg">



## BackGround Style Transfer

- **Result**

  <img src="./doc_images/bg_post.png">

## Reference

- https://github.com/jaehyeongAN/PyFlask_DL-service
- https://github.com/williamyang1991/DualStyleGAN

- https://github.com/zyxElsa/CAST_pytorch
