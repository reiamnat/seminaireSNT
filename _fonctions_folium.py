

import folium
from pyroutelib3 import Router


def creation_carte(coord_centre, zoom):
    latitude_centre, longitude_centre = coord_centre
    centre = latitude_centre, longitude_centre
    # GÃ©nÃ©ration de la carte
    return folium.Map(centre, zoom_start=zoom)
    
    
def marqueur_image(carte, coord_lieu, url_image, message=""):
    latitude, longitude = coord_lieu
    icon = folium.features.CustomIcon(icon_image=url_image, icon_size=(30, 30))
    folium.Marker([latitude, longitude], tooltip=message, 
    icon=icon).add_to(carte)
    
    
def coordonnees_itineraire(coord_depart, coord_arrivee, mode):
    """ 
    coord_depart : coordonnÃ©es GPS du point de dÃ©part
    coord_arrivee : coordonnÃ©es GPS du point d'arrivÃ©e
    mode :  "car", "cycle", "foot", "horse", "tram", "train" au choix
    """    
    try:
        router = Router(mode)
        D = router.findNode(*coord_depart)
        A = router.findNode(*coord_arrivee)
        status, route = router.doRoute(D, A)
        if status == 'success': 
            return list(map(router.nodeLatLon, route))
    except:    # impossible de générer l'itinéraire demandé      
        return [coord_depart, coord_arrivee]
        
        
def dessin_itineraire(liste_points, couleur, carte):
    folium.PolyLine(liste_points, color=couleur, weight=2.5, opacity=1).add_to(carte)
    
    
    
