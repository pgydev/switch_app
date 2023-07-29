def test_success(client):
    response = client.post("/process", json={
        'string': "ASDdd"
    })
    assert response.json['string'] == "asdDD"
    
def test_fail(client):
    response = client.post("/process", json={
        'string': "123"
    })
    assert response.json['error'] == "Please use letters and words"
    
def test_int_fail(client):
    response = client.post("/process", json={
        'string': 123
    })
    assert response.json['error'] == "Please use letters and words"