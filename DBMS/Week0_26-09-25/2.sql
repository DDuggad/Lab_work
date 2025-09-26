use dbms_lab;

insert into accident values(11, "2003-01-01","Mysore Road");
insert into accident values(12,"2004-02-02","South end Circle");
insert into accident values(13,"2003-01-21","Bull temple Road");
insert into accident values(14,"2008-02-17","Mysore Road");
insert into accident values(15,"2004-03-05","Kanakpura Road");

insert into person values("A01", "Richard","Srinivas nagar");
insert into person values("A02","Pradeep","Rajaji nagar");
insert into person values("A03","Smith","Ashok nagar");
insert into person values("A04","Venu","N R Colony");
insert into person values("A05","John","Hanumanth nagar");

insert into car values("KA052250", "Indica",1990);
insert into car values("KA031181","Lancer",1957);
insert into car values("KA095477","Toyota",1998);
insert into car values("KA053408","Honda",2008);
insert into car values("KA041702","Audi",2005);

insert into owns values("A01", "KA052250");
insert into owns values("A02","KA053408");
insert into owns values("A03","KA031181");
insert into owns values("A04","KA095477");
insert into owns values("A05","KA041702");

insert into PARTICIPATED values("A01","KA052250", 11,10000);
insert into PARTICIPATED values("A02","KA053408",12,50000);
insert into PARTICIPATED values("A03","KA095477",13,25000);
insert into PARTICIPATED values("A04","KA031181",14,3000);
insert into PARTICIPATED values("A05","KA041702",15,5000);