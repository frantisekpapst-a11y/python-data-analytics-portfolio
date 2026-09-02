SELECT *
FROM orders;

SELECT
    order_id,
    product,
    quantity,
    unit_price
FROM orders;

SELECT
    order_id,
    product,
    quantity,
    unit_price
FROM orders
WHERE quantity >= 2;

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    region TEXT
);

INSERT INTO customers (
    customer_id,
    customer_name,
    region
)
VALUES
    (101, 'Jan Novak', 'Praha'),
    (102, 'Eva Cerna', 'Brno'),
    (103, 'Petr Maly', 'Ostrava');

SELECT *
FROM customers;

SELECT
    o.order_id,
    o.product,
    o.quantity,
    o.unit_price,
    c.customer_name,
    c.region
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id;