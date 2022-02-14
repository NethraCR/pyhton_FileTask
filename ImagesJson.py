import json
# var = {
#        "Image_Detailes": {
#                    "file_size":"400MB",
#                    "img_res":"300px",
#                    "img_name":"Cat",
#                     "no_of_obg":"5",
#                      "obj_res":"240px"
#                        }
#        }
# with open("Image.json", "w") as p:
#    json.dump(var, p)
#  #
# f = open('Image.json')
# # # returns JSON object as a dictionary
# data = json.load(f)
#
# # Iterating through the json
# # # # list
# for i in data['Image_Detailes']:
#    print(i)
# #
# # # Closing file
# f.close()

import json
# function to add to JSON
def write_json(new_data, filename='Image.json'):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["Image_Detailes"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=7, sort_keys=True)

# python object to be appended
y = {
      "file_size" : "400MB",
      "img_res" : "300px",
      "img_name": "Lion",
      "no_of_obg": "6",
      "obj_res": "670px"
      }

write_json(y)