from utils.config import *
from utils.predict import predict, bert_model
import sys
net_trained=bert_model()
def emoji_output(input_text,emoji_num):
    s=input_text
    output=predict(input_text, net_trained, emoji_num).tolist()
    for i in range(len(output[0])):
        s+=label_to_emoji[output[0][i]]
    return s