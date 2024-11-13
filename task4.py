!pip install ipython-sql
%load_ext sql

import os
USER = os.environ['POSTGRESQL_USER']
PASSWORD = os.environ['POSTGRESQL_PASSWORD']
POSTGRESQL_HOST = '10.129.0.25'
DBASE_NAME = 'demo'

CONNECT_DATA = 'postgresql://{}:{}@{}/{}'.format(
    USER,
    PASSWORD,
    POSTGRESQL_HOST,
    DBASE_NAME
)

%%sql postgresql:///jovyan
    SELECT * FROM pg_database
    
%%sql postgresql:///jovyan

CREATE TABLE Employees (
    EMPLOYEE_ID INT PRIMARY KEY,
    FIRST_NAME VARCHAR(30),
    LAST_NAME VARCHAR(30),
    HIRE_DATE DATE,
    JOB_ID VARCHAR(20),
    MANAGER_ID INT,
    DEPARTMENT_ID SMALLINT
);

INSERT INTO Employees (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, HIRE_DATE, JOB_ID, MANAGER_ID, DEPARTMENT_ID) VALUES
(100, 'Steven', 'King', '1987-06-17', 'AD_PRES', 0, 90),
(101, 'Neena', 'Kochhar', '1987-06-18', 'AD_VP', 100, 90),
(102, 'Lex', 'DeHaan', '1987-06-19', 'AD_VP', 100, 90),
(103, 'Alexander', 'Hunold', '1987-06-20', 'IT_PROG', 102, 60),
(107, 'Diana', 'Lorentz', '1987-06-24', 'IT_PROG', 103, 60),
(108, 'Nancy', 'Greenberg', '1987-06-25', 'FI_MGR', 101, 100),
(109, 'Daniel', 'Faviet', '1987-06-26', 'FI_ACCOUNT', 108, 100),
(114, 'Den', 'Raphaely', '1987-07-01', 'PU_MAN', 100, 30),
(118, 'Guy', 'Himuro', '1987-07-05', 'PU_CLERK', 114, 30),
(144, 'Peter', 'Vargas', '1987-07-31', 'ST_CLERK', 114, 50),
(145, 'John', 'Russell', '1987-08-01', 'SA_MAN', 100, 80),
(146, 'Karen', 'Partners', '1987-08-02', 'SA_MAN', 100, 80);

%%sql postgresql:///jovyan

SELECT * 
FROM Employees

%%sql postgresql:///jovyan

CREATE TABLE Departments (
    DEPARTMENT_ID SMALLINT PRIMARY KEY,
    DEPARTMENT_NAME VARCHAR(50),
    MANAGER_ID INT
);

INSERT INTO Departments (DEPARTMENT_ID, DEPARTMENT_NAME, MANAGER_ID) VALUES
(10, 'Administration', 200),
(30, 'Purchasing', 114),
(40, 'HumanResources', 203),
(50, 'Shipping', 121),
(60, 'IT', 103),
(70, 'PublicRelations', 204),
(80, 'Sales', 145),
(90, 'Executive', 100),
(100, 'Finance', 108),
(110, 'Accounting', 205);

%%sql postgresql:///jovyan

SELECT * 
FROM Departments

%%sql postgresql:///jovyan
SELECT 
    d.DEPARTMENT_NAME,
    CONCAT(m.FIRST_NAME, ' ', m.LAST_NAME) AS MANAGER_NAME,
    COUNT(e.EMPLOYEE_ID) AS NUMBER_OF_EMPLOYEES
FROM Departments d
LEFT JOIN Employees e ON d.DEPARTMENT_ID = e.DEPARTMENT_ID
LEFT JOIN Employees m ON d.MANAGER_ID = m.EMPLOYEE_ID
GROUP BY d.DEPARTMENT_NAME, m.FIRST_NAME, m.LAST_NAME
ORDER BY d.DEPARTMENT_NAME;
