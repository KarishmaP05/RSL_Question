def is_cyclic(s1,s2):
    if len(s1)!=len(s2):
        return False
    
    doubled_s1=s1+s1

    if s2 in doubled_s1:
        return True

s1="abcd"
s2="acbd"
if is_cyclic(s1,s2):
    print(f'"{s2}" is a cyclic permutation of "{s1}".')
else:
    print(f'"{s2}" is NOT a cyclic permutation of "{s1}".')
