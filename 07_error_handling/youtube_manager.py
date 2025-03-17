import json

file_name = 'youtube.txt'

def load_data():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open(file_name, 'w') as file:
        json.dump(videos, file)
    
def list_all_videos(videos):
    print('\n')
    print('*' * 50)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['title']}, Duration: {video['length']}")
    print('\n')
    print('*' * 50)    

def add_new_video(videos):
    title = input("Enter the title of the video: ")
    lenght =input("Enter the video Length In Min: ")
    videos.append({
        'title': title,
        'length': lenght
    })
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new title of the video: ")
        length = input("Enter the new length of the video: ")
        videos[index - 1] = {
            'title': name,
            'length': length
        }
        save_data_helper(videos)
    else:
        print("Invalid index Selected. Please try again.")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to delete: "))

    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("Invalid index Selected. Please try again.")

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option: ")
        print("1. List all youtube videos ")
        print("2. Add a new youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit")
        choice = input("Enter your choice: ")
        #print(videos)

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_new_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()