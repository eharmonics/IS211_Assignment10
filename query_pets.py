import sqlite3 as lite


conn = lite.connect('pets.sqlite')

c = conn.cursor()

my_id = 0

while my_id != -1:    
    my_id = int(input("Enter a person's ID number: "))

    c.execute("SELECT first_name, last_name, age FROM person WHERE id = ?", (my_id,))

    row = c.fetchone()

    if (row):
        print("=====================================")
        print("========== Person Details ===========\n")
        print("Person: {} {} is {} years old".format(row[0], row[1], row[2]))

        # Select pet id from person_pet table where person id is my_id and then select pet name, breed, age from pet table where pet id is pet id
        c.execute("SELECT pet.name, pet.breed, pet.age FROM pet INNER JOIN person_pet ON pet.id = person_pet.pet_id WHERE person_pet.person_id = ?", (my_id,))
        pet_rows = c.fetchall()
        print("=====================================")
        print("========== Pet's  Details ===========\n")
        for pet_row in pet_rows:
            print("{} owned {}, a {}, that was {} years old".format(row[0], pet_row[0], pet_row[1], pet_row[2]))

    else:
        print("No person with that ID number exists.")
    

