from pyswip import Prolog


class PrologNLP:
    def __init__(self):
        self.prolog = Prolog()
        self.prolog.consult("morphophonology_analyzer.pl")

    def analyzer(self, word):
        query = self.prolog.query(f"analyze({word},L).")

        for soln in query:
            return str(soln["L"][0])