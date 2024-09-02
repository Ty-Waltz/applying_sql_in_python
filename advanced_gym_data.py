import mysql.connector

def get_members_in_age_range(start_age, end_age):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="user",
            password="password",
            database="gym_database"
        )
        cursor = conn.cursor()

        # SQL query  to fetch members in the specified age range
        query = "SELECT id, name, age FROM Members WHERE age BETWEEN %s AND %s"
        cursor.execute(query, (start_age, end_age))

        # Fetch all results
        members = cursor.fetchall()

        if members:
            print(f"Members between the ages of {start_age} and {end_age}:")
            for member in members:
                print(f"ID: {member[0]}, Name: {member[1]}, Age: {member[2]}")
        else:
            print(f"No members found between the ages of {start_age} and {end_age}.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        cursor.close()
        conn.close()

# Example 
get_members_in_age_range(25, 30)