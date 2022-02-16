def test_finde_one_by_from_name(test_app):
    test_data = {
  "id": "61fbbf4ed31a1822ae9e1d6f",
  "name": "Flynn Vang",
  "email": "turpis.non@Nunc.edu",
  "age": 69,
  "join_date": "2003-12-28T18:18:10-08:00",
  "job_title": "janitor",
  "company": "Twitter",
  "gender": "female",
  "salary": 9632
}
    respouns = test_app.get("/name_one_first/Flynn Vang")
    assert respouns.status_code == 200
    assert respouns.json() == test_data