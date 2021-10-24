from Fuzzy.FuzzyString import FuzzyString
from Repository.DocumentParser import DocumentParser
from Repository.SpeechRecognition import SpeechRecognition


class Runner:
    def __init__(self, n):
        self.numberOfQuestions = n
        self.dataSetPath = './Repository/BusQuestionAnswer.xlsx'

    def test(self):
        documentParser = DocumentParser(self.dataSetPath, "B,C")
        df = documentParser.parse()
        L = [369,  789,  495,  886,  576,  934,   42,  526,
             8, 1038,  521, 724,  331, 1018,  394,  940,  370,
             60,  574,  893]
        df = df.loc[L]
        # df = df.sample(n=self.numberOfQuestions)
        answers = df['Answer'].tolist()
        questions = df['Question'].tolist()
        results = []
        for question in questions:
            index = questions.index(question)
            fuzzyAnswer = self.run(question)
            if fuzzyAnswer == answers[index]:
                results.append(True)
            else:
                results.append(False)

        accuracy = 100 * results.count(True) / 20

        return accuracy

    def run(self):
        speechRecognition = SpeechRecognition()
        text = speechRecognition.recognize()
        print('----------- QUESTION -----------')
        print(text)
        fuzzyString = FuzzyString()
        documentParser = DocumentParser(self.dataSetPath, "B,C")
        df = documentParser.parse()
        answers = df['Answer']
        questions = df['Question']

        fuzzyAnswers = []
        ratios = []
        for i in range(len(answers)):
            ratio = fuzzyString.getRatio(text, questions[i])
            ratios.append(ratio)
            fuzzyAnswers.append(answers[i])

        maxRatio = max(ratios)
        indexOfMax = ratios.index(maxRatio)
        if fuzzyString.getAbsoluteRatio(text, fuzzyAnswers[indexOfMax]) < 50:
            return False
        else:
            return fuzzyAnswers[indexOfMax]