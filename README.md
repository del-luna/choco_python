# Deep learning Style Transfer Service Using Flask



<!-- 헤더 -->
![header](https://capsule-render.vercel.app/api?type=slice&color=auto&height=200&section=header&text=Hello&desc=We are%20Choco %Python %20team&fontSize=60&rotate=14&fontAlignY=25&fontAlign=75&descAlignY=43&descAlign=80&&animation=twinkling)



<div align=center>
<!--소개-->
<h3>:raised_hands: Introduction </h3>
:chocolate_bar: 안녕하세요! 팀 초코파이썬입니다.
<br/><br/>
 <!--기술스택-->
   <h3>:hammer:Skill </h3>
  <!--클라우드-->
  <img src="https://img.shields.io/badge/GCP-4285F4?style=plastic&logo=googlecloud&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=plastic&logo=docker&logoColor=white"/>
   <br/>
  <!--웹-->
   <img src="https://img.shields.io/badge/Flask-000000?style=plastic&logo=flask&logoColor=white"/>
  <br/>
  <!--인공지능-->
   <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=plastic&logo=pytorch&logoColor=white"/>
    <br/>
  <!--언어-->
    <img src="https://img.shields.io/badge/C++-00599C?style=flat&logo=Cplusplus&logoColor=white"/>
    <img src="https://img.shields.io/badge/Python-3776AB?style=plastic&logo=python&logoColor=white"/>
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=JavaScript&logoColor=white"/>

<br/><br/>



**Flask for Style-Transfer Prototype**

> Link : http://chocopython.kro.kr:5002/
(상시 가동중은 아닙니다.😅)


</div>

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
