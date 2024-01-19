def transform_data_to_website_format(input_dict: dict) -> list:
    output = []
    output_name = input_dict['first_name'] + ' ' + input_dict['last_name']
    output_state_city = input_dict['state'] + ' ' + input_dict['city']
    output_pictures = input_dict['picture'].split('/')[1]
    output_hobbies = ', '.join(input_dict['hobbies'])
    output_date = input_dict['date_of_birth'][:-5] + ',' + input_dict['date_of_birth'][-4:]
    for key, value in input_dict.items():
        if key == 'first_name':
            output.append(output_name)
        if key == 'last_name' or key == 'city':
            continue
        if key == 'date_of_birth':
            output.append(output_date)
        if key == 'hobbies':
            output.append(output_hobbies)
        if key == 'picture':
            output.append(output_pictures)
        if key == 'state':
            output.append(output_state_city)
    return output


def get_keys_from_dict(input_dict: dict, val: int=1) -> list:
    keys = [k for k, v in input_dict.items() if v == val]
    if keys:
        return keys
    return None