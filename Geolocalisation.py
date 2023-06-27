# La bibliothèque 
import folium

latitude = ...  # Attention le séparateur décimal est le point comme sur la calculatrice
longitude = ...

# définir le niveau de zoom entre 1 (planisphère) et 18 (bâtiment)
zoom = 17

# créer la carte en indiquant les coordonnées du centre et un niveau de zoom
carte = folium.Map(location=[latitude, longitude], 
                    zoom_start=zoom)

# ajout d'une icône image
# le texte du popup s'affiche au survol
icon = folium.features.CustomIcon(icon_image="LeLyceeMalherbe.jpg", icon_size=(30, 30))
folium.Marker([latitude, longitude], tooltip="Lycée Malherbe", icon=icon).add_to(carte)

# Affichage de la carte en cliquant sur l'icône "vue graphique".
carte.display()