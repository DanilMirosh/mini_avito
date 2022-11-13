import csv, json

# Params
csv_file_ads = 'ads.csv'
json_file_ads = '../ads/fixtures/ads.json'
ads_model = 'ads.ad'

csv_file_categories = 'categories.csv'
json_file_categories = '../ads/fixtures/categories.json'
categories_model = 'ads.category'

csv_file_location = 'location.csv'
json_file_location = '../ads/fixtures/location.json'
location_model = 'users.location'

csv_file_user = 'user.csv'
json_file_users = '../ads/fixtures/users.json'
users_model = 'users.user'


# Functions
def csv_to_json(csv_file_path: str, json_file_path: str, model: str) -> str:
    """Convert csv to json"""
    result = []
    with open(csv_file_path, encoding='utf-8') as f:
        for row in csv.DictReader(f):
            to_add = {'model': model, 'pk': int(row['Id'] if 'Id' in row else row['id'])}
            if 'id' in row:
                del row['id']
            else:
                del row['Id']

            if 'location_id' in row:
                row['location'] = [int(row['location_id'])]
                del row['location_id']

            if 'is_published' in row:
                if row['is_published'] == 'TRUE':
                    row['is_published'] = True
                else:
                    row['is_published'] = False
            if 'price' in row:
                row['price'] = int(row['price'])

            to_add['fields'] = row
            result.append(to_add)

    with open(json_file_path, 'w', encoding='utf-8') as file:
        file.write(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    csv_to_json(csv_file_ads, json_file_ads, ads_model)
    csv_to_json(csv_file_categories, json_file_categories, categories_model)
    csv_to_json(csv_file_location, json_file_location, location_model)
    csv_to_json(csv_file_user, json_file_users, users_model)
