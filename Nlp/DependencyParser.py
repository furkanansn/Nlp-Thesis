import stanza
import json


class DependencyParser:
    def __init__(self):
        stanza.download('tr')

    def getParsedText(self,text):
        nlp = stanza.Pipeline('tr')
        stanzaResponse = nlp(text)
        data = stanzaResponse.sentences[0]
        decodedJson = json.loads(json.dumps(str(data.dependencies_string)))
        decodedJson = decodedJson.replace("<", "")
        decodedJson = decodedJson.replace("bound method Sentence.dependencies_string of ", "")
        decodedJson = decodedJson.replace(">", "")
        decodedJson = json.loads(decodedJson)
        return decodedJson

    def getLemmas(self,text):
        parsedText = self.getParsedText(text)
        lemmas = []
        for i in range(len(parsedText)):
            try:
                if(parsedText[i]['lemma'].lower() != 'unk' and parsedText[i]['lemma'].lower() != 'li'
                and parsedText[i]['lemma'].lower() != 'i' and parsedText[i]['lemma'].lower() != '?'):
                   lemmas.append(parsedText[i]['lemma'].lower())

            except KeyError:
                print("")

        return lemmas