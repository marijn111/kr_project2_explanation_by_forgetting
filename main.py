import os
import csv

from OntologyProcessing import OntologyProcessing

# All the ontologies in 'datasets' that we want to process
ontologies = [f for f in os.listdir('datasets') if os.path.isfile(os.path.join('datasets', f))]

# the method we want to use for forgetting
# 1 - ALCHTBoxForgetter
# 2 - SHQTBoxForgetter
# 3 - ALCOntologyForgetter


with open('results.csv', 'w', newline='\n') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')
    filewriter.writerow(['Ontology Number', 'Ontology Name', 'Restrictions', '# Concepts forgotten', 'method'])

    for i, ontology in enumerate(ontologies):

        for method in range(1, 4):
            o = OntologyProcessing(ontology, method)

            restrictions = o.get_amount_of_restrictions()

            o.process_ontology()

            forgotten_items = o.amount_of_forgotten_items

            resultList = [i, ontology, restrictions, forgotten_items, method]
            filewriter.writerow(resultList)



# # Creates a csv file used for data analysis
# with open("results.csv", 'w', newline='\n') as csvfile:
#     filewriter = csv.writer(csvfile, delimiter=";")
#     filewriter.writerow(['Sudoku number', "Strategy",
#                          "Execution time", "Splits",
#                          "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9",
#                          "R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9",
#                          "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"])
#     # iterate over all the sudoku's in the sudoku file
#     # 17445 is the number of lines in the subig20 sudoku list
#     for sudokuNumber in range(17445):
#         # iterate over the available strategies
#         for strategy in range(1, 4):
#             print('\n[INFO] Sudoku number: \t\t{}'.format(sudokuNumber))
#             print('[INFO] Strategy: \t\t{}'.format(strategy))
#
#             # create and solve the sudocu
#             sObj = Sudoku()
#             sObj.parseFromDotsfile(rules_File, dots_File, sudokuNumber)
#             sObj.strategy = strategy
#             sObj.solve()
#
#             # Gather the results
#             resultList = [sudokuNumber, sObj.strategy,
#                           round(sObj.executionTime, 3), sObj.splits]
#             resultList += sObj.amountNumbersPerBox + \
#                 sObj.amountNumbersPerRow + sObj.amountNumbersPerColumn
#
#             # Write the results to a csv file
#             filewriter.writerow(resultList)