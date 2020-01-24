### part 2
import sqlite3
conn = sqlite3.connect('northwind_small.sqlite3')
cur = conn.cursor()
#get table information
'''
tables = cur.execute("""SELECT name FROM sqlite_master WHERE type = 'table' ORDER BY name;""")
conn.commit()
print(tables.fetchall())
'''
#What are the ten most expensive items (per unit price) in the database?
x = cur.execute("""
SELECT ProductName, UnitPrice FROM Product
ORDER BY UnitPrice DESC
LIMIT 10
""")
conn.commit()
print('Top 10 most expensive items:')
print(x.fetchall())

#What is the average age of an employee at the time of their hiring? (Hint: a lot of arithmetic works with dates.)
x = cur.execute("SELECT AVG(HireDate - BirthDate) FROM Employee")
conn.commit()
print('Avg age of employee at time of hiring:')
print(x.fetchall())


#(*Stretch*) How does the average age of employee at hire vary by city?
x = cur.execute("SELECT AVG(HireDate - BirthDate), City FROM Employee GROUP BY City")
conn.commit()
print('Avg age of employee at time of hiring, varying by city:')
print(x.fetchall())

### part 3

#What are the ten most expensive items (per unit price) in the database *and* their suppliers?
x = cur.execute("""
SELECT ProductName, UnitPrice, CompanyName FROM Product
INNER JOIN Supplier ON Supplier.Id = Product.SupplierId
ORDER BY UnitPrice DESC
LIMIT 10
""")
conn.commit()
print('Ten most expensive items and their suppliers:')
print(x.fetchall())

#What is the largest category (by number of unique products in it)?
x = cur.execute("""
SELECT CategoryName 
FROM Product
LEFT JOIN Category ON Category.Id = Product.CategoryId
GROUP BY CategoryId
ORDER BY COUNT(DISTINCT ProductName) DESC
LIMIT 1
""")
conn.commit()
print('The largest cateory with unique products:')
print(x.fetchall())


# (*Stretch*) Who's the employee with the most territories? Use `TerritoryId` (not name, region, or other fields) as the unique identifier for territories.
x = cur.execute("""
SELECT LastName, FirstName FROM Employee
INNER JOIN EmployeeTerritory
ON Employee.Id = EmployeeTerritory.EmployeeId
GROUP BY EmployeeId
ORDER BY COUNT(TerritoryId) DESC
LIMIT 1
""")
conn.commit()
print('The employee with most territories:')
print(x.fetchall())
