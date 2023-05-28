from modules.requestJsonSchema import analyzeJsonSchema, sentimentJsonSchema
from jsonschema import validate, exceptions
from modules.nlpProcessing import tokenization, part_of_speach, named_entity_recognition, sentiment_analyze
from flask import Flask, request, Response

app = Flask(__name__)
methods = {"tokenization": tokenization, "partOfSpeach": part_of_speach,
           "namedEntityRecognition": named_entity_recognition}


@app.route('/analyze', methods=['POST'])
def analyze():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        request_body = request.json
        try:
            validate(instance=request_body, schema=analyzeJsonSchema)
        except exceptions.ValidationError:
            return Response(response=" json not valid", status=400)
        try:
            data = methods[request_body["method"]](text=request_body["text"])
        except Exception as e:
            return Response(response=str(e), status=400)

        response_body = {"data": str(data)}
        return response_body
    else:
        return Response(response='Content-Type not supported!', status=400)


@app.route('/sentiment', methods=['POST'])
def sentiment():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        request_body = request.json
        try:
            validate(instance=request_body, schema=sentimentJsonSchema)
        except exceptions.ValidationError:
            return Response(response=" json not valid", status=400)
        try:
            data = sentiment_analyze(text=request_body["text"])
        except Exception as e:
            return Response(response=str(e), status=400)

        response_body = {"data": str(data)}
        return response_body
    else:
        return Response(response='Content-Type not supported!', status=400)


if __name__ == '__main__':
    app.run(debug=True)
