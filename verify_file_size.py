import os

def get_file_size(file_path):
    return os.path.getsize(file_path) / (1024 * 1024)  # Size in MB

def check_file_sizes(start=1, end=18, target_size_mb=5):
    oversized_files = []
    for i in range(start, end + 1):
        new_folder_name = f"{i}_new"
        for filename in os.listdir(new_folder_name):
            if filename.endswith(('.jpg', '.jpeg', '.png')):
                file_path = os.path.join(new_folder_name, filename)
                file_size_mb = get_file_size(file_path)
                
                if file_size_mb > target_size_mb:
                    oversized_files.append((file_path, file_size_mb))
    
    if oversized_files:
        print(f"The following files exceed {target_size_mb} MB:")
        for file_path, file_size_mb in oversized_files:
            print(f"{file_path} - {file_size_mb:.2f} MB")
    else:
        print(f"All files are below {target_size_mb} MB.")

if __name__ == "__main__":
    check_file_sizes()
