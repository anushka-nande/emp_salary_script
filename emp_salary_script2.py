import mysql.connector
from faker import Faker
import random

# ---------- Database Connection Settings ----------
DB_HOST = "localhost"
DB_USER = "root"  # Replace with your MySQL username
DB_PASSWORD = "Anushka@12"  # Replace with your MySQL password
DB_NAME = "Company"
# --------------------------------------------------

fake = Faker()

# Connect to MySQL
conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
cursor = conn.cursor()

# Ask user how many employees to create
num_employees = int(input("How many employees do you want to create? ➤ "))
salary_entries_per_emp = int(input("How many salary entries per employee? ➤ "))

for _ in range(num_employees):
    name = fake.name()
    position = fake.job()

    # Insert employee
    cursor.execute(
        "INSERT INTO employee (name, position) VALUES (%s, %s)",
        (name, position)
    )
    emp_id = cursor.lastrowid
    print(f"\n👤 Employee created: {name} | Position: {position} | ID: {emp_id}")

    # Insert salary entries
    for i in range(salary_entries_per_emp):
        salary_amount = random.randint(20000, 150000)
        cursor.execute(
            "INSERT INTO salary (emp_id, amount) VALUES (%s, %s)",
            (emp_id, salary_amount)
        )
        print(f"   💰 Salary {i+1}: ₹{salary_amount}")

# Finalize
conn.commit()
conn.close()
print("\n✅ All employee and salary data inserted successfully!")
