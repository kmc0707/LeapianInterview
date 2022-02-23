class Word:
    def __init__(self, pageId, wordId, wordIdOnPage, wordX, wordY, wordWidth, wordHeight, wordText) -> None:
        self.pageId = pageId
        self.wordId = wordId 
        self.wordIdOnPage = wordIdOnPage
        self.wordX = wordX
        self.wordY = wordY
        self.wordWidth= wordWidth
        self.wordHeight = wordHeight
        self.wordText = wordText

    def __repr__(self):
        d = "pageId: {}\n".format(self.pageId)
        d += "   wordId: {}\n".format(self.wordId)
        d += "   wordIdOnPage: {}\n".format(self.wordIdOnPage)
        d += "   wordX: {}\n".format(self.wordX)
        d += "   wordY: {}\n".format(self.wordY)
        d += "   wordWidth: {}\n".format(self.wordWidth)
        d += "   wordHeight: {}\n".format(self.wordHeight)
        d += "   wordText: {}".format(self.wordText)
        return d