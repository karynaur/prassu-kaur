from fastai.text.all import *
import torch
from transformers import GPT2TokenizerFast, GPT2LMHeadModel
import pandas as pd
import sys

pretrained_weights = 'gpt2'
tokenizer = GPT2TokenizerFast.from_pretrained(pretrained_weights)


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


learn=load_learner('rupi.pkl')
prompt=sys.argv[1]
prompt_ids = tokenizer.encode(prompt)
inp = tensor(prompt_ids)[None]#.cuda()
preds=learn.model.generate(inp,
                           do_sample=True, 
                           max_length=30, 
                           min_length=5,
                           top_k=40,
                           num_return_sequences=1)
poem=tokenizer.decode(preds[0].cpu().tolist())+'.'


def get_pic():
  photofile = random.choice(os.listdir("rupicursion/"))
  img_tag = '<img src="rupicursion/{0}">'.format(photofile)
  return img_tag

def make_html(poetry):
  f = open('poetry.html','w')
  poetry = poetry.replace("\n","<br/>")
  text = "<html><body style=\"font-family:Times\"> "+poetry+"<p> - prassu kaur </p>"+get_pic()+"</body></html>"
  f.write(text)
  f.close()

make_html(poem)
