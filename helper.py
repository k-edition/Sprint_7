import data


class ModifyData:
    @staticmethod
    def modify_create_courier_body(key, value):
        body = data.generate_payload_for_create_courier().copy()
        body[key] = value

        return body

    @staticmethod
    def modify_login_courier_body(body, key, value):
        new_body = body.copy()
        new_body[key] = value
        return new_body

    @staticmethod
    def modify_payload_for_login_courier(body):
        new_body = body.copy()
        del new_body["firstName"]
        return new_body

    @staticmethod
    def modify_create_order_body(key, value):
        body = data.generate_payload_for_create_order().copy()
        body[key] = value
        return body
