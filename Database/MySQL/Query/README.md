# Query 
쿼리쿼리 👍

<details>
<summary>Row가 많은 FK 찾기</summary>

![](.README_images/76a58505.png)
```sql
SELECT 
    customer_number
FROM 
    Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC 
LIMIT 1
```
</details>


<details>
<summary>Pk별로 오래된 날짜 가져오기 ✔Min()</summary>

![](.README_images/925529ff.png)
```sql
SELECT 
    player_id, MIN(event_date) AS first_login
FROM
    Activity
GROUP BY player_id
```
</details>


<details>
<summary>하루 전날보다 큰 값을 가진 Row 가져오기 ✔Datediff()</summary>

![](.README_images/f0b79eb0.png)
```sql
SELECT
    id
FROM 
    Weather W1, Weather W2
WHERE 
    DATE_DIFF(W2.recordDate, W1.recordDate) == 1
    AND W2.temperature > W1.temperature 
```
</details>

<details>
<summary>전형적인 ✔Left Outer Join</summary>

![](.README_images/0ff3e2c2.png)
```sql
SELECT
    name AS Customers
FROM
    Customers C LEFT JOIN Orders O 
        ON C.id = O.customerId
WHERE O.id = null
```
</details>

<details>
<summary>전형적인 ✔Group By ✔Having Count</summary>

![](.README_images/2b31cb86.png)
```sql
SELECT 
    class
FROM 
     Courses
GROUP BY class having count(*) >= 5
```
</details>


<details>
<summary>두번째로 높은값 찾기 ✔Distinct ✔Limit</summary>

![](.README_images/dfe5f50e.png)
```sql
SELECT 
   IFNULL(
        (SELECT DISTINCT salary FROM Employee ORDER BY salary desc LIMIT 1, 1)
        , null
   ) as SecondHighestSalary 
```
</details>


<details>
<summary>N번째로 높은값 찾기 ✔MySQL Function ✔Distinct ✔Limit</summary>

![](.README_images/3372926b.png)
![](.README_images/2c1ebf17.png)
```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN

DECLARE M INT;
SET M=N-1;

  RETURN (
      # Write your MySQL query statement below.
      SELECT IFNULL(
        (SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT M, 1)
        , null
      )
  );
END
```
</details>

<details>
<summary>Row 값 Rank 구하기 ✔Rank Over</summary>

![](.README_images/79977b95.png)
```sql
SELECT 
    score
    , DENSE_RANK() OVER(order by score desc) as 'rank'
FROM
    Scores 
ORDER BY score desc
```

![](.README_images/b76630cf.png)
![](.README_images/2724ef5f.png)
</details>



<details>
<summary>Row 값 Rank 구하기 ✔Cross Join ✔Max</summary>

![](.README_images/ac4c78aa.png)
```sql
SELECT 
	D.name as Department,
    E.name as Employee,
	E.salary as Salary
FROM 
	Employee E, Department D,
	(SELECT
		departmentId, MAX(Salary) as maxSalary
	FROM
		Employee
	GROUP BY DepartmentId) A
WHERE 
	E.departmentId = A.departmentId
    AND D.id= A.departmentId
    AND E.salary = A.maxSalary
    
```
</details>