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