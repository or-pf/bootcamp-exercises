use employees;
 -- How many male employees and how many female employees have worked in the company (single query)?
select count(gender), gender from employees group by gender;
-- How many different titles are there in the company?
select count(distinct title) from titles;
-- What are the names and titles of the employees who got hired in 1993?
select * from employees where hire_date >= "1993-01-01" and hire_date <= "1993-12-31";
-- Who are the ten employees whose title is or was Staff and have the lowest salary?-- 
select first_name, last_name, title, salary from employees inner join titles on employees.emp_no=titles.emp_no inner join salaries on employees.emp_no=salaries.emp_no where title= "staff" limit 10;
-- What is the average salary per title? Order the results from highest to lowest.
select title, avg(salary) from salaries inner join titles on salaries.emp_no=titles.emp_no group by title order by avg(salary) desc;