CREATE TABLE IF NOT EXISTS Department(
	department_id INT PRIMARY KEY,
	department_name VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS Employee(
	employee_id INT PRIMARY KEY,
	employee_name VARCHAR NOT NULL,
	department_id INT REFERENCES Department(department_id)
);

CREATE TABLE IF NOT EXISTS Boss(
	boss_id INT PRIMARY KEY,
	employee_id INT REFERENCES Employee(employee_id),
	department_id INT REFERENCES Department(department_id)
);