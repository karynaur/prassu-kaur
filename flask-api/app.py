from flask import Flask, request, redirect, url_for, flash, jsonify
from flask_restful import Api,Resource,reqparse
import numpy as np
import pickle as p
import json
from fastai.text.all import *
import torch
from transformers import GPT2TokenizerFast, GPT2LMHeadModel
import pandas as pd
import os
import requests
app = Flask(__name__)
api=Api(app)

@app.route('/api/', methods=['POST'])
#@staticmethod
def post():
    data = reqparse.RequestParser()
    data.add_argument('text')
    args=data.parse_args()
    prompt_ids = tokenizer.encode(args['text'])
    inp = tensor(prompt_ids)[None]
    preds=learn.model.generate(inp,
                           do_sample=True,
                           max_length=30,
                           min_length=5,
                           top_k=40,
                           num_return_sequences=1)
    return {'out':tokenizer.decode(preds[0].cpu().tolist())}

def tokenize(text):
    toks = tokenizer.tokenize(text)
    return tensor(tokenizer.convert_tokens_to_ids(toks))

class TransformersTokenizer(Transform):
    def __init__(self, tokenizer): self.tokenizer = tokenizer
    def encodes(self, x):
        return x if isinstance(x, Tensor) else tokenize(x)

    def decodes(self, x): return TitledStr(self.tokenizer.decode(x.cpu().numpy()))

class DropOutput(Callback):
  def after_pred(self):self.learn.pred=self.pred[0]



if __name__ == '__main__':
    pretrained_weights = 'gpt2'
    tokenizer = GPT2TokenizerFast.from_pretrained(pretrained_weights)
    learn=load_learner('/mnt/e/karynaur/prassu-kaur-poetry/rupi.pkl')
    app.run(debug=True, host='0.0.0.0')
