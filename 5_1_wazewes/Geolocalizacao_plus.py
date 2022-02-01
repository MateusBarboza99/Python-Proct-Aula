from pygeocoder import Geocoder

endereco = "avenida paulista, 100 São Paulo:"
resultado = Geocoder("AIzaSyAIYOcoggbhzTCe5rGF86FLUKXWKw2yPMM").reverse_geocode(-23.5703022, -46.6451267)
print(resultado)

