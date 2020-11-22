from emoji_output import emoji_output
from utils.config import *
from utils.predict import predict,bert_model

print("how many emojis do you want ?")
emoji_num=int(input())
quit=False
while quit==False:
    print("Please input the text you want to emojify.")
    input_text=input()
    if input_text=="q" or input_text=="\n":
        exit()
    print(emoji_output(input_text,emoji_num))