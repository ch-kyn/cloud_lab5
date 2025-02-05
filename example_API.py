from fastapi import FastAPI
import requests
# import subprocess

app = FastAPI()

database = [{'id': 0, 'item': 'pants'},
            {'id': 1, 'item': 'shirt'},
            {'id': 2, 'item': 'island'}]
    
@app.get('/')
def read_root():
    return {'Hello': 'World! :D'}

@app.get('/items/{item_id}')
def read_item(item_id: int, item: str | None = None):
    if item_id == database[item_id]['id']:
        return {'item_id': item_id, 'item': database[item_id]['item']}

@app.get('/all')
def read_all_items():
    all_items = []
    return database

# test this later with thunder strike something but am lazy rn
@app.post('/items') 
def add_item(item: str):
    new_item = {'id': len(database) + 1, 'item': item}
    database.append(new_item)
    return item

# instead of repeating the command
if __name__ == '__main__':
    import subprocess
    subprocess.run(['uvicorn', 'example_API:app', '--reload'])