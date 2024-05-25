<details>
<summary>1. Introduction </summary>

# Introduction

[https://sqlitebrowser.org/](https://sqlitebrowser.org/)

![image](https://github.com/omeatai/AI-and-Data-Science/assets/32337103/01970cf0-08fa-4879-b5d9-fdde92f5f5e9)
![image](https://github.com/omeatai/AI-and-Data-Science/assets/32337103/4e7a9d84-75e3-470d-b9d4-d0d60d004662)
![image](https://github.com/omeatai/AI-and-Data-Science/assets/32337103/c63b3ca3-6ca5-4db8-847a-d6fe99e49852)
![image](https://github.com/omeatai/AI-and-Data-Science/assets/32337103/732df91d-517d-4806-83ad-87f7520fae5d)
![image](https://github.com/omeatai/AI-and-Data-Science/assets/32337103/f86c2aeb-e487-4a21-addc-855cdc341b6a)
![image](https://github.com/omeatai/AI-and-Data-Science/assets/32337103/d1af7765-51a3-4c96-bf76-8d6731bb1d12)
![image](https://github.com/omeatai/AI-and-Data-Science/assets/32337103/a2b26072-fb01-4f45-b9a1-ba88b6fd28f2)

<img width="1327" alt="image" src="https://github.com/omeatai/AI-and-Data-Science/assets/32337103/41a516b7-c96b-4a36-9988-71f40af9b873">
<img width="1327" alt="image" src="https://github.com/omeatai/AI-and-Data-Science/assets/32337103/d35faea5-4387-4e1a-8d60-2148e8f43638">


# #END

</details>

<details>
<summary>2. SQL Comments </summary>

# SQL Comments

```sql
-- THIS IS A COMMENT

/*
THIS IS A COMMENT
THIS IS ANOTHER COMMENT

*/
```

```sql

/*
CREATED BY: WALTER SHIELDS
CREATE DATE: MM/DD/YYYY
DESCRIPTION: THIS IS THE STRUCTURE OF A BASIC QUERY

*/
```

# #END </details>

<details>
<summary>3. High-level questions for the composition of a Query </summary>

# High-level questions for the composition of a Query: 

- What table within the database are we requesting data from?
- What fields within that table are we interested in?
- Do we want to exclude any data or filter or omit any range or time period? 
- What does our query do?

# #END </details>

<details>
<summary>4. SELECT FIRSTNAME, LASTNAME AND EMAIL FROM CUSTOMER </summary>

# SELECT FIRSTNAME, LASTNAME AND EMAIL FROM CUSTOMER

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: This query displays all customers first names, last names and email addresses
*/

SELECT 
	FirstName, 
	LastName, 
	Email 
FROM 
	Customer
```

<img width="1327" alt="image" src="https://github.com/omeatai/AI-and-Data-Science/assets/32337103/c913434f-0eaf-4069-8f90-765880bcc718">
<img width="1327" alt="image" src="https://github.com/omeatai/AI-and-Data-Science/assets/32337103/01013a4f-539e-41ab-9508-74cb56206f99">

# #END </details>

<details>
<summary>5. SELECT FIRSTNAME, LASTNAME AND EMAIL FROM CUSTOMER with Column Aliases </summary>

# SELECT FIRSTNAME, LASTNAME AND EMAIL FROM CUSTOMER with Column Aliases

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: This query displays all customers first names, last names and email addresses
*/

SELECT 
	FirstName AS [Customer First Name], 
	LastName AS "Customer Last Name", 
	Email AS EMAIL
FROM 
	Customer
```

<img width="1327" alt="image" src="https://github.com/omeatai/AI-and-Data-Science/assets/32337103/ad61bdef-7bbd-4da1-bfeb-7820f95cdca4">

# #END </details>

<details>
<summary>6. Sorting Query Results </summary>

# Sorting Query Results

## Order By Column Descending

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: This query displays all customers first names, last names and email addresses
*/

SELECT 
	FirstName AS [Customer First Name], 
	LastName AS "Customer Last Name", 
	Email AS EMAIL
FROM 
	Customer
ORDER BY
	LastName
DESC	
```

<img width="1283" alt="image" src="https://github.com/omeatai/AI-and-Data-Science/assets/32337103/98e468ec-d0fa-4a9b-88ea-f28b02100528">

## Order by Column Ascending

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: This query displays all customers first names, last names and email addresses
*/

SELECT 
	FirstName AS [Customer First Name], 
	LastName AS "Customer Last Name", 
	Email AS EMAIL
FROM 
	Customer
ORDER BY
	LastName
ASC	
```

<img width="1327" alt="image" src="https://github.com/omeatai/AI-and-Data-Science/assets/32337103/eb077893-57a4-4a2a-b52a-c87e399eb5af">

## Order by Multiple Columns

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: This query displays all customers first names, last names and email addresses
*/

SELECT 
	FirstName AS [Customer First Name], 
	LastName AS "Customer Last Name", 
	Email AS EMAIL
FROM 
	Customer
ORDER BY
	FirstName ASC,	 
	LastName DESC	 
	
```

<img width="1327" alt="image" src="https://github.com/omeatai/AI-and-Data-Science/assets/32337103/538a47f7-8d0e-4f42-8e80-605139f81f40">

# #END </details>

<details>
<summary>7. Limiting Query Results </summary>

# Limiting Query Results

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: This query displays all customers first names, last names and email addresses
*/

SELECT 
	FirstName AS [Customer First Name], 
	LastName AS "Customer Last Name", 
	Email AS EMAIL
FROM 
	Customer
ORDER BY
	FirstName ASC,	 
	LastName DESC	 
LIMIT
	5
```

<img width="1327" alt="image" src="https://github.com/omeatai/AI-and-Data-Science/assets/32337103/d687979f-9bf4-4872-af98-752bb4bbb09b">


# #END </details>

<details>
<summary>8. Filter Data - How many customers purchased two songs at 99 cents each?  </summary>

# Filter Data - How many customers purchased two songs at 99 cents each?

- there are tracks at 99 cents each, which is part of our question.
- two songs purchased at 99 cents each will total to $1.98.
- So let's take a look at our invoice table and if we scroll over to the total, we do see that there are invoices totaling $1.98.

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: This query displays all customers first names, last names and email addresses
*/

SELECT 
	CustomerId,
	InvoiceDate,
	BillingAddress,
	BillingCity,
	Total
FROM 
	Invoice
WHERE 
	Total = 1.98
ORDER BY
	CustomerId ASC
LIMIT
	500

```

<img width="1327" alt="image" src="https://github.com/omeatai/AI-and-Data-Science/assets/32337103/e96f63f7-6886-4057-9188-eefaab757c71">

![image](https://github.com/omeatai/AI-and-Data-Science/assets/32337103/1f168133-944b-419b-adda-d39cdbcc7689)

# #END </details>

<details>
<summary>9. Filter Data - How many invoices exist between $1.98 and $5?  </summary>

# Filter Data - How many invoices exist between $1.98 and $5?

- We would simply have to make an alteration to our WHERE clause.
- We're simply going to include the logical operator between $1.98 and $5.

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: This query displays all customers first names, last names and email addresses
*/

SELECT 
	CustomerId,
	InvoiceDate,
	BillingAddress,
	BillingCity,
	Total
FROM 
	Invoice
WHERE 
	Total BETWEEN 1.98 AND 5.00
ORDER BY
	CustomerId ASC
LIMIT
	500

```

<img width="1327" alt="image" src="https://github.com/omeatai/AI-and-Data-Science/assets/32337103/913089fa-c9c0-4ccf-b6e9-ea09e766ce12">


# #END </details>

<details>
<summary>10. Filter Data - How many invoices do we have that are exactly $1.98 or $3.96?  </summary>

# Filter Data - How many invoices do we have that are exactly $1.98 or $3.96?

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: This query displays all customers first names, last names and email addresses
*/

SELECT 
	CustomerId,
	InvoiceDate,
	BillingAddress,
	BillingCity,
	Total
FROM 
	Invoice
WHERE 
	Total IN (1.98, 3.96)
ORDER BY
	CustomerId ASC
LIMIT
	500

```

<img width="1327" alt="image" src="https://github.com/omeatai/AI-and-Data-Science/assets/32337103/f07b8a9c-43a4-4801-b357-7a71e66e6060">

# #END </details>

<details>
<summary>11. Filter Data - How many invoices were billed to the city of Brussels?  </summary>

# Filter Data - How many invoices were billed to the city of Brussels?

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: This query displays all customers info per query instance
*/

SELECT 
	CustomerId,
	InvoiceDate,
	BillingAddress,
	BillingCity,
	Total
FROM 
	Invoice
WHERE 
	BillingCity = 'Brussels'
ORDER BY
	CustomerId ASC
LIMIT
	500

```

<img width="1327" alt="image" src="https://github.com/omeatai/AI-and-Data-Science/assets/32337103/51529ad4-5e9b-4589-988e-e7a73b4f845e">
<img width="1327" alt="image" src="https://github.com/omeatai/AI-and-Data-Science/assets/32337103/ae17089e-2192-42df-b280-1e54eeecf386">

# #END </details>

<details>
<summary>12. Filter Data - How many invoices were billed to Brussels, Orlando, or Paris?  </summary>

# Filter Data - How many invoices were billed to Brussels, Orlando, or Paris?

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: This query displays all customers info per query instance
*/

SELECT 
	CustomerId,
	InvoiceDate,
	BillingAddress,
	BillingCity,
	Total
FROM 
	Invoice
WHERE 
	BillingCity IN ('Brussels', 'Orlando', 'Paris')
ORDER BY
	CustomerId ASC
LIMIT
	500

```

<img width="1327" alt="image" src="https://github.com/omeatai/AI-and-Data-Science/assets/32337103/32c6b549-c358-4a7c-b4a2-f04a41291cf5">

# #END </details>

<details>
<summary>13. Filter Data - How many invoices were billed in the cities that start with B?  </summary>

# Filter Data - How many invoices were billed in the cities that start with B?

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: This query displays all customers info per query instance
*/

SELECT 
	CustomerId,
	InvoiceDate,
	BillingAddress,
	BillingCity,
	Total
FROM 
	Invoice
WHERE 
	BillingCity LIKE 'B%'
ORDER BY
	CustomerId ASC
LIMIT
	500

```

<img width="1327" alt="image" src="https://github.com/omeatai/AI-and-Data-Science/assets/32337103/92a3eaee-9a17-44a9-a2a9-9bd111216dea">

# #END </details>

<details>
<summary>14. Filter Data - How many invoices were billed in cities that have a B anywhere in its name?  </summary>

# Filter Data - How many invoices were billed in cities that have a B anywhere in its name? 

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: This query displays all customers info per query instance
*/

SELECT 
	CustomerId,
	InvoiceDate,
	BillingAddress,
	BillingCity,
	Total
FROM 
	Invoice
WHERE 
	BillingCity LIKE '%B%'
ORDER BY
	CustomerId ASC
LIMIT
	500

```

<img width="1327" alt="image" src="https://github.com/omeatai/AI-and-Data-Science/assets/32337103/3137beb5-1d6f-4797-b126-1bd0c6b2fdef">

# #END </details>

<details>
<summary>15. Filter Data - How many invoices were billed on May 22, 2010 (2010-05-22 00:00:00)?  </summary>

# Filter Data - How many invoices were billed on May 22, 2010 (2010-05-22 00:00:00)? 

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: This query displays all customers info per query instance
*/

SELECT 
	CustomerId,
	InvoiceDate,
	BillingAddress,
	BillingCity,
	Total
FROM 
	Invoice
WHERE 
	Date(InvoiceDate) =  '2010-05-22'
	-- DateTime(InvoiceDate) =  '2010-05-22 00:00:00'
	-- InvoiceDate = '2010-05-22 00:00:00'
ORDER BY
	CustomerId ASC
LIMIT
	500

```

<img width="1327" alt="image" src="https://github.com/omeatai/AI-and-Data-Science/assets/32337103/2ded905e-dea9-43e3-aaeb-b48590fe4b21">
<img width="1327" alt="image" src="https://github.com/omeatai/AI-and-Data-Science/assets/32337103/fcd07f2a-1179-4c00-b470-ebd0b846cc37">

# #END </details>

<details>
<summary>16. Filter Data - How many invoices were billed after 2010-05-22 and have a total of less than $3?  </summary>

# Filter Data - How many invoices were billed after 2010-05-22 and have a total of less than $3?

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: This query displays all customers info per query instance
*/

SELECT 
	CustomerId,
	InvoiceDate,
	BillingAddress,
	BillingCity,
	Total
FROM 
	Invoice
WHERE 
	Date(InvoiceDate) >  '2010-05-22' AND Total < 3.00
ORDER BY
	InvoiceDate ASC
LIMIT
	500

```

<img width="1327" alt="image" src="https://github.com/omeatai/AI-and-Data-Science/assets/32337103/a1089361-3f6b-49c5-a460-b963f8e5cb74">

# #END </details>

<details>
<summary>17. Filter Data - How many invoices whose billing city starts with P or the billing city starts with D?  </summary>

# Filter Data - How many invoices whose billing city starts with P or the billing city starts with D? 

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: This query displays all customers info per query instance
*/

SELECT 
	CustomerId,
	InvoiceDate,
	BillingAddress,
	BillingCity,
	Total
FROM 
	Invoice
WHERE 
	BillingCity LIKE  'P%'  OR BillingCity LIKE 'D%'
ORDER BY
	InvoiceDate ASC
LIMIT
	500

```

<img width="1327" alt="image" src="https://github.com/omeatai/AI-and-Data-Science/assets/32337103/851eb6a4-1661-4981-9628-305c9ba4bb5d">

# #END </details>

<details>
<summary>18. Filter Data - How many invoices are greater than $1.98 from any cities whose names start with P or D?  </summary>

# Filter Data - How many invoices are greater than $1.98 from any cities whose names start with P or D?

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: This query displays all customers info per query instance
*/

SELECT 
	CustomerId,
	InvoiceDate,
	BillingAddress,
	BillingCity,
	Total
FROM 
	Invoice
WHERE 
	Total > 1.98 AND (BillingCity LIKE 'P%' OR BillingCity LIKE 'D%')
ORDER BY
	InvoiceDate ASC
LIMIT
	500

```

<img width="1327" alt="image" src="https://github.com/omeatai/AI-and-Data-Science/assets/32337103/37b8079d-1224-4147-b7cb-a8d8d5343a76">

# #END </details>

<details>
<summary>19. Filter Data - Using IF THEN Logic with CASE  </summary>

# Filter Data - Using IF THEN Logic with CASE

## WSDA Music Sales Goal: 

- They want as many customers as possible to spend between $7.00 and $15.00. 

## Sales Categories:

- Baseline Purchase - Between $0.99 and $1.99
- Low Purchase- Between $2.00 and $6.99
- Target Purchase Between $7.00 and $15.00
- Top Performer- Above $15.00

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: This query displays all customers info per query instance
*/

SELECT 
	CustomerId,
	InvoiceDate,
	BillingAddress,
	BillingCity,
	Total
FROM 
	Invoice
WHERE 
	Total > 1.98 AND (BillingCity LIKE 'P%' OR BillingCity LIKE 'D%')
ORDER BY
	InvoiceDate ASC
LIMIT
	500

```

# #END </details>

<details>
<summary>+LinkedIn - SQL Essential Training </summary>

## Install venv

```sql

```

## Install venv

```sql

```

# #END

</details>