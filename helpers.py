# Roya Elisa Eskandani
# 24. Januar 2024

# helpers.py

"""Functions and Settings for Growing Neural Gas (GNG) Algorithm."""

import os
import sys
from typing import List
import numpy as np


img_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.gif']
def loadImages(dic: str, prefix: str) -> List[str]:
  def checkImageCount(arr: List[str]) -> None:
    n_img: int = len(arr)
    if n_img < 1:
      print(f'Interruption: Number of files = {n_img}')
      sys.exit(1)

  try:
    files = os.listdir(dic)
    files = [f'{dic}/{file}' for file in files if any(file.lower().startswith(prefix) and file.lower().endswith(ext) for ext in img_extensions)]
    
    checkImageCount(files)

    return sorted(files)

  except FileNotFoundError:
    print(f'Interruption: The directory \'{dic}\' could not be found.')
    sys.exit(1)


def convertDtypeImage(img: np.ndarray) -> np.ndarray:
  if img.dtype == 'uint8' and img.dtype != 'float32':
    fac_dtype: float = 1/255
    img = (img * fac_dtype).astype(np.float32)
  elif img.dtype != 'uint8' and img.dtype != 'float32':
    print(f'Interruption: Datatype of {img} not correct.')
    sys.exit(1)
      
  return img