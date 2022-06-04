# Deep learning Style Transfer Service Using Flask



<!-- 헤더 -->
![header](https://capsule-render.vercel.app/api?type=transparent&height=200&section=header&text=Choco%20Python&desc=Style%20Transfer%20Project&fontColor=5CFFD1&fontSize=60&rotate=&fontAlignY=25&fontAlign=50&descAlignY=50&descAlign=50&&animation=twinkling)



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
  <img src="https://img.shields.io/badge/Jenkins-D24939?style=plastic&logo=Jenkins&logoColor=white"/>
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

</div>

**Flask for Style-Transfer Prototype**

> Link : http://chocopython.kro.kr:5002/
(상시 가동중은 아닙니다.😅)



```shell
start_flask.py (우리가 실행하는 메인 파일)
flask_deep
		|____ static (asset, css, image등을 관리하는 폴더)
		|		|____ images (유저가 올린 charatcter content image가 저장되는 곳)
		|		|____ inference_images (모델 적용 후 character transfer image가 저장되는 곳)
		|		|____ testA(유저가 올린 background content image가 저장되는 곳)
		|		|____ testB(유저가 올린 background style image가 저장되는 곳)
		|
		|____ template (html 파일 관리)
	 	|        |____ index.html (메인페이지)
		|		|____ b_style_transfer.html (백그라운드 스타일 변환 초기 페이지)
		|		|____ bst_post.html (백그라운드 스타일 변환 적용 후 페이지)
		|		|____ c_style_transfer.html (캐릭터 스타일 변환 초기 페이지)
		|		|____ cst_post.html (캐릭터 스타일 변환 적용 후 페이지)
		|		|____ case.html(아직 깃에 올라가있지 않음(merge 예정), 모델 아웃풋 보여주는 페이지				|				(bst_post, cst_post)에서 버튼을 누를 시 여기로 옴->핸드폰 케이스 생성하는 페이지)
		|
		|____ __init__.py (flask 웹페이지 관리하는 파일 라우터 등이 여기서 작성됨)
```



## Updates

- [2022/06/04] README update

- [2022/06/02] add Jenkins

- [2022/06/01] BackGround Style Transfer and website linkage completed

- [2022/05/31] add docker file

- [2022/05/29] Character Style Transfer and website linkage completed

## Function 
* Neural Style Transfer
  * BackGround Style Transfer
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
