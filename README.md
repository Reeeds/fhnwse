
venv
 python -m venv [directory]
 source myvenv/bin/activate

*********************************************

conda
conda create --name tftestnew python=3.x
conda create --name tftestnew

*********************************************

Installation Guide Apple M1
https://www.youtube.com/watch?v=_CO-ND1FTOU
https://github.com/jeffheaton/t81_558_deep_learning/blob/master/install/tensorflow-install-mac-metal-jul-2021.ipynb


brew install miniforge
conda env create -f tensorflow-apple-metal.yml -n tensorflow _      --> in Ordner wo yml file ist
conda activate tensorflow
conda install nb_conda
jupyer notebook       --> richtiger Kernel auswählen



Test in JN

import sys

import tensorflow.keras
import pandas as pd
import sklearn as sk
import tensorflow as tf

print(f"Tensor Flow Version: {tf.__version__}")
print(f"Keras Version: {tensorflow.keras.__version__}")
print()
print(f"Python {sys.version}")
print(f"Pandas {pd.__version__}")
print(f"Scikit-Learn {sk.__version__}")
gpu = len(tf.config.list_physical_devices('GPU'))>0
print("GPU is", "available" if gpu else "NOT AVAILABLE")

--> Apple M1 Pro


Info RSC:
- run cifar10...py mit VS Code Run Button ausführen
