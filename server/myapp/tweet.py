'''
	Some attributes (like tb) come from the connect.py file.
	We've decided to write all our code class-oriented, that's why I've decided to create a connect class
'''

#Made from the code Alexandre sent me yesterday + a new attribute for location
class Tweet:
    text = ""
    author = ""
    dateTweet = ""
    nbLike = 0
    nbRT = 0
	location = []
	positivity = 0
	polarity = 0
	
	#Constructor
	def __init__(self, text, sender, date, nbL, nbRT, loc, pos, pol):
        self.text = text
        self.author = sender
        self.dateTweet = date 
        self.nbLike = nbL
        self.nbRT = nbRT
		self.location=loc
		self.positivity=pos
		self.polarity=pol
	#Getters
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
	
	def getPositivity(self):
		return self.positivity
		
	def getPolarity(self) :
		return self.polarity

	#Translate from Python to Json
    def getAuthorJson(self):
		decodedfile = json.dumps((self.author)._json)
		decodedfile = json.loads(decodedfile)
        return str(decodedfile['screen_name'])
	''' 
	As I can't test it for the moment, here is what we did on the first version of the code :
		for tweet in tweepy.Cursor(api.search, q="#jeuxolympiques2018",count=25,
			lang="fr", since="2018-02-019").items():
			#print(tweet.created_at, tweet.text) #print the global twitter
			#print(tb(tweet.text).sentiment) #print a number who juge the positiveness
			print(tweet.created_at) #print the date of the tweet
			
		def username(tweet) :
			file = tweet.author._json
			decodedfile = json.dumps(file)
			decodedfile = json.loads(decodedfile)
			return str(decodedfile['screen_name'])
	'''	

    def getDateTweetJson(self);
		return dumps(self.Date, default=json_serial)

    def getnbLikeJson(self):
        return self.nbLike

    def getnbRTJson(self):
        return self.nbRT
	
	#Waiting for the getLoc that will be done by Julien
	def getLocJson(self) :
		return self.nbRT
		
	def getTextJson(self):
        return self.text
		
	def getPolarityJson(self):
		file = tweet.author._json
		decodedfile = json.dumps(file)
		decodedfile = json.loads(decodedfile)
		return connect.tb(tweet.text).sentiment[0]
		
	def getPositivityJson(self):
		
	
	#Done by Julien
	def getLocJson(self) :
		return self.nbRT
	
	#Setters
    def setText(self,text):
         self.text = text

    def setAuthor(self,author):
        self.author = tweet.author

    def setDateTweet(self,date);
         self.dateTweet = date

    def setnbLike(self,nbL):
         self.nbLike = nbL

    def setnbRT(self,nbRT):
         self.nbRT = nbRT
		 
	def setPositivity(self,positivity):
		self.positivity=positivity
	
	def setPolarity(self,polarity):
		self.polarity=polarity