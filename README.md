# nrich_exe
a task by Nrich

to deploy use docker compose 
1. docker compose build
2. docker compose pull
3. docker compose up


curl example :
1. curl -H 'Content-Type: application/json' -d '{"text":"some text", "method": "namedEntityRecognition"}' -X POST  http://127.0.0.1:3000/analyze # note method options tokenization, partOfSpeach and namedEntityRecognition
2. 1. curl -H 'Content-Type: application/json' -d '{"text":"some text"}' -X POST  http://127.0.0.1:5000/sentiment  # note sentiment endpoint  is not on cach 
