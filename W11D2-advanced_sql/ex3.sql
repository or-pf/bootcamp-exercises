use employees;
-- Who are the first ten employees (who ever held this title) whose title is or was Assistant Engineer?
select first_name, last_name, from_date from employees inner join titles on employees.emp_no= titles.emp_no
where title= "Assistant Engineer" order by from_date asc limit 10;

-- Who are the second ten employees (11-20, who ever held this title) whose title is or was Senior Engineer?
select first_name, last_name, from_date from employees inner join titles on employees.emp_no= titles.emp_no
where title= "Senior Engineer" order by from_date asc limit 10,10;

-- What are the departments who have the largest amount of engineers (of any kind)?

select dept_name from departments
inner join dept_emp on dept_emp.dept_no = departments.dept_no
inner join titles on titles.emp_no = dept_emp.emp_no
where dept_emp.emp_no in
(select emp_no from titles where title in ("Engineer", "Senior Engineer", "Assistant Engineer"))
group by dept_name
order by count(*) desc;

-- Per department, who is the employee that held the highest salary?
select dept_name, first_name, last_name, max(salary) from salaries 
inner join employees on salaries.emp_no = employees.emp_no
inner join dept_emp on salaries.emp_no= dept_emp.emp_no
inner join departments on departments.dept_no = dept_emp.dept_no
group by dept_name;

-- this is necessary to make sure the salary was paid during the time the employee worked at that department
SELECT dept_name, max(salary) FROM dept_emp as de
-- INNER JOIN departments as d ON de.dept_no = d.dept_no
-- INNER JOIN employees as e ON de.emp_no = e.emp_no
-- INNER JOIN salaries as s ON de.emp_no = s.emp_no and de.from_date < s.from_date and de.to_date > s.to_date
-- GROUP BY dept_name;

