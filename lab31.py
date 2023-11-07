import os
import csv

def create_annotation_file(root_dir, output_file):
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Абсолютный путь', 'Относительный путь', 'Метка класса'])

        for class_name in ['tiger', 'leopard']:
            class_path = os.path.join(root_dir, class_name)
            for filename in os.listdir(class_path):
                absolute_path = os.path.join(class_path, filename)
                relative_path = os.path.relpath(absolute_path, start=root_dir)
                writer.writerow([absolute_path, relative_path, class_name])

root_dir = 'dataset'
output_file = 'annotations.csv'
create_annotation_file(root_dir, output_file)
print(f"Файл аннотации {output_file} успешно создан.")
