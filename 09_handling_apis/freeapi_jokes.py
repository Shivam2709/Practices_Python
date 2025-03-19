import requests 

def fetch_random_joke():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    data = response.json()


    if data['success'] and 'data' in data:
        # print(data)
        joke = data['data']
        random_joke = joke['content']
        return random_joke
    else:
        raise Exception("Failed to fetch joke")
    
def main():
    try:
        joke = fetch_random_joke()
        print(f"Random Joke: {joke}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
