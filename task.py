from aiohttp import web
import json
import csv
import os
import glob
import pandas as pd


routes = web.RouteTableDef()

@routes.get('/data')
async def get_data(request):
    try:
        params = request.rel_url.query
        image = params['is_image_exists']

        if image == 'False':
            image = False
        elif image == 'True':
            image = True

        print(image)

        csvfile = open('processed_data/output.csv', 'r')
        data = pd.read_csv(csvfile)
        if image:
            data = data.loc[data['img_path'] != '-']
        else:
            data = data.loc[data['img_path'] == '-']

        js = data.to_dict(orient='records')
        out = json.dumps(js)

        return web.json_response(
            out
        )
    except Exception:
        print('Something wrong')

@routes.post('/data')
async def post_handler(request):
    process_data()
    return web.json_response(
        status=201
    )

def process_data():

    directory = "02-src-data/"

    all_files = []
    for i in os.listdir(directory):
        if i.endswith(".csv"):
            all_files.append(i)

    all_files.sort()

    combined_csv = pd.concat([pd.read_csv(directory+f) for f in all_files])

    arr = []
    image_path = []

    for f in all_files:
        arr.append(f[:-4])
        temp = f[:-4] + ".png"
        try:
            image_path.append(os.path.abspath(temp))
        except Exception:
            image_path.append('-')


    combined_csv.loc[:,'user_id'] = pd.Series(arr, index=combined_csv.index)

    combined_csv = combined_csv[['user_id'] + [col for col in combined_csv.columns if col != 'user_id']]

    combined_csv.loc[:,'img_path'] = pd.Series(image_path, index=combined_csv.index)

    combined_csv.to_csv("processed_data/output.csv", index=False, encoding='utf-8-sig')


app = web.Application()
app.add_routes(routes)


if __name__ == '__main__':
    web.run_app(app, port=8080)