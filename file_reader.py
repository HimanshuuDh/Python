#step 1 create the file object
names_file=open('name.txt','r')

#step 2 is process the file
#file_content= names_file.read()
#print(file_content)

#step 2 process the file
line=names_file.readline()
while line != '':
    print(line)
    line=names_file.readline()


#Step 3 close the file
names_file.close()