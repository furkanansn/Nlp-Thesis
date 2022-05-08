from pyswip import Prolog
from Repository.DocumentParser import DocumentParser
from itertools import combinations, permutations


class Generator:
    def __init__(self):
        self.dataSetPath = './Repository/BusQuestionAnswer.xlsx'
        self.prolog = Prolog()

    def consult(self):
        self.prolog.consult("prolog-files/nominal_finder.pl")
        self.getQuestions()

    def getQuestions(self):
        documentParser = DocumentParser(self.dataSetPath, "B,C")
        df = documentParser.parse()
        answers = df['Answer'].tolist()
        # answers = ["adüden foruma n_605 numaralı otobüs gitmektedir"]
        self.getUnits(answers)

    def getUnits(self, answers):
        s_list = []
        for answer in answers:
            query = self.prolog.query(f"generate_questions_units('{answer}',Q).")
            q_list = []
            for soln in query:
                for i in soln["Q"]:
                    s_list.append(i)
        self.getCombinations(s_list)

    def getCombinations(self,arr):
        temp = permutations(arr, len(arr))
        generatedQuestions = []
        for i in list(temp):
           generatedQuestions.append(self.generatedQuestions(list(i)))
        return generatedQuestions
    # generate_questions('[['adüye'], ['n_605', 'numaralı', 'otobüs'], ['gitmektedir']]',Q).
    # generate_questions([['adüye'], ['n_605', 'numaralı', 'otobüs'], ['gitmektedir']], Q).

    def generatedQuestions(self,arr):
        s_list = []
        query = self.prolog.query(f"generate_questions({arr},Q).")
        q_list = []
        for soln in query:
            q_list.append(soln["Q"])
        s_list.append(q_list)
        print("question number", len(set(q_list)))
        # print(set(q_list))
        # for answer in arr:
        #     print('answer')
        #     print(answer)
        #     query = self.prolog.query(f"generate_questions('{answer}',Q).")
        #     q_list = []
        #     print('query')
        #     print(query)
        #     for soln in query:
        #         print('soln')
        #         print(soln)
        #         q_list.append(soln["Q"])
        #     s_list.append({
        #         "units": q_list
        #     })
        return s_list