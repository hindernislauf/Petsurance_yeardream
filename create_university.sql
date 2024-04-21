drop table inst_dept;
drop table instructor;
drop table department;

create table department
	(ID		int, 
     dept_name varchar(10),
	 building		varchar(15),
	 budget		        numeric(12,2) check (budget > 0),
	 primary key (ID)
	);

create table instructor
	(ID			int, 
	 name			varchar(20) not null, 
	 dept_id		int, 
	 salary			numeric(8,2) check (salary > 29000),
	 primary key (ID),
	 foreign key (dept_id) references department (ID)
		on delete set null
	);
        
create table inst_dept
	(i_id INT,
     d_id INT,
     semester varchar(8),
     primary key (i_id, d_id, semester),
     foreign key (i_id) references instructor (ID) on delete cascade,
     foreign key (d_id) references department (ID) on delete cascade)