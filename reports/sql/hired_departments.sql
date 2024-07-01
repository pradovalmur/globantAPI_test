SELECT 
   d.id,
   d.department,
   count(he.id) as hired 
FROM 
    public.hired_employees AS he
INNER JOIN 
    public.departments AS d ON he.department_id = d.id
INNER JOIN 
    public.jobs AS j ON he.job_id = j.id
WHERE 
    EXTRACT(YEAR FROM TO_TIMESTAMP(he.datetime, 'YYYY-MM-DD"T"HH24:MI:SS"Z"')) = 2021
GROUP BY 
    d.id, d.department
order by 3 desc;