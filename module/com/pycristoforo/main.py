from module.com.pycristoforo.utils.constants import Constants
from module.com.pycristoforo.geo.eucountries import EUCountryList
from shapely.geometry import Point, Polygon, MultiPolygon
from numpy.random import uniform

def main(key: str):

    # reading
    country_ids = EUCountryList(Constants.EU_PATH)
    uid = country_ids.get_by_key(key)
    shape_dict = country_ids.get_by_key(uid)

    # create shape
    poligons = []
    if shape_dict['type'] == "MultiPolygon":
        for polygon in shape_dict['coordinates']:
            for sub_polygon in polygon:
                pol = Polygon(sub_polygon)
                poligons.append(pol)
        shape = MultiPolygon(poligons)
    else:
        if shape_dict['type'] == "Polygon":
            shape = Polygon(shape_dict['coordinates'][0])
        else:
            print("Other")

    #print(shape_dict)
    for s in shape:
        string = str(s.envelope).  \
              replace('POLYGON', '').\
              replace('(', '[').\
              replace(',', '],[').\
              replace(' [[', '[[').\
              replace(' 4', ',4'). \
              replace(' 3', ',3'). \
            replace(' 1', ',1'). \
            replace(' 2', ',2'). \
            replace(' 5', ',5'). \
            replace(' 6', ',6'). \
            replace(' 7', ',7'). \
            replace(' 8', ',8'). \
            replace(' 9', ',9'). \
            replace('[,','[').\
            replace('))', ']]')
        print('{ "type": "Feature","geometry": {"type": "Polygon","coordinates": ['+string+']},"properties": {"prop0": "value0","prop1": {"this": "that"}}},')

    generate_random(shape, 500)


def generate_random(shape, points: int):
    min_lng = shape.bounds[0]
    min_lat = shape.bounds[1]
    max_lng = shape.bounds[2]
    max_lat = shape.bounds[3]
    i = 0
    c = 0
    while i != points:
        c = c+1
        val1 = uniform(min_lng, max_lng)
        val2 = uniform(min_lat, max_lat)
        random_point = Point(val1, val2)
        if random_point.within(shape):
            print(
                '{"type": "Feature","geometry": {"type": "Point","coordinates": ['+str(val1)+','+str(val2)+']},"properties": {"prop0": "value0","prop1": { "this": "that" }}},'
            )
            i = i+1
    print(f"Tentative {c}, fair {i}")


if __name__ == '__main__':
    main("Italy")


