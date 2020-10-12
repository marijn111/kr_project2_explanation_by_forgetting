import collections


"""
This currently just reads all the classes from the ontology and writes them all to the signature.txt file in the correct format. 
"""


f = open('datasets/pizza_super_simple.owl')

amount_of_restrictions = 0
classes = collections.defaultdict(int)


for line in f:
    if '<owl:Restriction>' in line:
        amount_of_restrictions += 1

    elif '<owl:Class rdf:about' in line or '<rdf:Description rdf:about' in line:

        # preprocess the line a bit, so that it is only the valid URI
        line = line.split()
        owl_class = line[1]
        owl_class = owl_class.split('=')[1]
        owl_class = owl_class.replace('/>', '')
        owl_class = owl_class.replace('"', '')
        owl_class = owl_class.replace('>', '')

        classes[owl_class] += 1


f.close()

print(amount_of_restrictions)
print(classes)

fout = open('datasets/signature.txt', 'w')

for k in classes:
    fout.write(k)
    fout.write('\n')

fout.close()
