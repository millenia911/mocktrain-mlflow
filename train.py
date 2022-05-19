import mlflow
import argparse
import os
from random import sample
from shutil import copyfile

os.system('pip install azure-storage-blob')
os.system('pip install azure-identity')
os.system('nvidia-smi')
os.system('chmod +x ./blob-data-extractor.sh')
os.system('./blob-data-extractor.sh')
os.system('ls .')
os.makedirs('images', exist_ok=True)
images = os.listdir('./new_dataset/dataset_val')
images = sample(images, 10)

path = './new_dataset/dataset_val'
new_path = './images'
for im in images:
    src = os.path.join(path, im)
    dst = os.path.join(new_path, im)
    copyfile(src, dst)

parser = argparse.ArgumentParser(description="Training Script")
parser.add_argument('--path', type=str, default=None)
opt = parser.parse_args()

mlflow.start_run()
mlflow.log_param("name", 12)
mlflow.log_param("path", opt.path)
mlflow.log_artifact("./images", "logged_images/")
mlflow.end_run()