import os
import random

dataset_path = 'dataset'
class_instances = {}

def get_next_instance(class_name):
    if class_name not in class_instances:
        class_instances[class_name] = os.listdir(os.path.join(dataset_path, class_name))
        random.shuffle(class_instances[class_name])

    if class_instances[class_name]:
        return os.path.join(dataset_path, class_name, class_instances[class_name].pop())
    else:
        return None

# Example usage of the function
print(get_next_instance('tiger'))
print(get_next_instance('tiger'))
print(get_next_instance('leopard'))
print(get_next_instance('leopard'))
print(get_next_instance('tiger'))
print(get_next_instance('leopard'))
print(get_next_instance('tiger'))
print(get_next_instance('leopard'))
print(get_next_instance('tiger'))
print(get_next_instance('leopard'))
print(get_next_instance('tiger'))
print(get_next_instance('leopard'))
print(get_next_instance('tiger'))
print(get_next_instance('leopard'))
