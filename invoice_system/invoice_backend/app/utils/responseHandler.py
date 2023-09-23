def success_response(**kwargs):
    response = {
        "status": 200
    }
    response.update(kwargs)
    return response
