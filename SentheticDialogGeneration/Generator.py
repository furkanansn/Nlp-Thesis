from pyswip import Prolog
from Repository.DocumentParser import DocumentParser
from itertools import combinations


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
        #answers = df['Answer'].tolist()
        answers = ["adüye n_605 numaralı otobüs gitmektedir"]
        self.getUnits(answers)

    def getUnits(self, answers):
        s_list = []
        for answer in answers:
            query = self.prolog.query(f"generate_questions_units('{answer}',Q).")
            q_list = []
            for soln in query:
                for i in soln["Q"]:
                    s_list.append({
                        "units": i
                    })
        print(s_list)
        #self.getCombinations(s_list)

    def getCombinations(self,arr):
        temp = combinations(arr, len(arr))
        generatedQuestions = []
        for i in list(temp):
           generatedQuestions.append(self.generatedQuestions(arr))
        return generatedQuestions

    def generatedQuestions(self,arr):
        s_list = []
        for answer in arr:
            query = self.prolog.query(f"generate_questions('{answer}',Q).")
            q_list = []
            for soln in query:
                q_list.append(soln["Q"].replace("n_", ""))
            q_list = set(q_list)
            s_list.append({
                "units": q_list
            })
        return s_list

