import json



with open('my_data.json', 'r') as f:
    json_obj = json.loads(f.read())

for index, obj in enumerate(json_obj):
    full_name = (json_obj['ad_user'][index]['full_name'])
    email = f"{full_name.lower().replace(' ', '.')}@example.com"

print(email)