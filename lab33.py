import os
import shutil
import random

def copy_with_random_names(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    for class_name in ['tiger', 'leopard']:
        class_path = os.path.join(source_dir, class_name)
        for filename in os.listdir(class_path):
            random_number = random.randint(0, 10000)
            new_filename = f"{str(random_number).zfill(5)}.jpg"
            source_file_path = os.path.join(class_path, filename)
            dest_file_path = os.path.join(dest_dir, new_filename)
            shutil.copy(source_file_path, dest_file_path)

source_dir = 'dataset'
dest_dir = 'random_dataset'
copy_with_random_names(source_dir, dest_dir)
print(f"Создана копия датасета в директории {dest_dir}.")
