from geocoder import geocode

def get_address_coords(address):
    toponym = geocode(address)
    toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    # Печатаем извлечённые из ответа поля:
    return toponym_coodrinates


def main():
    for address in ['Москва, Красная площадь, 1']
        coords = get_addres_coords(address)
        print(f'{address} имеет координаты: {coords}')
    print('')

if __name__ == '__main__':
    main()
