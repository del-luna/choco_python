import os
import sys
sys.path.append("..")

from flask import Flask, request, flash
from flask.templating import render_template
from style_transfer import main
from cast import cast_main

app = Flask(__name__)
app.debug = True

''' Main page '''
@app.route('/')
def index():
	return render_template('index.html')

''' Neural Style Transfer '''
@app.route('/b_style_transfer')
def bst_get():
    	return render_template('b_style_transfer.html')

@app.route('/bst_post', methods=['GET','POST'])
def bst_post():
	if request.method == 'POST':
		#Content Image
		content_img = request.files["user_img"]
		content_img.save('./flask_deep/static/testA/' + str(content_img.filename))
		content_img_path = './flask_deep/static/testA/'+str(content_img.filename)

		#Style Image
		style_img = request.files["style_img"]
		style_img.save('./flask_deep/static/testB/' + str(content_img.filename))
		style_img_path = './flask_deep/static/testB/'+str(content_img.filename)

		#Background Style Transfer
		transfer_img_path = cast_main(content_img_path, style_img_path) # return -> file name

		print(f'content: {content_img_path}')
		print(f'transfer: {transfer_img_path}')

		c_list = content_img_path.split('/')
		content_img_path = c_list[-2]+'/'+c_list[-1]
		t_list = transfer_img_path.split('/')
		transfer_img_path = t_list[-3]+'/'+t_list[-2]+'/'+t_list[-1]

	return render_template('bst_post.html',content_img=content_img_path, transfer_img=transfer_img_path)


@app.route('/c_style_transfer')
def cst_get():
    	return render_template('c_style_transfer.html')

@app.route('/cst_post', methods=['GET','POST'])
def cst_post():
	if request.method == 'POST':
		#Content Image
		content_img = request.files["user_img"]
		content_img.save('./flask_deep/static/images/' + str(content_img.filename))
		content_img_path = './flask_deep/static/images/'+str(content_img.filename)

		#Style Image
		style = request.form['style'] #str
		style_id = request.form['style_id'] #str
		#Character Style Transfer
		transfer_img_path, alert = main(content_img_path, style, int(style_id)) # return -> file name
		#print(f'Alert: {alert}')
		c_list = content_img_path.split('/')
		content_img_path = c_list[-2]+'/'+c_list[-1]
		t_list = transfer_img_path.split('/')
		transfer_img_path = t_list[-2]+'/'+t_list[-1]
	if alert:
		flash("얼굴을 탐지하지 못했습니다.\n 성능이 떨어질 수 있습니다.")
		return render_template('cst_post.html',content_img=content_img_path, transfer_img=transfer_img_path)
	else:
		return render_template('cst_post.html',content_img=content_img_path, transfer_img=transfer_img_path)

'''
(soyeah 수정)
위와 마찬가지로 https://초코파이썬_홈페이지_주소/case로 넘어가게끔 하는 코드
'''
@app.route('/case')
def case_get():
    	return render_template('case.html')
 
 '''
 bst_post.html 에서 case.html(= /case)로 넘어갈 때 POST를 받으면 아래의 함수가 작용하고, return 값을
 /case 에 전달함
 
 근데 뭐가 잘못 됐는지 작동을 하지 않아서 주석처리 하겠음

#아래는 가장 최근의 파일 이름을 return 함
@app.route('/case', methods=['GET','POST'])
def case_post():
    files_Path = "/static/testB/" # 파일들이 들어있는 폴더
    file_name_and_time_lst = []
    # 해당 경로에 있는 파일들의 생성시간을 함께 리스트로 넣어줌. 
    if request.method == "POST":
        for f_name in os.listdir(f"{files_Path}"):
            written_time = os.path.getctime(f"{files_Path}{f_name}")
            file_name_and_time_lst.append((f_name, written_time))
        # 생성시간 역순으로 정렬하고,
        sorted_file_lst = sorted(file_name_and_time_lst, key=lambda x: x[1], reverse=True)
        # 가장 앞에 이는 놈을 넣어준다.
        recent_file = sorted_file_lst[0]
        recent_file_name = recent_file[0]
    return render_template('case.html', transfer_img = recent_file_name)

 '''
 
 '''
위와 마찬가지로 https://초코파이썬_홈페이지_주소/griptok 으로 넘어가게끔 하는 코드
'''

@app.route('/griptok')
def griptok_get():
		return render_template('griptok.html')

