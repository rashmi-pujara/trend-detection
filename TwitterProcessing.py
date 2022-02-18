import re


def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)
    
    
class TwitterProcessing:
    """
    This class is used to pre-process tweets.  This centralises the processing to one location.  Feel free to add.
    """

    def __init__(self, tokeniser, lStopwords):
        """
        Initialise the tokeniser and set of stopwords to use.

        @param tokeniser:
        @param lStopwords:
        """

        self.tokeniser = tokeniser
        self.lStopwords = lStopwords

   


    def process(self, text):
        """
        Perform the processing.
        @param text: the text (tweet) to process

        @returns: list of (valid) tokens in text
        """

        text = text.lower()
        tokens = self.tokeniser.tokenize(text)
        tokensStripped = [tok.strip() for tok in tokens]

        # pattern for digits
        # the list comprehension in return statement essentially remove all strings of digits or fractions, e.g., 6.15
        regexDigit = re.compile("^\d+\s|\s\d+\s|\s\d+$")
        # regex pattern for http
        regexHttp = re.compile("^http")

        
 
        
        
        return [remove_emoji(tok) for tok in tokensStripped if tok not in self.lStopwords and regexDigit.match(tok) == None and regexHttp.match(tok) == None]