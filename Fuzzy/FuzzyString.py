from fuzzywuzzy import fuzz


class FuzzyString:


    def getRatio(self, firstString, secondString):
        tokenSortRatio = fuzz.token_sort_ratio(firstString, secondString)
        tokenSetRatio = fuzz.token_set_ratio(firstString, secondString)
        print('set ratio : ' + str(tokenSetRatio))

        print('sort ratio : ' + str(tokenSortRatio))
        return tokenSortRatio
        # I also removed these codes because before did it was %87 but now %99.62 :))
        #if tokenSetRatio > tokenSortRatio:
        #    return tokenSetRatio
        #else:
        #    return tokenSortRatio

    def getAbsoluteRatio(self, firstString, secondString):
        return fuzz.ratio(firstString, secondString)
