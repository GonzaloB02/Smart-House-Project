import time
from datetime import datetime
from sistema import automatizaciones_registradas, obtener_estado

def monitorizacion_automatica():
    print('\nMonitorización iniciada.')
    while True:
        hora_actual = datetime.now().strftime('%I:%M %p')

        for auto in automatizaciones_registradas:
            if hora_actual == auto.hora_inicio and not auto.activado:
                auto.dispositivo.estado = auto.estado
                auto.activado = True
                print(f'\n{auto.dispositivo.nombre}: {auto.estado.nombre} (Automatización {auto.nombre} iniciada).')

            if hora_actual == auto.hora_fin and auto.activado:
                auto.dispositivo.estado = obtener_estado('APAGADO')
                auto.activado = False
                print(f'\n{auto.dispositivo.nombre}: APAGADO (Automatización {auto.nombre} finalizada)')
                
        time.sleep(60)


