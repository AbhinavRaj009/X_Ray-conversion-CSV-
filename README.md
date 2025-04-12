What This Code Does:
📂 It searches for all .jpg, .png, .jpeg files you uploaded to Colab.

📷 It reads each image in grayscale and resizes it to 128x128.

📊 It flattens each image into a row of 16,384 numbers (pixel values).

🧾 It adds all rows to a DataFrame and saves everything as xray_dataset.csv.
