import json

def saveGraphicsPath(path):
    with open('graphicsPath.json', 'w') as f:
        json.dump({'file_path' : path}, f)

def loadGraphicsPath():
    try:
        with open('graphicsPath.json', 'r') as f:
            path = json.load(f)
            return path['file_path']
    except:
        pass    