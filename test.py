import os

ontologies = [f for f in os.listdir('datasets') if os.path.isfile(os.path.join('datasets', f))]

print(ontologies)