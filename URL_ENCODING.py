

def url_encode(s):
    sym_dict={' ':'%20', '!':'%21','#':'%23','$':'%24'}
    new_URL=''
    for i in s:
        if i in sym_dict:
            value=sym_dict.get(i)
            new_URL+=value
        else:
            new_URL+=i
            
    print(new_URL)
            
url_encode("#Raja Software$ Labs@")