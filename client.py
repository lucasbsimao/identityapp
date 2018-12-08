import requests
import time

# PythonDecorators/entry_exit_class.py
def show_time(func):
    def wrapper(*args):
        start_time = time.time()
        result  = func(*args)
        delta_time = time.time() - start_time
        print(func.__name__ + "took {0} ".format(delta_time) + " seconds and returned: {0} ".format(result))

        return result

    return wrapper
    

class Client:
    def __init__(self, url):
        self.url = url

    @show_time
    def callPostId(self):
        payload = "{id:1}"

        return requests.post(self.url,data=payload) 

    @show_time
    def callGetId(self):
        urlForId = self.url + "/1"

        return requests.get(urlForId)

if __name__ == "__main__":
    client = Client("http://127.0.0.1:8080/api/user")
    client.callGetId()
    client.callPostId()
