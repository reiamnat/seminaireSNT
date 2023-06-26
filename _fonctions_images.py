from PIL import Image


def nature(fichier_image) :
    """la fonction nature prend en argument le nom complet du fichier (nom et extension) écrit entre guillemets
    cette fonction affiche quelques informations sur l'image"""
    # on "ouvre" l'image pour déterminer ses caractéristiques
    imgsource = Image.open(fichier_image) 
    print("Format de l'image : ", imgsource.format)
    print("Taille de l'image : ", imgsource.size)
    print("Mode de l'image : ", imgsource.mode)
    # on récupère les valeurs du couple imgsource.size donnant la largeur et la hauteur
    L, H = imgsource.size 
    print("En largeur, l'image contient :", L, " pixels")
    print("En hauteur, l'image contient :", H, " pixels")
    # on récupère le codage du pixel de coordonnées (0, 0)
    pixel = imgsource.getpixel((0, 0)) 
    print("le pixel (0, 0) est codé par :", pixel) 
    # instruction pour voir l'image 
    imgsource.show()
    # pour "fermer" l'image
    imgsource.close() 


# ATTENTION : la fonction transformation ne pourra être utilisée que pour des images en mode L
 
 
def transformation(nom_image, f):
    """nom_image est le nom du fichier contenant l'image originale avec son extension et entre guillemets
    f est une fonction qui prend en paramètre un entier compris entre 0 et 255 et renvoie un entier compris entre 0 et 255
    cette fonction affiche une image en nuances de gris"""
    # on ouvre le fichier image à transformer
    img = Image.open(nom_image)
    # on récupère la largeur et la hauteur de l'image
    L, H = img.size 
    # on crée une nouvelle image de même mode (ici 'L') que img et de même taille
    # tous les pixels de cette image sont à 0 autrement dit elle est noire.
    img1 = Image.new(img.mode, img.size) 
    # on parcourt l'image de haut en bas et de droite à gauche pour accéder à chaque pixels de l'image
    for y in range(H):
        for x in range(L):
            # permet de récupérer l'entier compris entre 0 et 255 qui donne l'intensité de lumière
            # correspondant au pixel de coordonnées (x,y)
            valeur_pixel = img.getpixel((x, y)) 
            # on calcule la nouvelle valeur du pixel
            nouvelle_valeur = f(valeur_pixel)  
            # on affecte la valeur que l'on vient de calculer au pixel de coordonnées (x,y) de la nouvelle image
            img1.putpixel((x, y), nouvelle_valeur)
    # on ferme le fichier contenant l'image  originale
    img.close()
    # on affiche la nouvelle image
    img1.show()
    # on ferme le fichier contenant la nouvelle image 
    img1.close()
    
 
# ATTENTION : la fonction transformation_gris ne pourra être utilisée que pour des images en mode RGB

    
def transformation_gris(nom_image, f):
    """nom_image est le nom du fichier contenant l'image originale avec son extension et entre guillemets
    f est une fonction qui prend en paramètre un triplet d'entiers compris entre 0 et 255 et qui renvoie un entier compris entre 0 et 255
    la fonction affiche une image en mode L"""
    img = Image.open(nom_image) 
    L, H = img.size 
    # on crée une nouvelle image de mode 'L' et de même taille que l'image originale
    # tous les pixels de cette image sont à 0 autrement dit elle est noire.
    img1 = Image.new("L", img.size) 
    for y in range(H):
        for x in range(L): 
            valeur_pixel = img.getpixel((x, y)) 
            # on calcule le gris correspondant
            nouvelle_valeur = f(valeur_pixel)  
            # on affecte la valeur que l'on vient de calculer au pixel de coordonnées (x,y) de la nouvelle image
            img1.putpixel((x, y), nouvelle_valeur)             
    img.close()
    img1.show()
    img1.close() 
 
    
 # ATTENTION : la fonction transformation_couleur ne pourra être utilisée que pour des images en mode RGB
 
    
def transformation_couleur(nom_image, f):
    """nom_image est le nom du fichier contenant l'image originale avec son extension et entre guillemets
    f est une fonction qui prend en paramètre un triplet d'entiers compris entre 0 et 255 et qui renvoie un triplet d'entiers compris entre 0 et 255
    la fonction affiche une image en mode RGB"""
    img = Image.open(nom_image) 
    L, H = img.size 
    # on crée une nouvelle image de mode 'L' et de même taille que l'image originale
    # tous les pixels de cette image sont à 0 autrement dit elle est noire.
    img1 = Image.new("RGB", img.size) 
    for y in range(H):
        for x in range(L): 
            valeur_pixel = img.getpixel((x, y)) 
            # on calcule le gris correspondant
            nouvelle_valeur = f(valeur_pixel)  
            # on affecte la valeur que l'on vient de calculer au pixel de coordonnées (x,y) de la nouvelle image
            img1.putpixel((x, y), nouvelle_valeur)             
    img.close()
    img1.show()
    img1.close() 
