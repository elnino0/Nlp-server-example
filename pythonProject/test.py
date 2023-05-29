import json
import pytest

def test_analyze_happyflow(app, client):
    quote = """
     Men like Schiaparelli watched the red planet—it is odd, by-the-bye, that
     for countless centuries Mars has been the star of war—but failed to
     interpret the fluctuating appearances of the markings they mapped so well.
     All that time the Martians must have been getting ready.
     During the opposition of 1894 a great light was seen on the illuminated
     part of the disk, first at the Lick Observatory, then by Perrotin of Nice,
     and then by other observers. English readers heard of it first in the
     issue of Nature dated August."""
    req_body = {"text": quote, "method": "namedEntityRecognition"}
    res = client.post('/analyze', data=json.dumps(req_body), headers={'Content-Type': 'application/json'})
    assert res.status_code == 200
    expected_entities = ['Schiaparelli', 'Nature', 'Perrotin', 'Mars', 'Lick Observatory']
    data = res.get_data(as_text=True)
    for en in expected_entities:
        assert en in data


def test_bad_Content_Type(app, client):
    quote = ""
    req_body = {"text": quote, "method": "namedEntityRecognition"}
    res = client.post('/analyze', data=json.dumps(req_body), headers={'Content-Type': 'application/text'})
    assert res.status_code == 400


def test_sentiment_happyflow(app, client):
    quote = """
     Men like Schiaparelli watched the red planet—it is odd, by-the-bye, that
     for countless centuries Mars has been the star of war—but failed to
     interpret the fluctuating appearances of the markings they mapped so well.
     All that time the Martians must have been getting ready.
     During the opposition of 1894 a great light was seen on the illuminated
     part of the disk, first at the Lick Observatory, then by Perrotin of Nice,
     and then by other observers. English readers heard of it first in the
     issue of Nature dated August."""
    req_body = {"text": quote}
    res = client.post('/sentiment', data=json.dumps(req_body), headers={'Content-Type': 'application/json'})
    assert res.status_code == 200

    expected_data = json.loads('{"data": {"neg": 0.055, "neu": 0.8, "pos": 0.145, "compound": 0.8419}}')
    assert expected_data == json.loads(res.get_data(as_text=True))


def test_sentiment_badchars(app, client):
    quote = "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
    req_body = {"text": quote}
    res = client.post('/sentiment', data=json.dumps(req_body), headers={'Content-Type': 'application/json'})
    assert res.status_code == 200

    expected_data = json.loads('{"data": {"neg": 0.0, "neu": 1.0, "pos": 0.0, "compound": 0.0}}')
    assert expected_data == json.loads(res.get_data(as_text=True))


def test_sentiment_badjson(app, client):
    quote = "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
    req_body = {"text": quote, "z": 1}
    res = client.post('/sentiment', data=json.dumps(req_body), headers={'Content-Type': 'application/json'})
    assert res.status_code == 400
