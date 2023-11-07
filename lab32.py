import os
import shutil
import csv

def copy_and_rename_dataset(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    with open('annotations_modified.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Абсолютный путь', 'Относительный путь', 'Метка класса'])

        for class_name in ['tiger', 'leopard']:
            class_path = os.path.join(source_dir, class_name)
            new_class_name = f"{class_name}_"
            for i, filename in enumerate(sorted(os.listdir(class_path))):
                image_path = os.path.join(class_path, filename)
                new_filename = f"{class_name}_{str(i).zfill(4)}.jpg"
                new_image_path = os.path.join(dest_dir, new_filename)
                shutil.copy(image_path, new_image_path)
                relative_path = os.path.relpath(new_image_path, start=dest_dir)
                writer.writerow([new_image_path, relative_path, class_name])

source_dir = 'dataset'
dest_dir = 'modified_dataset'
copy_and_rename_dataset(source_dir, dest_dir)
print(f"Датасет успешно скопирован и переименован в директорию {dest_dir}.")
