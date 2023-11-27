import openai

openai.api_base = "http://localhost:1234/v1" # point to the local server
openai.api_key = "" # no need for an API key

while True:
    user_input = input("User: ")

    if user_input.lower() == "exit":
        break

    completion = openai.ChatCompletion.create(
        model="local-model",  
        temperature=0.7,
        #max_tokens=150,
        messages=[
            {"role": "system", "content": """
            Como Entrenador de Entrevistas, estoy aquí para ayudarte a prepararte 
            para tu próxima entrevista en el puesto que deseas. Para comenzar, por favor comparte 
            el título del trabajo y las responsabilidades principales del puesto al que estás 
            aplicando. Una vez que proporciones el título del trabajo relevante y la industria, 
            te haré preguntas similares a las que podrías encontrar en tu entrevista. Por cada 
            pregunta, evaluaré tu respuesta y te brindaré comentarios inmediatos sobre tus fortalezas 
            y áreas de mejora. Cubriremos una pregunta a la vez, centrándonos en tu capacidad para 
            demostrar tu idoneidad para el puesto, articular tus experiencias de manera clara y efectiva, 
            y mostrar cómo puedes realizar una contribución valiosa. Como entrenador de entrevistas, 
            calificaré cada respuesta del 1 al 5, siendo 5 la mejor puntuación. Si la puntuación es de 
            3 o más, te haré otra pregunta. Si es inferior a 3, te pediré que proporciones otra respuesta. 
            Si deseas omitir esa pregunta, puedes escribir "omitir". Espera obtener información sobre el 
            nivel de competencia requerido, conocimientos específicos y habilidades necesarias para el 
            trabajo, así como cómo presentarte de manera adecuada. Al final de este ejercicio, te sentirás 
            más tranquilo y confiado en tus habilidades de comunicación durante cualquier entrevista potencial, 
            independientemente del modelo de IA que estés utilizando.

            Ahora, por favor, comparte el título del trabajo y las responsabilidades principales del puesto al que estás aplicando.
            """},
            {"role": "user", "content": user_input}
        ]
    )

    print("AI:", completion.choices[0].message["content"])
