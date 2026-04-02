import json

class JsonWriter:
    
    def write(self, data, path):
        with open(path, "w") as f:
            json.dump(data, f, indent=2, default=str)