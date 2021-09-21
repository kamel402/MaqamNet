DATA_DIR = './data/'
BASE_DIR = './data/MaqamNet/' # data dir for this model 
MTT_DIR = './data/MaqamPub/mp3/' # MTT data dir 
AUDIO_DIR = './data/pubMaqam_mp3s_to_npy/'
ANNOT_FILE = './data/annotations_final.csv'
LIST_OF_TAGS = './data/MaqamNet/4_tags.txt'

DEVICE_IDS=[0,1]

# audio params 
SR = 22050
NUM_SAMPLES = 59049
NUM_TAGS = 4

# train params 
BATCH_SIZE =16
LR = 0.008
DROPOUT = 0.5
NUM_EPOCHS = 50