import argparse
from email.policy import default
import os

class Options():
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="parser for PyTorch-Style-Transfer")

        # evaluation args
        # eval_arg = subparsers.add_parser("eval", help="parser for evaluation/stylizing arguments")
        self.parser.add_argument("--ngf", type=int, default=128,
                                help="number of generator filter channels, default 128")
        # self.parser.add_argument("--content-image", type=str, required=True,
        #                         help="path to content image you want to stylize")
        # self.parser.add_argument("--style-image", type=str, default="images/9styles/candy.jpg",
        #                         help="path to style-image")
        self.parser.add_argument("--content-size", type=int, default=512,
                                help="factor for scaling down the content image")
        self.parser.add_argument("--style-size", type=int, default=512,
                                help="size of style-image, default is the original size of style image")
        self.parser.add_argument("--style-folder", type=str, default="images/9styles/",
                                help="path to style-folder")
        # self.parser.add_argument("--output-image", type=str, default="flask_deep/static/inference_images/output.jpg",
        #                         help="path for saving the output image")
        self.parser.add_argument("--model", type=str, default="choco/choco_python-main/choco_python-main/model/21styles.model",
                                help="saved model to be used for stylizing the image")
        self.parser.add_argument("--cuda", type=int, default=0,
                                help="set it to 0 for running on CPU, 1 for GPU")    
        self.parser.add_argument("--vgg-model-dir", type=str, default="model/",
                                help="directory for vgg, if model is not present in the directory it is downloaded")

    def parse(self):
        return self.parser.parse_args()
