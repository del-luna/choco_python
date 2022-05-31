##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## Created by: Hang Zhang
## ECE Department, Rutgers University
## Email: zhang.hang@rutgers.edu
## Copyright (c) 2017
##
## This source code is licensed under the MIT-style license found in the
## LICENSE file in the root directory of this source tree 
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import os
import sys
import time
import random
import numpy as np
from tqdm import tqdm, trange

import torch
from torch.optim import Adam
from torch.autograd import Variable
from torch.utils.data import DataLoader

from torchvision import datasets
from torchvision import transforms

import module.utils as utils
from module.net import Net, Vgg16
from module.option import Options

def b_main(content_image_path, style_image_path):
    # figure out the experiments type
    '''
    args.content_image = content_image_path
    args.style_image = style_image_path

    '''
    args = Options().parse()
    
    # if args.subcommand is None:
    # #     raise ValueError("ERROR: specify the experiment type")
    # if args.cuda and not torch.cuda.is_available():
    #     raise ValueError("ERROR: cuda is not available, try running on CPU")

    evaluate(args, content_image_path, style_image_path)


def evaluate(args, content_image_path, style_image_path):
    content_image = utils.tensor_load_rgbimage(content_image_path, size=args.content_size, keep_asp=True)
    content_image = content_image.unsqueeze(0)
    style = utils.tensor_load_rgbimage(style_image_path, size=args.style_size)
    style = style.unsqueeze(0)    
    style = utils.preprocess_batch(style)

    style_model = Net(ngf=args.ngf)
    model_dict = torch.load(args.model)
    model_dict_clone = model_dict.copy()
    for key, value in model_dict_clone.items():
        if key.endswith(('running_mean', 'running_var')):
            del model_dict[key]
    style_model.load_state_dict(model_dict, False)

    if args.cuda:
        style_model.cuda()
        content_image = content_image.cuda()
        style = style.cuda()

    style_v = Variable(style)

    content_image = Variable(utils.preprocess_batch(content_image))
    style_model.setTarget(style_v)

    output = style_model(content_image)
    #output = utils.color_match(output, style_v)

    '''
    output_image_dir 경로 체크하기
    '''
    output_image_name = 'output.jpg'
    output_image_dir = 'choco/choco_python-main/choco_python-main/flask_deep/static/inference_images/'
    output_image_path = os.path.join(output_image_dir, output_image_name)

    utils.tensor_save_bgrimage(output.data[0], output_image_path, args.cuda)
    return output_image_path


if __name__ == "__main__":
   b_main()
