from Fuzzy.FuzzyString import FuzzyString
from Nlp.DependencyParser import DependencyParser
from Repository.DocumentParser import DocumentParser
from Repository.SpeechRecognition import SpeechRecognition


class RunnerKeyword:
    def __init__(self):
        self.dataSetPath = './Repository/BusQuestionAnswer.xlsx'
        self.documentParser = DocumentParser(self.dataSetPath, "B,C,D")
        self.df = self.documentParser.parse()

    def test(self):
        answers = self.df['Answer'].tolist()
        questions = self.df['Question'].tolist()
        keywords = self.df['keywords'].tolist()
        results = []
        for question in questions:
            index = questions.index(question)
            answer = self.getAnswer(question)
            if answer == answers[index]:
                results.append(True)
            else:
                results.append(False)
            self.reporter(index, question, answer, answers[index],results[index])
        accuracy = 100 * results.count(True) / len(questions)

        return accuracy,len(questions)

    def run(self):
        #speechRecognition = SpeechRecognition()
        #text = speechRecognition.recognize()
        text = input("enter \n")
        print('----------- QUESTION -----------')

        return self.getAnswer(text)



    def getAnswer(self,text):
        dependencyParser = DependencyParser()
        lemmas = dependencyParser.getLemmas(text)

        for i in range(len(self.df['keywords'])):

            for j in range(len(lemmas)):
                count = 0
                if lemmas[j] in self.df['keywords'][i]:

                    for k in range(len(lemmas)):
                        if lemmas[k] in self.df['keywords'][i]:
                            count = count + 1

                    if (len(lemmas) - count) == 0:
                        print("Founded Keywords: " + " ".join(lemmas) + '\n' + 'dataset keywords: ' + self.df['keywords'][i])
                        return self.df['Answer'][i]
        else:
            return 'Sorunun cevabını bilmiyorum ama senin için araştırıcam'



    #@ DO NOT RUN IF DATASET WAS NOT UPDATED
    def generateKeywords(self):
        dependencyParser = DependencyParser()
        allLemmas = []
        for i in range(len(self.df['Question'])):
            lemmas = dependencyParser.getLemmas(self.df['Question'][i])
            print(str(i) + ' .sıra' + ' ' + ' '.join(lemmas))
            allLemmas.append(' '.join(lemmas))

        self.df['keywords'] = allLemmas
        self.df.to_excel(self.dataSetPath)



    def reporter(self,index,question,fuzzyAnswer,answer,isCorrect):
        print('--------------------------------' + str(index) + '--------------------------------')
        print('Is correct :' + str(isCorrect) +'\n' +'question: ' + question + '\n' + 'our answer: ' + str(fuzzyAnswer) + '\n' + 'answer: ' + answer)
        print('---------------------------------------------------------------------')