import os
from PIL import Image
import cv2

def get_file_size(file_path):
    return os.path.getsize(file_path)

def reduce_file_size(image_path, output_path, target_size_mb=5):
    img = Image.open(image_path)
    img = img.convert("RGB")
    
    # base_width = 800
    # w_percent = (base_width / float(img.size[0]))
    # h_size = int((float(img.size[1]) * float(w_percent)))
    # img = img.resize((base_width, h_size), Image.ANTIALIAS)

    img.save(output_path, "JPEG", quality=85)
    
    file_size_kb = get_file_size(output_path) / 1024.0
    file_size_mb = file_size_kb / 1024.0

    if file_size_mb > target_size_mb:
        img_cv = cv2.imread(output_path)
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 50]
        cv2.imwrite(output_path, img_cv, encode_param)

def process_folders(start=1, end=18):
    for i in range(start, end + 1):
        folder_name = str(i)
        new_folder_name = f"{i}_new"
        
        if not os.path.exists(new_folder_name):
            os.makedirs(new_folder_name)
        
        for filename in os.listdir(folder_name):
            if filename.endswith(('.jpg', '.jpeg', '.png')):
                old_file_path = os.path.join(folder_name, filename)
                new_file_path = os.path.join(new_folder_name, filename)
                reduce_file_size(old_file_path, new_file_path)

if __name__ == "__main__":
    process_folders()
