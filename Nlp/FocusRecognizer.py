import stanza
import json


class FocusRecognizer:
    def __init__(self, text):
        self.text = text
        stanza.download('tr')

    def getParsedText(self):
        nlp = stanza.Pipeline('tr')
        stanzaResponse = nlp(self.text)
        data = stanzaResponse.sentences[0]
        decodedJson = json.loads(json.dumps(str(data.dependencies_string)))
        decodedJson = decodedJson.replace("<", "")
        decodedJson = decodedJson.replace("bound method Sentence.dependencies_string of ", "")
        decodedJson = decodedJson.replace(">", "")
        decodedJson = json.loads(decodedJson)
        return decodedJson

    def recognize(self):
        parsedText = self.getParsedText()
        focus = []
        for i in range(len(parsedText)):
            try:
                if parsedText[i]["deprel"] == "obl":
                    if(parsedText[i]['text'] != "UNK"):
                        focus.append(str(parsedText[i]["text"]))
                if parsedText[i]["deprel"] == "nsubj":
                    if (parsedText[i]['text'] != "UNK"):
                        focus.append(str(parsedText[i]["text"]))
                if parsedText[i]["deprel"] == "nmod":
                    if (parsedText[i]['text'] != "UNK"):
                        focus.append(str(parsedText[i]["text"]))
                if parsedText[i]["deprel"] == "nmod:poss":
                    if (parsedText[i]['text'] != "UNK"):
                        focus.append(str(parsedText[i]["text"]))

            except KeyError:
                print("there is a key erro in " + parsedText[i]["text"])

        return focus
