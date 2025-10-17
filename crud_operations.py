
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root123',
    database='idea_platform'
)
cur = conn.cursor()

def list_ideas_by_status(status):
    query = "SELECT idea_id, idea_title, category, status FROM innovations WHERE status = %s"
    cur.execute(query, (status,))
    for row in cur.fetchall():
        print(row)

def update_status(project_id, new_status):
    cur.execute("CALL update_project_status(%s, %s)", (project_id, new_status))
    conn.commit()
    print(f"Project {project_id} status updated to {new_status}")

if __name__ == "__main__":
    list_ideas_by_status("Submitted")
    update_status("I001", "Approved")
    conn.close()
