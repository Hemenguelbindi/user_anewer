def user_entity(item) -> dict:
    return {
        "name": str(item["name"]),
        "email": str(item["email"]),
        "age": int(item["age"]),
        "join_date": str(item["join_date"]),
        "job_title": str(item["job_title"]),
        "company": str(item["company"]),
        "gender": item["gender"],
        "salary": int(item["salary"]),
    }


def users_entity(entity) -> list:
    return [user_entity(item) for item in entity]