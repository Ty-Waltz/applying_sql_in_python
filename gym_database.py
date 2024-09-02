import mysql.connector

def add_member(id, name, age):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="user",
            password="password",
            database="gym_database"
        )
        cursor = conn.cursor()

        # Creating a SQL query to add a new member
        cursor.execute("INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)", (id, name, age))

        # This will commit the changes
        conn.commit()
        print("Member added successfully!")

    except mysql.connector.IntegrityError as e:
        print(f"Error: {e}")
        print("Member ID already exists or other constraint violated.")
    
    finally:
        cursor.close()
        conn.close()
# Example of how it would be used
add_member(1, 'John Doe', 30)

def add_workout_session(member_id, session_date, session_time, activity):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="user",
            password="password",
            database="gym_database"
        )
        cursor = conn.cursor()

        # Adds a query to SQL
        cursor.execute("INSERT INTO WorkoutSessions (member_id, session_date, session_time, activity) VALUES (%s, %s, %s, %s)",
                       (member_id, session_date, session_time, activity))

        # Commits the changes to SQL
        conn.commit()
        print("Workout session added successfully!")

    except mysql.connector.IntegrityError as e:
        print(f"Error: {e}")
        print("Invalid member ID or other constraint violated.")
    
    finally:
        cursor.close()
        conn.close()

# Example of how it would be used
add_workout_session(1, '2024-08-29', '15:30', 'Cardio')

def update_member_age(member_id, new_age):
    try:
        conn = mysql.connector.connect(
            host="localhost",
           user="user",
            password="password",
            database="gym_database"
        )
        cursor = conn.cursor()

        # Check if member exists
        cursor.execute("SELECT * FROM Members WHERE id = %s", (member_id,))
        member = cursor.fetchone()

        if member:
            # query to update age
            cursor.execute("UPDATE Members SET age = %s WHERE id = %s", (new_age, member_id))
            conn.commit()
            print("Member age updated successfully!")
        else:
            print("Member not found.")
    
    finally:
        cursor.close()
        conn.close()

# Example 
update_member_age(1, 31)

def delete_workout_session(session_id):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="user",
            password="password",
            database="gym_database"
        )
        cursor = conn.cursor()

        # Check if session exists
        cursor.execute("SELECT * FROM WorkoutSessions WHERE session_id = %s", (session_id,))
        session = cursor.fetchone()

        if session:
            # SQL query to delete a session
            cursor.execute("DELETE FROM WorkoutSessions WHERE session_id = %s", (session_id,))
            conn.commit()
            print("Workout session deleted successfully!")
        else:
            print("Session ID not found.")
    
    finally:
        cursor.close()
        conn.close()

# Example 
delete_workout_session(1)