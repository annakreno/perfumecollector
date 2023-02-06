from django.shortcuts import render

perfume = [
  {'name': 'Monstera', 'brand': 'Xinú', 'notes': ['Monstera fruit and leaves', 'Sacred ear flower', 'White datura', 'Bull horn orchid', 'Lush', 'Crunchy leaf', 'Jungle', 'Jade'], 'description': 'Monstera is inspired by the jungle, the green leaves of the monstera deliciosa plant, the narcotic perfume of the datura flower, the subtle and magnetic honey of the torito orchid, and the smell of moss over exotic woods. Monstera is astonishingly juicy and lush, like a leaf that has been snapped open, allowing droplets of the plant juice to seep out. Supported by a damp earth accord, bitter moss, and the sharpness of a pineapple-like note from the monstera fruit, embraced by a creamy white floral tone, with a hint of bitter cocoa and vanilla. Technically impressive!'},
  {'name': 'Thé Noir 29', 'brand': 'Le Labo', 'notes': ['bergamot', 'fig', 'bay leaves', 'cedarwood', 'vetiver', 'musk', 'dry', 'leafy', 'hay', 'tobacco'], 'description': 'THÉ NOIR 29 is an ode to the noble leaf and the craft that surrounds it. THÉ NOIR 29 combines depth and freshness, softness and strength through permanent oscillation between the light of bergamot, fig, and bay leaves and the depth of cedarwood, vetiver, and musk. A special extraction of black tea leaves wraps up the composition by bringing to the formula a dry, leafy, hay, tobacco feeling in the dry down to transform this creation into a sensuous and addictive essence.'},
]

def home(request):
    return render(request, 'home.html')

# Create your views here.
