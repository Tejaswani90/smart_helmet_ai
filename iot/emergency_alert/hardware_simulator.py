class HardwareSimulator:

    def green_led_on(self):
        print("GREEN LED: ON")

    def green_led_off(self):
        print("GREEN LED: OFF")

    def red_led_on(self):
        print("RED LED: ON")

    def red_led_off(self):
        print("RED LED: OFF")

    def buzzer_on(self):
        print("BUZZER: ON")

    def buzzer_off(self):
        print("BUZZER: OFF")


helmet = HardwareSimulator()

print("\nSMART HELMET HARDWARE SIMULATOR")

print("\nNORMAL STATE")
helmet.green_led_on()
helmet.red_led_off()
helmet.buzzer_off()

print("\nACCIDENT STATE")
helmet.green_led_off()
helmet.red_led_on()
helmet.buzzer_on()

print("\nRIDER SAFE")
helmet.green_led_on()
helmet.red_led_off()
helmet.buzzer_off()

print("\nEMERGENCY STATE")
helmet.green_led_off()
helmet.red_led_on()
helmet.buzzer_on()