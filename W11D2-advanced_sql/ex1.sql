create database programs;
use programs;
create table participant(
participantID int,
first_name varchar(25) not null,
last_name varchar(25) not null,
country varchar(15),
gender enum ("f", "m", "none", "both"),
english_level int default 5,
isIsraeli boolean,
primary key (participantID)
);
create table payment (
paymentID int,
participantID int not null,
sum int,
payment_date date,
payment_method enum ("paypal", "cash"),
primary key (paymentID),
foreign key (participantID) references participant (participantID)
);
insert into participant 
values (110, "yael", "cohen", "usa", "f", 10, false),
(111, "moti", "levi", "israel", "m", 3, true);
insert into payment
values (1, 110, 250, 01/12/2015, "cash"),
(2, 111, 5000, 08/08/1975, "paypal");
insert into payment
values (3, 113, 250, 01/12/2015, "cash");



