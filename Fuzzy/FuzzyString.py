from fuzzywuzzy import fuzz


class FuzzyString:


    def getRatio(self, firstString, secondString):
        tokenSortRatio = fuzz.token_sort_ratio(firstString, secondString)
        tokenSetRatio = fuzz.token_set_ratio(firstString, secondString)
        if tokenSetRatio > tokenSortRatio:
            return tokenSetRatio
        else:
            return tokenSortRatio

    def getAbsoluteRatio(self, firstString, secondString):
        return fuzz.ratio(firstString, secondString)
