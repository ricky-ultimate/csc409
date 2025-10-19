### Data Recap (Table 1)

| MatricNo | Name          | Department           | CGPA |
| -------- | ------------- | -------------------- | ---- |
| 011      | Tolu Fabiyi   | Software Engineering | 3.8  |
| 012      | Ruth Oluwa    | IT                   | 4.5  |
| 013      | David Chuks   | Computer Science     | 3.5  |
| 014      | Hanna Abiodun | Software Engineering | 3.9  |

---

### Step 1 — Create the Database

1. **Open Microsoft Access**

   * Choose **“Blank database”**
   * Name it: `StudentRecords.accdb`
   * Click **Create**

2. **Create Table**

   * In the main window, click **Table Design**

   * Add these fields:

     | Field Name | Data Type       |
     | ---------- | --------------- |
     | MatricNo   | Short Text      |
     | Name       | Short Text      |
     | Department | Short Text      |
     | CGPA       | Number (Double) |

   * **Set MatricNo as Primary Key**
     → Right-click the row header beside *MatricNo* → **Primary Key**

3. **Save the table**

   * Name it `Students`

---

### Step 2 — Enter Records

1. Double-click the `Students` table to open **Datasheet View**
2. Enter the records from Table 1
3. Press **Ctrl+S** to save

---

### Step 3 — Run Queries

#### Retrieve all students

* Go to **Create → Query Design → SQL View**
* Enter:

```sql
SELECT * FROM Students;
```

* Run (red exclamation mark ▶)

---

#### Search for a student by matric number

```sql
SELECT * FROM Students
WHERE MatricNo = '012';
```

---

#### Find students with GPA > 3.5

```sql
SELECT Name, CGPA
FROM Students
WHERE CGPA > 3.5;
```