# -*- coding: utf-8 -*-
"""x_ray.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DqSIGIunGcvY0Fu-CH86np1d5zAsN5Zt
"""

import numpy as np
import pandas as pd
import cv2

import cv2
import numpy as np
import pandas as pd
import os
from google.colab import files

# Step 1: List all images in the current directory
image_files = [f for f in os.listdir() if f.endswith(('.jpg', '.png', '.jpeg'))]

# Create a list to store all flattened image data
all_data = []

# Step 2: Loop through each image
for filename in image_files:
    # Load in grayscale
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"⚠️ Couldn't load {filename}, skipping.")
        continue

    # Resize to 128x128
    img_resized = cv2.resize(img, (128, 128))

    # Flatten and add to the list
    flattened = img_resized.flatten()
    all_data.append(flattened)

# Step 3: Convert to DataFrame and save to CSV
df = pd.DataFrame(all_data)
df.to_csv('xray_dataset.csv', index=False)

print(f"✅ Converted {len(all_data)} images into 'xray_dataset.csv'")