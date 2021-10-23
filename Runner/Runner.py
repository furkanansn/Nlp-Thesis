from Fuzzy.FuzzyString import FuzzyString
from Repository.DocumentParser import DocumentParser
from Repository.SpeechRecognition import SpeechRecognition


class Runner:
    @staticmethod
    def test(text):
        dataSetPath = '/Users/admin/Documents/University/Thesis/Project/Repository/BusQuestionAnswer.xlsx'
        fuzzyString = FuzzyString()
        documentParser = DocumentParser(dataSetPath, "B,C")
        df = documentParser.parse()
        answers = df['Answer']
        fuzzyAnswers = []
        ratios = []
        for i in range(len(answers)):
            ratio = fuzzyString.getRatio(text, answers[i])
            ratios.append(ratio)
            fuzzyAnswers.append(answers[i])

        maxRatio = max(ratios)
        indexOfMax = ratios.index(maxRatio)
        if fuzzyString.getAbsoluteRatio(text, fuzzyAnswers[indexOfMax]) < 50:
            return "Şuanda bu soruya cevap verememekteyim. Başka bir sorunuz var mıydı?"
        else:
            return fuzzyAnswers[
                indexOfMax]


    @staticmethod
    def run():
        dataSetPath = '/Users/admin/Documents/University/Thesis/Project/Repository/BusQuestionAnswer.xlsx'
        # speechRecognition = SpeechRecognition()
        # text = speechRecognition.recognize()
        fuzzyString = FuzzyString()
        documentParser = DocumentParser(dataSetPath, "B,C")
        df = documentParser.parse()
        answers = df['Answer']

        text = input("Lütfen soru yazınız\n")
        # focusRecognizer = FocusRecognizer(text)
        # focus = focusRecognizer.recognize()
        # focusString = ' '.join(focus)
        # print('Focus and non freezes: ' + focusString)

        fuzzyAnswers = []
        ratios = []
        for i in range(len(answers)):
            ratio = fuzzyString.getRatio(text, answers[i])
            ratios.append(ratio)
            fuzzyAnswers.append(answers[i])

        maxRatio = max(ratios)
        indexOfMax = ratios.index(maxRatio)
        if fuzzyString.getAbsoluteRatio(text, fuzzyAnswers[indexOfMax]) < 50:
            print("Şuanda bu soruya cevap verememekteyim. Başka bir sorunuz var mıydı?")
        else:
            print('Ratio between question and answer is: ' + '%' + str(maxRatio) + ',\nAnswer is: ' + fuzzyAnswers[
                indexOfMax])
