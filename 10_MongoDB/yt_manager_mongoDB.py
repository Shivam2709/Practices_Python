from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://shivamthakur2709:shivamthakur2709@python-projects.l5pac.mongodb.net/", tlsAllowInvalidCertificates=True)
# Note a good practice to use environment variables to store the connection string
# tlsAllowInvalidCertificates=True is used to avoid the SSL certificate error but it is not a good practice

db = client["yt_manager"]
collection = db["videos"]

print(collection)

def list_videos():
    print('\n' + '*' * 50)
    videos = collection.find()
    if not videos:
        print("No videos found.")
    else:
        for video in videos:
            print(f"Video ID: {video['_id']}, Title: {video['title']}, and Length: {video['length']}")
    print('\n' + '*' * 50)

def add_video(title, length):
    collection.insert_one({"title": title, "length": length})

def update_video(video_id, new_title, new_length):
    collection.update_one({"_id": ObjectId (video_id)}, {"$set": {"title": new_title, "length": new_length}})

def delete_video(video_id):
    collection.delete_one({"_id":ObjectId (video_id)})

def main():
    while True:
        print("\n Youtube Manager app with DB ")
        print("1. List all youtube videos ")
        print("2. Add a new youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            title = input("Enter the title of the video: ")
            length = input("Enter the length of the video: ")
            add_video(title, length)
        elif choice == '3':
            video_id = input("Enter the video id to update: ")
            new_title = input("Enter the new title of the video: ")
            new_length = input("Enter the new length of the video: ")
            update_video(video_id, new_title, new_length)
        elif choice == '4':
            video_id = input("Enter the video id to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()




