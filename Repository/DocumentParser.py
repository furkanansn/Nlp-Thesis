import pandas as pd


class DocumentParser:
    def __init__(self, documentName, cols):
        self.documentName = documentName
        self.cols = cols

    def parse(self):
        return pd.read_excel(self.documentName, usecols=self.cols)

    def getArray(self):
        df = self.parse()
        array = df.values.tolist()
        return array
