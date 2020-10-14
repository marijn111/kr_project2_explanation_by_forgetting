import os
import time

"""
This is the class responsible for processing the ontology and calculating all the things
"""


class OntologyProcessing:

    def __init__(self, ontology, method):
        self.forgetOntology = 'datasets/' + ontology
        self.signature = ''
        self.method = method
        self.satisfiable = 0
        self.loop_count = 0
        self.amount_of_restrictions = 0
        self.amount_of_forgotten_items = 0
        self.classes = []

    def get_amount_of_restrictions(self):
        f = open(self.forgetOntology)

        for line in f:
            if '<owl:Restriction>' in line:
                self.amount_of_restrictions += 1

    def format_uri(self, axiom):
        axiom = axiom.strip(' \n<>/')
        axiom = axiom.split()[1]
        uri = axiom.split('=')[1]
        uri = uri.strip('"')
        return uri

    def process_ontology(self):

        while self.satisfiable:

            print('[INFO] generating subclasses...')
            # generate new subclasses.nt file
            os.system('java -jar kr_functions.jar ' + 'saveAllSubClasses' + " " + self.forgetOntology)

            time.sleep(5)

            f = open('datasets/subClasses.nt')

            for line in f:
                line = line.split()
                subclass = line[0].strip('<>')
                object_property = line[1].strip('<>')
                class_name = line[2].strip('<>')

                if 'Nothing' not in class_name and class_name not in self.classes:
                    self.classes.append(class_name)

            f.close()

            if not len(self.classes):
                break

            print(self.classes)

            fout = open('datasets/signature.txt', 'w')

            for k in self.classes:
                fout.write(k)
                fout.write('\n')

            fout.close()

            time.sleep(5)

            # Start forgetting stuff

            print('[INFO] Starting with Forgetting...')
            os.system(
                'java -cp lethe-standalone.jar uk.ac.man.cs.lethe.internal.application.ForgettingConsoleApplication --owlFile ' + self.forgetOntology + ' --method ' + self.method + ' --signature ' + self.signature)

            time.sleep(5)

            self.forgetOntology = './result.owl'

            result_file = open('result.owl')

            general_axiom_section = 0
            axioms = []

            for line in result_file:

                if 'General axioms' in line:
                    general_axiom_section = 1
                    continue

                if general_axiom_section:
                    if '<rdfs:subClassOf ' in line:
                        if line not in axioms:
                            axioms.append(line)

            f.close()

            print(axioms)

            if len(axioms) == 1 and 'Nothing' in axioms[0].strip():
                self.satisfiable = 0
                print('[INFO] Unsatisfiable. Terminating.')
                self.amount_of_forgotten_items = len(self.classes)
                break

            else:
                for axiom in axioms:
                    self.classes.append(self.format_uri(axiom))

            self.loop_count += 1
            print('[INFO] Current loop count: ' + str(self.loop_count))

        print('[INFO] Amount of restrictions: {}'.format(self.amount_of_restrictions))
        print('[INFO] Amount of forgotten items: {}'.format(self.amount_of_forgotten_items))








#
# forgetOntology = 'datasets/pizza_super_simple.owl'
# signature = 'datasets/signature.txt'
# method = '2'
# satisfiable = 1
#
# loop_count = 0
#
# amount_of_restrictions = 0
# amount_of_forgotten_items = 0
# classes = []
#
#
# added_axioms = 1
#
# ontology = open('datasets/pizza_super_simple.owl')
#
# # Gather the amount of restrictions
# for line in ontology:
#     if '<owl:Restriction>' in line:
#         amount_of_restrictions += 1






