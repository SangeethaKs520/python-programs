def binar_search(data):
 li=['a','e','i','o','u']
 binarydata=""
 for dat in data:
        if dat in li:
            dat='0'
            binarydata=binarydata+dat
        else:
            dat='1'
            binarydata=binarydata+dat

 print(binarydata)
    
binar_search("heraku")

