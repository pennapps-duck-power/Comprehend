import boto3
import json

# input text string
def lambda_handler(event, context):
    text = event['text'];

    comprehend = boto3.client(service_name='comprehend')

    response = comprehend.detect_sentiment(
        Text=text,
        LanguageCode='en'
    )

    if 'ResponseMetadata' in response:
        del response['ResponseMetadata']

    return json.dumps(response)
