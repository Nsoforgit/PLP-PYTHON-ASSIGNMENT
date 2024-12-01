class Smartphone:
    def __init__(self, brand, model, storage_capacity, color):
        self.brand = brand
        self.model = model
        self.storage_capacity = storage_capacity
        self.color = color
        self.battery_level = 100

    def make_call(self, number):
        print(f"Calling {number}...")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

    def charge_battery(self, minutes):
        self.battery_level += minutes // 10

    def check_battery(self):
        print(f"Battery level: {self.battery_level}%")


class SmartPhoneWithCamera(Smartphone):
    def __init__(self, brand, model, storage_capacity, color, camera_megapixels):
        super().__init__(brand, model, storage_capacity, color)
        self.camera_megapixels = camera_megapixels

    def take_picture(self):
        print(f"Taking a picture with {self.camera_megapixels} MP camera")


# Create instances of the Smartphone class
phone1 = Smartphone("Apple", "iPhone 14", 128, "Black")
phone2 = Smartphone("Samsung", "Galaxy S23", 256, "White")

# Create an instance of the SmartPhoneWithCamera class
camera_phone = SmartPhoneWithCamera("Google", "Pixel 7 Pro", 512, "Black", 48)

# Use the methods of the objects
phone1.make_call("123-456-7890")
phone2.send_message("987-654-3210", "Hello!")
camera_phone.take_picture()
camera_phone.charge_battery(30)
camera_phone.check_battery()