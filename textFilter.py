with open("Books.txt", "r") as f:
    lines=f.readlines()

    docs=[[]]
    newText=True

    i=0
    j=0
    while i<len(lines):
        lines[i] = lines[i].rstrip('\n')
        if "_" in lines[i]:
            i += 3
            j += 1
            docs.append([])
        
        docs[j].append(lines[i])
        i += 1
    
    print(docs)
    i=0
    for doc in docs:

        title=doc[0].strip()
        title=title.replace(" ", "_")
        title=title.replace(",", "_")

        with open("stories/"+str(i)+"———"+title+".txt", "w+") as f:
            for line in doc:
                if line!="":
                    f.write(line+"\n")

        i += 1





