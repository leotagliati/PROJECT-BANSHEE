import time
import RPi.GPIO as GPIO

class InputSystem:
    def __init__(self, pin_map, poll_interval=0.05, debug_interval=1.0):
        """
        pin_map: {pino: ação}, exemplo {16: "UP", 23: "DOWN", 20: "LEFT", 21: "RIGHT", 18: "FIRE"}
        poll_interval: tempo entre leituras dos pinos
        debug_interval: tempo entre prints de debug (em segundos)
        """
        self.pin_map = pin_map
        self.poll_interval = poll_interval
        self.debug_interval = debug_interval
        self.states = {action: False for action in pin_map.values()}
        self.prev_states = self.states.copy()
        self.last_debug = time.time()

        GPIO.setmode(GPIO.BCM)
        for pin in pin_map.keys():
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def update(self):
        """Atualiza o estado de cada ação com base nos pinos GPIO"""
        for pin, action in self.pin_map.items():
            self.prev_states[action] = self.states[action]
            self.states[action] = (GPIO.input(pin) == GPIO.LOW)

        # Debug print a cada debug_interval
        now = time.time()
        if now - self.last_debug >= self.debug_interval:
            self.debug_print_buttons()
            self.last_debug = now

    def is_pressed(self, action):
        return self.states.get(action, False)

    def is_pressed_edge(self, action):
        return self.states.get(action, False) and not self.prev_states.get(action, False)

    def debug_print_buttons(self):
        pressed = [a for a, v in self.states.items() if v]
        if pressed:
            print("Botões pressionados:", ", ".join(pressed))

    def cleanup(self):
        GPIO.cleanup()
