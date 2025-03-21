import sqlite3
import re

# Database setup
conn = sqlite3.connect("game_data.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        wins INTEGER DEFAULT 0,
        losses INTEGER DEFAULT 0
    )
''')
conn.commit()


# Function to validate email using regex
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)


# Function for signing up a new player
def sign_up():
    while True:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        email = input("Enter email: ").strip()

        if not is_valid_email(email):
            print("Invalid email format. Try again.")
            continue

        try:
            cursor.execute("INSERT INTO players (username, password, email) VALUES (?, ?, ?)",
                           (username, password, email))
            conn.commit()
            print("Sign-up successful! You can now log in.")
            return
        except sqlite3.IntegrityError:
            print("Username or email already exists. Try again.")


# Function for logging in an existing player
def log_in():
    while True:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        cursor.execute("SELECT * FROM players WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()

        if user:
            print(f"Login successful! Welcome, {username}!")
            return username  # Return username for session tracking
        else:
            print("Invalid credentials. Try again.")


# Function to display the leaderboard
def view_leaderboard():
    cursor.execute("SELECT username, wins, losses FROM players ORDER BY wins DESC, losses ASC")
    players = cursor.fetchall()

    print("\n🏆 Leaderboard 🏆")
    print("-" * 30)
    print("{:<15} {:<10} {:<10}".format("Player", "Wins", "Losses"))
    print("-" * 30)

    for player in players:
        print("{:<15} {:<10} {:<10}".format(player[0], player[1], player[2]))

    print("-" * 30)


# Function to update the leaderboard after a game
def update_leaderboard(winner, loser):
    cursor.execute("UPDATE players SET wins = wins + 1 WHERE username=?", (winner,))
    cursor.execute("UPDATE players SET losses = losses + 1 WHERE username=?", (loser,))
    conn.commit()


# Function to display the main menu
def main_menu():
    while True:
        print("\n🎯 Shooting Game Menu 🎯")
        print("1. Sign Up")
        print("2. Sign In")
        print("3. View Leaderboard")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            sign_up()
        elif choice == "2":
            user1 = log_in()
            print("Waiting for Player 2 to log in...")
            user2 = log_in()
            print(f"\n{user1} and {user2} are ready! Starting game...\n")
            return user1, user2  # Start game with logged-in players
        elif choice == "3":
            view_leaderboard()
        elif choice == "4":
            print("Goodbye!")
            conn.close()
            exit()
        else:
            print("Invalid choice. Try again.")


def start_game():
    return main_menu()

if __name__ == "__main__":
    player1, player2 = main_menu()
