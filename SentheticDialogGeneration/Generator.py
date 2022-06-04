from pyswip import Prolog
from Repository.DocumentParser import DocumentParser
from itertools import combinations, permutations


class Generator:
    def __init__(self):
        self.dataSetPath = './Repository/BusQuestionAnswer.xlsx'
        self.prolog = Prolog()
        self.questions = set()
        self.unit_number = None

    def consult(self):
        self.prolog.consult("prolog-files/nominal_finder.pl")
        self.getQuestions()

    def getQuestions(self):
        documentParser = DocumentParser(self.dataSetPath, "B,C")
        df = documentParser.parse()
        # answers = df['Answer'].tolist()
        answers = ["adüye n_605 numaralı otobüs gitmektedir"]
        self.getUnits(answers)
        print("\n".join(list(self.questions)))
        print(len(self.questions))

    def getUnits(self, answers):
        s_list = []
        for answer in answers:
            query = self.prolog.query(f"generate_questions_units('{answer}',Q).")
            q_list = []
            for soln in query:
                for i in soln["Q"]:
                    s_list.append(i)
            if self.unit_number is None:
                self.unit_number = len(s_list)
            elif self.unit_number is not len(s_list):
                continue
            self.getCombinations(s_list)

    def getCombinations(self,arr):
        temp = permutations(arr, len(arr))
        generatedQuestions = []
        for i in list(temp):
           generatedQuestions.append(self.generatedQuestions(list(i)))
        return generatedQuestions
    # generate_questions('[['adüye'], ['n_605', 'numaralı', 'otobüs'], ['gitmektedir']]',Q).
    # generate_questions([['adüye'], ['n_605', 'numaralı', 'otobüs'], ['gitmektedir']], Q).

    def isListEmpty(self, inList):
        if isinstance(inList, list):  # Is a list
            return all(map(self.isListEmpty, inList))
        return False

    def generatedQuestions(self,arr):
        s_list = []
        query = self.prolog.query(f"generate_questions({arr},Q).")
        q_list = []
        for soln in query:
            q_list.append(soln["Q"])


        for q in q_list:
            x = None
            arr_sent = q.split()
            if len(arr_sent) > 0:
                isQ = arr_sent[0] + ' ' + arr_sent[1]
                q_start = self.prolog.query(f"find_Q1(X, '{isQ}').")
                for soln in q_start:
                    if soln["X"] is not None:
                        x = soln["X"]
            if x is not None:
                continue
            clean_string = " ".join(q.split())
            self.questions.add(clean_string)
            self.getUnits([clean_string])
        s_list.append(q_list)
        return s_list