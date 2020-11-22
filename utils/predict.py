import mojimoji
import re
import os
import string
import torch
import torchtext
import pickle
from utils.bert import get_config, load_vocab, BertModel, BertTokenizer,BertForEmoji,set_learned_params
from utils.config import * 

def preprocessing_text(text):
    # 半角・全角の統一
    text = mojimoji.han_to_zen(text) 
    # 改行、半角スペース、全角スペースを削除
    text = re.sub('\r', '', text)
    text = re.sub('\n', '', text)
    text = re.sub('　', '', text)
    text = re.sub(' ', '', text)
    # 数字文字の一律「0」化
    text = re.sub(r'[0-9 ０-９]+', '0', text)  # 数字

    # カンマ、ピリオド以外の記号をスペースに置換
    for p in string.punctuation:
        if (p == ".") or (p == ","):
            continue
        else:
            text = text.replace(p, " ")

    return text



# 前処理と単語分割をまとめた関数を定義
def tokenizer_with_preprocessing(text):
    tokenizer_bert = BertTokenizer(vocab_file=VOCAB_FILE, do_lower_case=False)
    text = preprocessing_text(text)
    ret = tokenizer_bert.tokenize(text)  
    return ret

"""
def pickle_dump(TEXT,path):
    with open(path, "wb") as f:
        pickle.dump(TEXT,f)
"""

def pickle_load(path):
    with open(path, "rb") as f:
        TEXT=pickle.load(f)
    return TEXT

def bert_model():
    config=get_config(file_path=BERT_CONFIG)
    net_bert=BertModel(config)
    net_trained=BertForEmoji(net_bert)
    net_trained.load_state_dict(torch.load(MODEL_FILE,map_location=torch.device('cpu')))
    device=torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    net_trained.eval()
    net_trained.to(device)
    return net_trained


def predict(input_text, net_trained,candidate_num=3,output_print=False):
    TEXT=pickle_load(PKL_FILE)
    device=torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    tokenizer_bert=BertTokenizer(vocab_file=VOCAB_FILE, do_lower_case=False)
    text=preprocessing_text(input_text)
    text=tokenizer_bert.tokenize(text)
    text.insert(0,"[CLS]")
    text.append("[SEP]")
    token_ids=torch.ones((max_length)).to(torch.int64)
    ids_list=list(map(lambda x:TEXT.vocab.stoi[x],text))
    for i, index in enumerate(ids_list):
        token_ids[i]=index
    ids_list=token_ids.unsqueeze_(0)
    input=ids_list.to(device)
    input_mask=(input != 1)
    outputs, attention_probs=net_trained(input, token_type_ids=None, attention_mask=None, 
                    output_all_encoded_layers=False, attention_show_flg=True)
    
    offset_tensor = torch.tensor(offset,device=device)
    outputs-=offset_tensor
    if output_print==True:print(outputs)
    _, preds=torch.topk(outputs,candidate_num)
    return preds
