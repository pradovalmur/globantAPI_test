SELECT 
    d.department,
    j.job,
    SUM(CASE WHEN EXTRACT(QUARTER FROM TO_TIMESTAMP(he.datetime, 'YYYY-MM-DD"T"HH24:MI:SS"Z"')) = 1 THEN 1 ELSE 0 END) AS Q1,
    SUM(CASE WHEN EXTRACT(QUARTER FROM TO_TIMESTAMP(he.datetime, 'YYYY-MM-DD"T"HH24:MI:SS"Z"')) = 2 THEN 1 ELSE 0 END) AS Q2,
    SUM(CASE WHEN EXTRACT(QUARTER FROM TO_TIMESTAMP(he.datetime, 'YYYY-MM-DD"T"HH24:MI:SS"Z"')) = 3 THEN 1 ELSE 0 END) AS Q3,
    SUM(CASE WHEN EXTRACT(QUARTER FROM TO_TIMESTAMP(he.datetime, 'YYYY-MM-DD"T"HH24:MI:SS"Z"')) = 4 THEN 1 ELSE 0 END) AS Q4
FROM 
    public.hired_employees AS he
INNER JOIN 
    public.departments AS d ON he.department_id = d.id
INNER JOIN 
    public.jobs AS j ON he.job_id = j.id
WHERE 
    EXTRACT(YEAR FROM TO_TIMESTAMP(he.datetime, 'YYYY-MM-DD"T"HH24:MI:SS"Z"')) = 2021
GROUP BY 
    d.department, j.job;