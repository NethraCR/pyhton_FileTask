import csv
with open('Images.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# #Example 2: Write to a CSV file
# import csv
# with open('Images.csv', 'w') as file:
#     Image = csv.writer(file)
#     Image.writerow(["Name", "Size", "img_res","no_of_obg","obj_res"])
#     Image.writerow(["cat", "200MP", "30PX","6","230"])
#     Image.writerow(["Dog", "654MP", "78PX","3","130"])



