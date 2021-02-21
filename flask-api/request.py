import requests
import json
from fastai.text.all import *
import torch
from transformers import GPT2TokenizerFast, GPT2LMHeadModel
import pandas as p

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


url = 'http://0.0.0.0:5000/api/'

data = {'text':'From an api '}
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=data)
print(r.json()['out'])
