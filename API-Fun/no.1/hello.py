import twitter
api = twitter.Api()
api = twitter.Api(consumer_key='0sfVXX1Fa9rrn2PTixIrpg',
                  consumer_secret='t6ZudotmTOBKinXIaKYQJR62DJlg7bODJdC6644', 
                  access_token_key='19182576-nKNUvsiySnk9Gqnake8NeovZBKyu880Jx7ONCRo', 
                  access_token_secret='9FDMy49t7WS0QHihIjv2PCGXLNZU2kFmwrSUbk')

status = api.PostUpdate('bugga boo boo ')
