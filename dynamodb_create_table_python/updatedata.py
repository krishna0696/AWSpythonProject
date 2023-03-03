import boto3
from pprint import pprint
from decimal import Decimal


def update_movie(title, year, rating, plot, dynamodb=None):

    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('movies')

    respone = table.update_item(
        Key={
            'year':year,
            'title':title
        },
        UpdateExpression="set info.rating=:r, info.plot=:p",
        ExpressionAttributeValues = {
            ':r':Decimal(rating),
            ':p':plot
        },

        ReturnValues='UPDATED_NEW'
    )

    return respone


if __name__=="__main__":
    update_response = update_movie(
        "Thor: The Dark World", 2013, "8.5", "this is the new plot updated"
    )

    pprint(update_response)