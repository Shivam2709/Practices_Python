import sqlite3

conn = sqlite3.connect('youtube_manager.db')

cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        length TEXT NOT NULL
    )
''')

def list_videos():
    print('\n' + '*' * 50)

    cursor.execute('SELECT * FROM videos')
    rows = cursor.fetchall()  # Fetch all rows first

    if not rows:  # Check if the result set is empty
        print("No videos found.")
    else:
        for row in rows:
            print(row)
    
    print('\n' + '*' * 50)

def add_video(title, length):
    cursor.execute('INSERT INTO videos (title, length) VALUES (?, ?)', (title, length))
    conn.commit()

def update_video(video_id, new_title, new_length):
    cursor.execute("UPDATE videos SET title = ?, length = ? WHERE id = ?", (new_title, new_length, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()

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
            length = input("Enter the video length in min: ")
            add_video(title, length)

        elif choice == '3':
            video_id = input("Enter the video id to update: ")
            name = input("Enter the title of the video: ")
            length = input("Enter the video length in min: ")
            update_video(video_id, name, length)

        elif choice == '4':
            video_id = input("Enter the video id to delete: ")
            delete_video(video_id)

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")
    conn.close()

if __name__ == "__main__":
    main()