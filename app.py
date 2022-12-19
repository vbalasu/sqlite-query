from chalice import Chalice, Response

app = Chalice(app_name='sqlite-query')

@app.route('/', cors=True)
def index():
    url = app.current_request.query_params['url']
    import requests, uuid, boto3
    response = requests.get(url)
    s3 = boto3.client('s3')
    s3.get_object(Bucket='cloudmatica', Key='db/empty.txt')  # Get an empty file, to set IAM policy for get_object
    key = f'1d/{str(uuid.uuid4())}'
    s3.put_object(Body=response.content, Bucket='cloudmatica', Key=key)
    return s3.generate_presigned_url('get_object', Params={'Bucket': 'cloudmatica', 'Key': key})


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
