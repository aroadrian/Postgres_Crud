# CRUD operations

# Create
# Read
# Update
# Delete
import psycopg2


def create_person(conn, firstname, lastname, age, ):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO person (firstname, lastname, age) VALUES (%s, %s, %s)", (firstname, lastname, age))
    conn.commit()
    cursor.close()

def read_all_persons(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM person")
    persons = cursor.fetchall()
    cursor.close()
    return persons

def read_person(conn, person_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM person WHERE id = %s", (person_id,))
    one_person = cursor.fetchone()
    cursor.close()
    return one_person

def update_person(conn, person_id, person):
    cursor = conn.cursor()
    cursor.execute("UPDATE person SET firstname = %s, lastname = %s, age = %s WHERE id = %s", (person['firstname'], person['lastname'], person['age'], person_id))
    conn.commit()
    cursor.close()


def delete_person(conn, person_id):
    pass


if __name__ == "__main__":
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="admin"
    )
    #insert data on Database
    #create_person(conn, "Adrian", "Aro", 25)
    persons = read_all_persons(conn)
    print(persons)

    #select one data by ID
    person_id = 3
    one_person = read_person(conn, person_id)
    print(one_person)
    
    #update data by ID
    person_id = 2
    person = {
        'firstname': 'Adrian',
        'lastname': 'Ar0',
        'age': 1,
    }
    new_person = update_person(conn, person_id, person)
    print(new_person)
    print(persons)


    #print(persons[0][1])