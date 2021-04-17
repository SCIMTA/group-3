def on_success(data=None, message='Thành công', status=1):
    if data is not None:
        return {
            'message': message,
            'data': data,
            'status': status,
        }

    return {
        'message': message,
        'status': status
    }


def on_fail(message='Thất bại', status=0):
    return {
        'message': message,
        'status': status
    }
