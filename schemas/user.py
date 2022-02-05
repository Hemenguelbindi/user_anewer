def people_entity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "age": int(item["age"]),
        "join_date": item["join_date"],
        "job_title": item["job_title"],
        "company": item["company"],
        "gender": str(item["gender"]),
        "salary": item["salary"],
    }




