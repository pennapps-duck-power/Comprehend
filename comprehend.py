import boto3
import json

# input text string
def comprehendText(text):

	comprehend = boto3.client(service_name='comprehend')
	                
	response = comprehend.detect_sentiment(
	    Text=text,
	    LanguageCode='en'
	)

	if 'ResponseMetadata' in response:
		del response['ResponseMetadata']

	return json.dumps(response)

#	{'Sentiment': 'POSITIVE', 
#    'SentimentScore': {
#  		'Positive': 0.9192718863487244, 
#  		'Negative': 0.001119148568250239, 
#  		'Neutral': 0.07677706331014633, 
#  		'Mixed': 0.00283180084079504}}
