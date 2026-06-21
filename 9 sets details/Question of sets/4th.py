# check if one set is subset and superset of another

set1={14,24,36,37,39,93,25,21,12,31,34}
set2={14,36,25,255}

if set1.issuperset(set2):
    print("Set1 is the superset of set2")
elif set1.issubset(set2):
    print("set1 is the subset of set2")
else:
    print("Both are different set")