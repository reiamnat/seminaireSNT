import folium
from pyroutelib3 import Router


def creation_carte(latitude_centre, longitude_centre, zoom):
    centre = latitude_centre, longitude_centre
    # Génération de la carte
    return folium.Map(centre, zoom_start=zoom)
    
    
def marqueur_image(carte, latitude, longitude, url_image, message=""):
    icon = folium.features.CustomIcon(icon_image=url_image, icon_size=(30, 30))
    folium.Marker([latitude, longitude], tooltip=message, 
    icon=icon).add_to(carte)
    
    
def itineraire(depart, arrivee, mode):
    """ 
    depart : coordonnées GPS du point de départ
    arrivee : coordonnées GPS du point d'arrivée
    mode :  "car", "cycle", "foot", "horse", "tram", "train" au choix
    """    
    try:
        router = Router(mode)
        D = router.findNode(*depart)
        A = router.findNode(*arrivee)
        status, route = router.doRoute(D, A)
        if status == 'success': 
            return list(map(router.nodeLatLon, route))
    except:    # impossible de générer l'itinéraire demandé        
        return [depart, arrivee]

 
