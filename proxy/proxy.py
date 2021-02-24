import requests
class Proxy:
    def __init__(self, instance):
        self.instance = instance

    def proxy(self):
        object_instance = self.instance
        if object_instance.number % 2 == 0:
            print("proxy actuando... :)")
            return True
        return False
class Proxy2:
    def __init__(self, instance):
        self.instance = instance

    def proxy(self):
        object_instance = self.instance
        if object_instance.number % 2 == 0:
            continente="asia"
            response = requests.get(f"https://restcountries.eu/rest/v2/region/{continente}")
            print(response.content)
            return True
        else:
            continente="americas"
            response = requests.get(f"https://restcountries.eu/rest/v2/region/{continente}")
            print(response.content)
            return True