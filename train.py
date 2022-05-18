import mlflow
import argparse
import os
os.system('nvidia-smi')
print("trigger from new branch")

parser = argparse.ArgumentParser(description="Training Script")
parser.add_argument('--path', type=str, default=None)
opt = parser.parse_args()

mlflow.start_run()
mlflow.log_param("name", 12)
mlflow.log_param("path", opt.path)
mlflow.log_param("newbranch", "True")
mlflow.end_run()