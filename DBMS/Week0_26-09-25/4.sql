update participated set damage_amount=25000 where reg_num='KA053408' and report_num=12;
select * from participated;
select count(distinct driver_id) CNT from participated a, accident b where a.report_num=b.report_num and b.accident_date like "2004-%-%";