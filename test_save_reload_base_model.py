#!/usr/bin/python3
from models.base_model import BaseModel
from models import storage


all_objs = storage.all()
obj_len = len(all_objs)
if len(all_objs) == 0:
    print("{} object(s) have been created".format(len(all_objs)))
else:
    print("{} objects reloaded".format(obj_len))
    print("--------Reloaded objects-------------")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

print("--------Creating a new object---------")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)
