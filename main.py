import os
import csv

from OntologyProcessing import OntologyProcessing

# All the ontologies in 'datasets' that we want to process
ontologies = [f for f in os.listdir('datasets') if os.path.isfile(os.path.join('datasets', f))]
processed_ontologies = []
# the method we want to use for forgetting
# 1 - ALCHTBoxForgetter
# 2 - SHQTBoxForgetter
# 3 - ALCOntologyForgetter


with open('results.csv', 'w', newline='\n') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')
    filewriter.writerow(['Ontology Number', 'Ontology Name', 'Restrictions', '# Concepts forgotten', 'method'])

    for i, ontology in enumerate(ontologies):

        if ontology != 'signature.txt' and ontology != 'subClasses.nt' and ontology not in processed_ontologies:

            processed_ontologies.append(ontology)

            print('[INFO] Processing ontology: {}'.format(ontology))

            for method in range(1, 4):
                o = OntologyProcessing(ontology, method)

                restrictions = o.get_amount_of_restrictions()

                o.process_ontology()

                forgotten_items = o.amount_of_forgotten_items

                resultList = [i, ontology, restrictions, forgotten_items, method]
                filewriter.writerow(resultList)
