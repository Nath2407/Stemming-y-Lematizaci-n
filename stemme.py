def stem(word):

    # Lista de prefijos comunes en español
    prefixes = [
        "des", "re", "pre", "in", "a", "an" "anti", "bi", "co", "contra", "ex", "extra", 
        "multi", "super", "ultra", "semi", "im"
    ]
    
    # Eliminar prefijos
    for prefix in prefixes:
        if word.startswith(prefix):
            word = word[len(prefix):]
    
    # Lista de sufijos comunes en español que queremos eliminar
    suffixes = [
        "ar", "er", "ir", "ando", "endo", "iendo", "aba", "ada", "ida", "ía", "ía", "ara",
        "iera", "ad", "ed", "id", "ase", "iese", "aste", "iste", "an", "aban", "ían", "aron",
        "ieron", "ado", "ido", "iendo", "arán", "erán", "irán", "arás", "erás", "irás", "aría",
        "ería", "iría", "aría", "iería", "ador", "edor", "idor", "ante", "mente", "mente",
        "able", "ible", "ismo", "ización", "adora", "edor", "izadora", "al", "il", "ual", "il",
        "icar", "ificar"
    ]
    
    # Aplicar stemming eliminando sufijos
    for suffix in suffixes:
        if word.endswith(suffix):
            word = word[:-len(suffix)]
    
    return word

def stem_text(text):

    # Tokenizar el texto en palabras
    words = text.split()
    
    # Aplicar stemming a cada palabra
    stemmed_words = [stem(word) for word in words]
    
    # Unir las palabras en un nuevo texto
    stemmed_text = ' '.join(stemmed_words)
    
    return stemmed_text

# Ejemplo de texto
text = "Deshacer, rehacer, prever, imposible, antibiótico, exnovia, ultramar, semicírculo"

# Aplicar stemming al texto
stemmed_text = stem_text(text)

# Imprimir el texto original y el texto con stemming
print("Texto original:", text)
print("Texto con stemming:", stemmed_text)