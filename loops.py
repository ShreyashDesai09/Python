list_of_cloud = ['AWS', 'AZURE']

print(list_of_cloud)

list_of_cloud.append('GCP')

print("Appended List:",list_of_cloud)

list_of_cloud.insert(1,'IBM')

print("Inserted List:",list_of_cloud)

print("Length:", len(list_of_cloud))

print("LOOP:-")
for cloud in list_of_cloud:
    print(cloud)

for i in range(1,11):
    print(i)