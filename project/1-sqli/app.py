import psycopg2
from colorama import Fore, Style, init

init(autoreset=True)

def connect_db():
    return psycopg2.connect(
        dbname="demo",
        user="demo",
        password="demo",
        host="localhost",
        port=5432
    )

def options_list():
    print("\n=============================================")
    print("List of examples:")
    print("1 - Vulnerable hidden data")
    print("2 - Vulnerable login")
    print("-2 - Fixed login")
    print("3 - Vulnerable UNION attacks")
    print("4 - Vulnerable Blind SQLi attacks")

def vulnerable_hidden_data():
    conn = connect_db()
    cur = conn.cursor()

    print("-- Display public profiles")
    role = input("Enter role (admin/moderator/user): ")

    query = f"SELECT * FROM profiles WHERE role = '{role}' AND private = FALSE"
    print(Fore.CYAN + "Executing:", query)

    try:
        cur.execute(query)
        result = cur.fetchall()
        if result:
            print(Fore.GREEN + "(+) Profiles:")
            columns = [desc[0] for desc in cur.description]

            for entry in result:
                print(dict(zip(columns, entry)))

        else:
            print(Fore.RED + "(-) Invalid role")
    except Exception as e:
        print("(!) Error:", e)

    cur.close()
    conn.close()    

def vulnerable_hidden_data_with():
    with connect_db() as conn:
        with conn.cursor() as cur:

            print("-- Display public profiles")
            role = input("Enter role (admin/moderator/user): ")

            query = f"SELECT * FROM profiles WHERE role = '{role}' AND private = FALSE"
            print(Fore.CYAN + "Executing:", query)

            try:
                cur.execute(query)
                result = cur.fetchall()
                if result:
                    print(Fore.GREEN + "(+) Profiles:")
                    columns = [desc[0] for desc in cur.description]

                    for entry in result:
                        print(dict(zip(columns, entry)))

                else:
                    print(Fore.RED + "(-) Invalid role")
            except Exception as e:
                print("(!) Error:", e)
    #conn.close()    

def vulnerable_login():
    conn = connect_db()
    cur = conn.cursor()

    print("-- Login:")
    username = input("Username: ")
    password = input("Password: ")

    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(Fore.CYAN + "Executing:", query)

    try:
        cur.execute(query)
        result = cur.fetchone()
        if result:
            columns = [desc[0] for desc in cur.description]

            print(Fore.GREEN + "(+) Login successful:")
            print(dict(zip(columns, result)))
        else:
            print(Fore.RED + "(-) Invalid credentials")
    except Exception as e:
        print("(!) Error:", e)

    cur.close()
    conn.close()

def fixed_login():
    conn = connect_db()
    cur = conn.cursor()

    print("-- Login (PARAMETRIZED QUERY):")
    username = input("Username: ")
    password = input("Password: ")

    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    print(Fore.CYAN + "Executing (safe):", query)

    try:
        cur.execute(query, (username, password))
        result = cur.fetchone()
        if result:
            columns = [desc[0] for desc in cur.description]

            print(Fore.GREEN + "(+) Login successful:")
            print(dict(zip(columns, result)))
        else:
            print(Fore.RED + "(-) Invalid credentials")
    except Exception as e:
        print("(!) Error:", e)

    cur.close()
    conn.close()


def vulnerable_union():
    conn = connect_db()
    cur = conn.cursor()

    print("-- Search users based on username pattern:")
    username = input("Username pattern: ")
    query = f"SELECT id, username, name, surname FROM users WHERE username LIKE '%{username}%'"

    print(Fore.CYAN + "Executing:", query)

    try:
        cur.execute(query)
        result = cur.fetchall()
        if result:
            columns = [desc[0] for desc in cur.description]
            
            print(Fore.GREEN + "(+) Data:")
            for entry in result:
                print(dict(zip(columns, entry)))
        else:
            print(Fore.RED + "(-) No user matches the given pattern")
    except Exception as e:
        print("(!) Error:", e)

    cur.close()
    conn.close()

def fixed_union():
    return

def vulnerable_blind():
    conn = connect_db()
    cur = conn.cursor()

    print("-- Check if user exists:")
    username = input("Username: ")

    query = f"SELECT 1 FROM users WHERE username = '{username}'"
    #print(Fore.CYAN + "Executing:", query)

    try:
        cur.execute(query)
        result = cur.fetchall()
        if result:
            print(Fore.GREEN + "(+) User exists")
        else:
            print(Fore.RED + "(-) User not found")
    except Exception as e:
        print("(!) Error:", e)

    cur.close()
    conn.close()

options = {
    -2: fixed_login,
    1: vulnerable_hidden_data_with,
    2: vulnerable_login,
    3: vulnerable_union,
    4: vulnerable_blind
}

if __name__ == "__main__":
    while True:
        options_list()
        try:
            option = int(input("Choose an option: "))
        except ValueError:
            print("(!) Invalid option")
            continue

        if option in options:
            options[option]()
        else:
            print("(!) Invalid option")