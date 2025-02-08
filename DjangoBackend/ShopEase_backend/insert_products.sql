DELETE FROM myapp_product;
DELETE FROM myapp_productcategory;

-- Insert product categories
INSERT INTO myapp_productcategory (name, description, created_at, updated_at) VALUES
    ('Electronics', 'Devices and gadgets', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    ('Clothing', 'Men and Women apparel', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    ('Books', 'Collection of various genres', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    ('Home Appliances', 'Household electronic appliances', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    ('Toys', 'Kids play items and games', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- Insert products
INSERT INTO myapp_product (name, slug, image, description, price, category_id, created_at, updated_at) VALUES
    ('Smartphone', 'smartphone', 'img/smartphone.jpg', 'Latest model smartphone', 699.99, 
        (SELECT id FROM myapp_productcategory WHERE name='Electronics'), CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    ('Laptop', 'laptop', 'img/laptop.jpg', 'High performance laptop', 1299.99, 
        (SELECT id FROM myapp_productcategory WHERE name='Electronics'), CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    ('T-Shirt', 't-shirt', 'img/tshirt.jpg', 'Comfortable cotton t-shirt', 19.99, 
        (SELECT id FROM myapp_productcategory WHERE name='Clothing'), CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    ('Novel', 'novel', 'img/novel.jpg', 'Bestselling fiction novel', 14.99, 
        (SELECT id FROM myapp_productcategory WHERE name='Books'), CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    ('Washing Machine', 'washing-machine', 'img/washing_machine.jpg', 'Front-load washing machine', 499.99, 
        (SELECT id FROM myapp_productcategory WHERE name='Home Appliances'), CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    ('Microwave Oven', 'microwave-oven', 'img/microwave_oven.jpg', 'Compact microwave oven', 199.99, 
        (SELECT id FROM myapp_productcategory WHERE name='Home Appliances'), CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    ('Action Figure', 'action-figure', 'img/action_figure.jpg', 'Superhero action figure', 29.99, 
        (SELECT id FROM myapp_productcategory WHERE name='Toys'), CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    ('Board Game', 'board-game', 'img/board_game.jpg', 'Strategy board game', 39.99, 
        (SELECT id FROM myapp_productcategory WHERE name='Toys'), CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
