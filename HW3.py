dict={}
with open("file1.txt") as f:
    with open("file2.txt", "w") as f1:
        for line in f:
            #f1.write(line.rstrip())
            line=line.rstrip().split()
            if len(line)>0:
                for word in line:
                    if word not in dict:
                        dict[word]=1
                    else:
                        dict[word]=dict[word]+1
                line="".join(line)
                print(line)
total=0
counter=-1
for key,value in dict.items():
    print(key,":",value)
    total+=int(value)
    counter+=1