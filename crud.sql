create schema qrio;
create user admin with password 'admin';
alter user admin with superuser;

drop table person;

create table person (
	id SERIAL primary key,
	firstname VARCHAR(100) not null,
	lastname VARCHAR(100) not null,
	age INT,
	active bool default true
)


-- CREATE
insert into person (firstname, lastname, age)
values ('gelo', 'aguinaldo', 22);


-- READ
select * from person;


-- UPDATE
update person
set AGE = 23
where id = 1;

-- DELETE
delete from person where id = 3;