from pathlib import Path
emoji_to_label={"😊":0,"😱":1,"😢":2,
"😪":3,"😈":4,"😃":5,"😳":6,"😭":7,"😁":8, "😝":9,
   "😍":10,"💦":11,"😇":12,"😅":13,"🤣":14,"😫":15,
   "👀":16,"😤":17,"😡":18,"😋":19}
label_to_emoji={0:"😊",1:"😱",2:"😢",3:"😪",4:"😈",5:"😃",6:"😳",7:"😭",8:"😁", 9:"😝",
   10:"😍",11:"💦",12:"😇",13:"😅",14:"🤣",15:"😫",16:"👀",17:"😤",18:"😡",19:"😋"}
BASE_DIR="./"
VOCAB_FILE=BASE_DIR + "vocab/vocab.txt"
BERT_CONFIG = BASE_DIR+"weights/bert_config.json"
model_file = BASE_DIR + "weights/pytorch_model.bin"
MODEL_FILE = BASE_DIR + "weights/bert_fine_tuning.pth"
PKL_FILE = BASE_DIR + "data/text.pkl"
DATA_PATH = BASE_DIR + "data"
max_length = 256
offset=[-0.2183,  0.5670, -0.7703, -1.7347, -0.3613, -0.9013,  1.0803, -1.3668,
         -1.6816, -0.9048,  1.2739,  0.6666,  0.4471, -1.7258,  1.3446,  0.0163,
         -1.6485,  0.4534, -0.6312, -0.5033]