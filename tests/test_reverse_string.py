def test_reverse_string(app, client):
    res = client.get('/myservice?word=hello')
    assert res.status_code == 200
    expected = "olleh"
    assert expected == res.get_data(as_text=True)


def test_reverse_string_incorrect(app, client):
    res = client.get('/myservice?word=hello')
    assert res.status_code == 200
    expected = "hello"
    assert expected == res.get_data(as_text=True)
