-- Initial DDLs for the Tables
CREATE TABLE fct.fct_user (
    id SERIAL PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    password_hash VARCHAR(256) NOT NULL,
    is_admin BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE fct.cart (
    id SERIAL PRIMARY KEY,
    total VARCHAR NOT NULL,
    is_purchased BOOLEAN NOT NULL DEFAULT FALSE,
    is_abandoned BOOLEAN NOT NULL DEFAULT FALSE,
    is_active BOOLEAN NOT NULL DEFAULT FALSE,
    user_id INTEGER NOT NULL,
    CONSTRAINT fk_cart_user FOREIGN KEY (user_id) REFERENCES fct.fct_user(id)
);


CREATE TABLE fct.chain (
    id SERIAL PRIMARY KEY,
    type VARCHAR NOT NULL,
    price DECIMAL(10,2) NOT NULL DEFAULT 0,
    in_stock BOOLEAN NOT NULL DEFAULT FALSE,
    stock INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE fct.frame_finish (
    id SERIAL PRIMARY KEY,
    type VARCHAR NOT NULL,
    price DECIMAL(10,2) NOT NULL DEFAULT 0,
    stock INTEGER NOT NULL DEFAULT 0,
    in_stock BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE fct.frame_type (
    id SERIAL PRIMARY KEY,
    type VARCHAR NOT NULL,
    price DECIMAL(10,2) NOT NULL DEFAULT 0,
    stock INTEGER NOT NULL DEFAULT 0,
    in_stock BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE fct.frame (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    frame_finish_id INTEGER NOT NULL,
    frame_type_id INTEGER NOT NULL,
    price DECIMAL(10,2) NOT NULL DEFAULT 0,
    stock INTEGER NOT NULL DEFAULT 0,
    in_stock BOOLEAN NOT NULL DEFAULT FALSE,
    CONSTRAINT fk_frame_finish FOREIGN KEY (frame_finish_id) REFERENCES fct.frame_finish(id),
    CONSTRAINT fk_frame_type FOREIGN KEY (frame_type_id) REFERENCES fct.frame_type(id)
);

CREATE TABLE fct.product (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    product_type_id INTEGER NOT NULL,
    stock INTEGER NOT NULL DEFAULT 0,
    price DECIMAL(10,2) NOT NULL DEFAULT 0,
    in_stock BOOLEAN NOT NULL DEFAULT FALSE,
    CONSTRAINT fk_product_type FOREIGN KEY (product_type_id) REFERENCES fct.product_type(id)
);

CREATE TABLE fct.product_cart (
    id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL,
    cart_id INTEGER NOT NULL,
    amount INTEGER NOT NULL DEFAULT 0,
    CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES fct.product(id),
    CONSTRAINT fk_cart FOREIGN KEY (cart_id) REFERENCES fct.cart(id)
);

CREATE TABLE fct.product_type (
    id SERIAL PRIMARY KEY,
    type VARCHAR NOT NULL
);

CREATE TABLE fct.rim (
    id SERIAL PRIMARY KEY,
    color VARCHAR NOT NULL,
    price DECIMAL(10,2) NOT NULL DEFAULT 0,
    in_stock BOOLEAN NOT NULL DEFAULT FALSE,
    stock INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE fct.wheel (
    id SERIAL PRIMARY KEY,
    type VARCHAR NOT NULL,
    price DECIMAL(10,2) NOT NULL DEFAULT 0,
    in_stock BOOLEAN NOT NULL DEFAULT FALSE,
    stock INTEGER NOT NULL DEFAULT 0
);


CREATE TABLE fct.bike (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    frame_id INT NOT NULL,
    wheel_id INT NOT NULL,
    rim_id INT NOT NULL,
    chain_id INT NOT NULL,
    product_id INT NOT NULL,
    price FLOAT NOT NULL DEFAULT 0,
    stock INT NOT NULL DEFAULT 0,
    in_stock BOOLEAN NOT NULL DEFAULT FALSE,
    is_created_by_admin BOOLEAN NOT NULL DEFAULT TRUE,
    is_created_by_user BOOLEAN NOT NULL DEFAULT FALSE,
    creator_id INT NOT NULL,
    FOREIGN KEY (frame_id) REFERENCES fct.frame(id),
    FOREIGN KEY (wheel_id) REFERENCES fct.wheel(id),
    FOREIGN KEY (rim_id) REFERENCES fct.rim(id),
    FOREIGN KEY (chain_id) REFERENCES fct.chain(id),
    FOREIGN KEY (product_id) REFERENCES fct.product(id),
    FOREIGN KEY (creator_id) REFERENCES fct.fct_user(id)
);


CREATE TABLE fct.valid_combinations (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    frame_id INTEGER NOT NULL,
    wheel_id INTEGER NOT NULL,
    rim_id INTEGER NOT NULL,
    chain_id INTEGER NOT NULL,
    FOREIGN KEY (frame_id) REFERENCES fct.frame(id),
    FOREIGN KEY (wheel_id) REFERENCES fct.wheel(id),
    FOREIGN KEY (rim_id) REFERENCES fct.rim(id),
    FOREIGN KEY (chain_id) REFERENCES fct.chain(id)
);
