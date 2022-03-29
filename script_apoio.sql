SELECT a.* FROM public.hr_attendance a

SELECT x.* FROM public.hr_employee x 
WHERE name ilike '%Alipio%'


SELECT x.name,a.*,x.* FROM public.hr_attendance a
join public.hr_employee x on a.employee_id = x.id  
WHERE x.name ilike '%Abiga%'


SELECT x.name,a.*,x.* FROM public.hr_attendance a
join public.hr_employee x on a.employee_id = x.id 
where x.id = 12

WHERE x.name ilike '%Alí%'


SELECT a.*,date_part('year',a.create_date) FROM public.hr_attendance a
where date_part('year',a.create_date) = '2022'
and date_part('month',a.create_date) = '01'

SELECT x.name,a.*,x.* FROM public.hr_attendance a
join public.hr_employee x on a.employee_id = x.id 
where date_part('year',a.create_date) = '2022'
and date_part('month',a.create_date) = '01'
and x.id = 12
order by check_in 


SELECT x.name,a.*,x.* FROM public.hr_attendance a
join public.hr_employee x on a.employee_id = x.id 
where date_part('year',a.create_date) = '2022'
and date_part('month',a.create_date) = '01'
and x.id = 12
order by a.id 



--rodando pelo psql -U odoo -d odoo_xxx
psql> \copy (
SELECT x.name,a.check_in ,a.check_out ,a.worked_hours FROM public.hr_attendance a
join public.hr_employee x on a.employee_id = x.id 
where date_part('year',a.create_date) = '2022'
and date_part('month',a.create_date) = '01'
and x.id = 12
order by a.id 
) To '/home/alipio/test.csv' With CSV DELIMITER '|' HEADER;


---  FINAIS  ---------------------------------------------------------------------------

Servidor : 192.168.10.32
base: vision
port: 5432
user: odoo
pass: odoo


SELECT 
x.name	as colaborador,
a.check_in as entrada,
a.check_out as saida,
a.worked_hours as horas
FROM public.hr_attendance a
join public.hr_employee x on a.employee_id = x.id 
where date_part('year',a.create_date) = '2022'
and date_part('month',a.create_date) = '01'
--and x.id = 12
--order by a.id 
order by x."name" ,a.check_in  



--rodando pelo psql -U odoo -d odoo_xxx
psql> \copy (
SELECT 
x.name	as colaborador,
a.check_in as entrada,
a.check_out as saida,
a.worked_hours as horas
FROM public.hr_attendance a
join public.hr_employee x on a.employee_id = x.id 
where date_part('year',a.create_date) = '2022'
and date_part('month',a.create_date) = '01'
--and x.id = 12
--order by a.id 
order by x."name" ,a.check_in  
) To '/home/alipio/00.planilha_horas_odoo/test.csv' With CSV DELIMITER '|' HEADER;




