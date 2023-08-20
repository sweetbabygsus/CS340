#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the CRUD module
from AnimalShelter import CrudAnimalShelter

#create instance with authentication
USER = 'aacuser'
PASS = 'Pokemon845!'
crud = CrudAnimalShelter(USER, PASS)

# Sample animal data
sample_animal = [
    {
        "name":"bess",
        "type":"dog"
    },
    {
        "name":"moneypenny",
        "type":"cat"
    },
    {
        "name":"jack",
        "type":"dog"
    }
]
# loop through sample data and insert into databse using create method class
for i in sample_animal:
    crud.create(i)
    
# get all dogs from databaase by using read method
dogs = crud.read( {"type":"dog"} )
for dog in dogs:
    print(dog)

# update an existing dog with the name "bess"
update_lookup = {"name": "bess"}
update_data = {"age": 6}
num_modified = crud.update(update_lookup, update_data)
print(f"Number of dogs modified: {num_modified}")

# Get all dogs from the database after update
updated_dogs = crud.read({"type": "dog"})
print("Dogs in the database after update:")
for dog in updated_dogs:
    print(dog)
    
# delete a dog from the database "jack"
delete_lookup = {"name": "jack"}
num_removed = crud.delete(delete_lookup)
print(f"Number of dogs removed: {num_removed}")

# Get all dogs from database again after delete method
remaining_dogs = crud.read({"type": "dog"})
print("Remaining dogs in the database:")
for dog in remaining_dogs:
    print(dog)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




