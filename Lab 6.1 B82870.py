#Laboratorio 6 Evelyn Feng Wu B82870
import time
import random
import threading


#eventos.py
class EventManager:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event, callback):
        if event not in self.subscribers:
            self.subscribers[event] = []
        self.subscribers[event].append(callback)

    def unsubscribe(self, event, callback):
        if event in self.subscribers and callback in self.subscribers[event]:
            self.subscribers[event].remove(callback)

    def notify(self, event, data=None):
        if event in self.subscribers:
            for callback in self.subscribers[event]:
                callback(data)

#datamanager.py

class RealTimeDataManager:
    def __init__(self):
        self.data = {"temperatura": 25.0, "humedad": 60.0}
        self.event_manager = EventManager()

    def start_real_time_updates(self):
        while True:
            time.sleep(3)
            self.generate_real_time_data()
            # Notificar que los datos han cambiado
            self.event_manager.notify("datos_cambiados", self.data.copy())

    def generate_real_time_data(self):
        self.data["temperatura"] += random.uniform(-1.0, 1.0)
        self.data["humedad"] += random.uniform(-2.0, 2.0)

# Si este módulo es ejecutado directamente
if __name__ == "__main__":
    # Crea una instancia de RealTimeDataManager
    real_time_data_manager = RealTimeDataManager()

    # Ac[a se define un callback para imprimir los datos
    def print_data_callback(data):
        print("Datos actualizados:", data)

    # Suscribe el callback al evento "datos_cambiados"
    real_time_data_manager.event_manager.subscribe("datos_cambiados", print_data_callback)

    # Inicia el hilo para actualizaciones en tiempo real
    update_thread = threading.Thread(target=real_time_data_manager.start_real_time_updates)
    update_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nPrograma terminado.")
