use imdb;
-- Which films Kevin Bacon participated in? 
select title from movies 
inner join cast on movies.id= cast.movie_id 
inner join actors on cast.actor_id= actors.id 
where full_name = "Kevin Bacon";

-- Which actors have participated in a film with Kevin Bacon?
select distinct full_name from actors 
join cast on cast.actor_id= actors.id
join movies on movies.id= cast.movie_id 
where movies.title in (select title from movies 
inner join cast on movies.id= cast.movie_id 
inner join actors on cast.actor_id= actors.id
where full_name= "Kevin Bacon") and full_name <> "Kevin Bacon";

 -- Which actor has the highest average wage? Don’t forget - the column salary is within the cast table
 
select full_name from actors join cast on cast.actor_id = actors.id
where actors.id = (select actor_id from cast group by actor_id order by avg(salary) desc limit 1);

-- How many actors participated in the film “Aliens”?
select count(*) from cast join movies on cast.movie_id= movies.id 
where movie_id= (select id from movies where title= "aliens");




