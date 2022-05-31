import os
import sys
sys.path.append("..")
# real_path = os.path.dirname(os.path.realpath(__file__))
# sub_path = os.path.split(real_path)[0]
# os.chdir(sub_path)

from flask import Flask, request
from flask.templating import render_template
# from style_transfer import main

# Background module 
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from B_style_transfer import b_main


app = Flask(__name__)
app.debug = True

def root_path():
	'''root 경로 유지'''
	real_path = os.path.dirname(os.path.realpath(__file__))
	sub_path = "\\".join(real_path.split("\\")[:-1])
	return os.chdir(sub_path)

''' Main page '''
@app.route('/')
def index():
	return render_template('index.html')

''' Neural Style Transfer '''
@app.route('/b_style_transfer')
def bst_get():
    	return render_template('b_style_transfer.html')

@app.route('/bst_post', methods=['GET', 'POST'])
def bst_post():
	if request.method == 'POST':
		#Content Image
		content_image = request.files["user_img"]
		content_image.save('choco/choco_python-main/choco_python-main/flask_deep/static/images/' + str(content_image.filename))
		content_image_path = 'choco/choco_python-main/choco_python-main/flask_deep/static/images/'+str(content_image.filename)

		# Style Image
		style_image = request.files["style_img"]
		style_image.save('choco/choco_python-main/choco_python-main/flask_deep/static/21styles/' + str(style_image.filename))
		style_image_path = 'choco/choco_python-main/choco_python-main/flask_deep/static/21styles/'+str(style_image.filename)

		# Background Style Transfer # style_transfer과 연동한다
		transfer_img_path = b_main(content_image_path, style_image_path) # return -> file name
		
		c_list = content_image_path.split('/')
		content_image_path = c_list[-2]+'/'+c_list[-1]
		t_list = transfer_img_path.split('/')
		transfer_img_path = t_list[-2]+'/'+t_list[-1]
	return render_template('bst_post.html',
				content_img=content_image_path, transfer_img=transfer_img_path)


@app.route('/c_style_transfer')
def cst_get():
    	return render_template('c_style_transfer.html')

@app.route('/cst_post', methods=['GET','POST'])
def cst_post():
	if request.method == 'POST':
		#Content Image
		content_img = request.files["user_img"]
		content_img.save('/flask_deep/static/images/' + str(content_img.filename))
		content_img_path = ('/flask_deep/static/images/'+str(content_img.filename))

		#Style Image
		style = request.form['style'] #str
		style_id = request.form['style_id'] #str
		#Character Style Transfer
		# transfer_img_path = main(content_img_path, style, int(style_id)) # return -> file name
		
		c_list = content_img_path.split('/')
		content_img_path = c_list[-2]+'/'+c_list[-1]
		t_list = transfer_img_path.split('/')
		transfer_img_path = t_list[-2]+'/'+t_list[-1]
	return render_template('cst_post.html',
				content_img=content_img_path, transfer_img=transfer_img_path)
'''

@app.route('/nst_post', methods=['GET','POST'])
def nst_post():
	if request.method == 'POST':
		root_path()

		# Reference Image
		refer_img = request.form['refer_img']
		refer_img_path = '/images/nst_get/'+str(refer_img)

		# User Image (target image)
		user_img = request.files['user_img']
		user_img.save('./flask_deep/static/images/'+str(user_img.filename))
		user_img_path = '/images/'+str(user_img.filename)

		# Neural Style Transfer 
		transfer_img = neural_style_transfer.main(refer_img_path, user_img_path)
		transfer_img_path = '/images/'+str(transfer_img.split('/')[-1])

	return render_template('nst_post.html', 
					refer_img=refer_img_path, user_img=user_img_path, transfer_img=transfer_img_path)
'''