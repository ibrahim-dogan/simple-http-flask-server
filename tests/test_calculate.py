def test_calculate(app, client):
    res = client.get('/calculate?a=10&b=2')
    assert res.status_code == 200
    expected = "12"
    assert expected == res.get_data(as_text=True)


def test_calculate_incorrect(app, client):
    res = client.get('/calculate?a=5&b=2')
    assert res.status_code == 200
    expected = "12"
    assert expected == res.get_data(as_text=True)
