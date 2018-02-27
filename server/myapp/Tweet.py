class Tweet:
    text = ""
    sender = "inconnu"
    dateTweet = ""
    nbLike = 0
    nbRT = 0
"""
    consumer_key = 'd9UUsBFWzdBrMv8HwEay8mzeP'
	consumer_secret = 'YhheggCydfUm3VwHiT14ig1lM0ahLAIaFbtBfq71JgWp6dHA5B'
	access_token = '960451934535774208-g3s0XuB7efDic5lQBK8RNfSa4GL5GKB'
	access_token_secret = 'XW05i2CvXt2Th9ipoY8wU4ICk39mVhSI051DPj7ad8gej'
"""
    def __init__(self, text, sender, date, nbL, nbRT):
        self.text = text
        self.sender = sender
        self.dateTweet = date 
        self.nbLike = nbL
        self.nbRT = nbRT


    def getText(self):
        return self.text

    def getSender(self):
        return self.sender

    def getDateTweet(self);
        return self.dateTweet

    def getnbLike(self):
        return self.nbLike

    def getnbRT(self):
        return self.nbRT

    def setText(self,text):
         self.text = text

    def setSender(self,sender):
         self.sender = sender

    def setDateTweet(self,date);
         self.dateTweet = date

    def setnbLike(self,nbL):
         self.nbLike = nbL

    def setnbRT(self,nbRT):
         self.nbRT = nbRT

    
    def displayTweet(self)
        print(self.sender,"\n")
         print(self.text,"\n")
          print(self.dateTweet,"\n")


    


