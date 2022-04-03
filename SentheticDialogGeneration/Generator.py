from pyswip import Prolog
from Repository.DocumentParser import DocumentParser


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
        self.getUnits(answers)

    def getUnits(self, answers):
        s_list = []
        for answer in answers:
            query = self.prolog.query(f"generate_questions_units('{answer}',Q).")
            q_list = []
            for soln in query:
                q_list.append(soln["Q"].replace("n_", ""))
            q_list = set(q_list)
            s_list.append({
                "units": q_list
            })
        print(s_list)
