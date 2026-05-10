import random
from flask import Flask
from datos import residuos

app = Flask(__name__)


facts_list = [
    "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo.",
    "Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo.",
    "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
    "La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos.",
    "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos.",
    "Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos.",
    "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas."
    
]

@app.route("/")
def home():
    return (
        f'<a href="/random_fact">¡Ver un dato aleatorio!</a>'
        f'<a href="/lista_de_cosas_organicas_reciclables_o_basura">¡Ver una lista de cosas orgánicas, reciclables o basura!</a>'
    )
    

@app.route("/lista_de_cosas_organicas_reciclables_o_basura")
def lista_residuos():
    # .items() toma la pareja (llave y valor). 
    # list() lo convierte en algo que random puede leer.
    objeto, tipo = random.choice(list(residuos.items()))
    
    return f'<p>El residuo <strong>{objeto}</strong> es de tipo: <strong>{tipo}</strong></p>'

@app.route("/secret!")
def pagina_secreta():
    # randint(1, 2) elige un número entero aleatorio entre 1 y 2
    number = random.randint(1, 2)
    
    # Si el número es 1, la variable moneda será "Cara"
    if number == 1:
        moneda = "Cara"
    # Si no es 1 (es decir, si es 2), será "sol"
    else:
        moneda = "sol"
    
    # Devolvemos el resultado dentro de una etiqueta de párrafo <p> de HTML
    return f"<p> {moneda} </p>"

@app.route("/random_fact")
def facts():
    return f'<p>{random.choice(facts_list)}</p>'

app.run(debug=True)
