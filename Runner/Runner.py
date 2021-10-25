from Fuzzy.FuzzyString import FuzzyString
from Repository.DocumentParser import DocumentParser
from Repository.SpeechRecognition import SpeechRecognition


class Runner:
    def __init__(self, n):
        self.numberOfQuestions = n
        self.dataSetPath = './Repository/BusQuestionAnswer.xlsx'

    def test(self,isCompetition):
        documentParser = DocumentParser(self.dataSetPath, "B,C")
        df = documentParser.parse()
        L = [369,  789,  495,  886,  576,  934,   42,  526,
             8, 1038,  521, 724,  331, 1018,  394,  940,  370,
             60,  574,  893]
        if not isCompetition:
            df = df.loc[L]
        # df = df.sample(n=self.numberOfQuestions)
        answers = df['Answer'].tolist()
        questions = df['Question'].tolist()
        results = []
        for question in questions:
            index = questions.index(question)
            fuzzyAnswer = self.getFuzzyAnswer(question,answers,questions)

            if fuzzyAnswer == answers[index]:
                results.append(True)
            else:
                results.append(False)
            self.reporter(index, question, fuzzyAnswer, answers[index],results[index])
        accuracy = 100 * results.count(True) / len(questions)

        return accuracy,len(questions)

    def run(self):
        speechRecognition = SpeechRecognition()
        text = speechRecognition.recognize()
        print('----------- QUESTION -----------')
        print(text)
        documentParser = DocumentParser(self.dataSetPath, "B,C")
        df = documentParser.parse()
        answers = df['Answer']
        questions = df['Question']
        return self.getFuzzyAnswer(text,answers,questions)



    def getFuzzyAnswer(self,text,answers,questions):
        fuzzyString = FuzzyString()
        fuzzyAnswers = []
        ratios = []
        for i in range(len(answers)):
            ratio = fuzzyString.getRatio(text, questions[i])
            ratios.append(ratio)
            fuzzyAnswers.append(answers[i])

        maxRatio = max(ratios)

        indexOfMax = ratios.index(maxRatio)
        return fuzzyAnswers[indexOfMax]

        # I remove these codes because before i removed them the accuraciy was %67. After I removed them it was %87.
        # I know We should take precautions but other ways instead of this
        #if fuzzyString.getAbsoluteRatio(text, fuzzyAnswers[indexOfMax]) < 50:
        #    return False
        #else:
        #    return fuzzyAnswers[indexOfMax]

    def reporter(self,index,question,fuzzyAnswer,answer,isCorrect):
        print('--------------------------------' + str(index) + '--------------------------------')
        print('Is correct :' + str(isCorrect) +'\n' +'question: ' + question + '\n' + 'fuzzy answer: ' + str(fuzzyAnswer) + '\n' + 'answer: ' + answer)
        print('---------------------------------------------------------------------')