Use test_db;

CREATE TABLE `discs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `brand` varchar(45) NOT NULL,
  `model` varchar(45) NOT NULL,
  `style` varchar(45) NOT NULL,
  `price` decimal(4,2) NOT NULL,
  `color` varchar(45) NOT NULL,
  `img` varchar(45) NOT NULL,
  `img2` varchar(45) NOT NULL,
  `descr` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
);


INSERT INTO discs (brand, model, style, price, color, img, img2, descr) VALUES ('Dynamic Discs', 'Judge Prime', 'Putter', '9.99', 'Pink', 'p1.jpg', 'p1a.jpg', 'Designed by Dynamic Discs for straight short range putting'),
('Dynamic Discs', 'Judge Prime', 'Putter', '9.99', 'Blue', 'p2.jpg', 'p2a.jpg', 'Designed by Dynamic Discs for short range putting'),
('Disc Mania', 'Pro Putter P2', 'Putter', '11.99', 'orange', 'p3.jpg','p3a.jpg', 'Designed by Disc Mania for short range putting when a stronger fade is necessary'),
('Volt', 'Electron', 'Driver', '9.99', 'Purple', 'd1.jpg', 'd1a.jpg', 'Designed by Volt for driving under 400ft'),
('Innova', 'Leopard 3', 'Driver', '9.99', 'Red', 'd2.jpg', 'd2a.jpg','Designed by Innova for hooking drives under 400ft'),
('Innova', 'Wraith', 'Driver', '9.99', 'Red', 'd3.jpg', 'd3a.jpg','Designed by Innova for max range drives'),
('Innova', 'StarGator', 'Midrange', '9.99', 'Orange', 'm1.jpg', 'm1a.jpg','Designed by Innova for midrange drives that require an overstable approach'),
('Innova', 'Roc', 'Midrange', '9.99', 'Purple', 'm2.jpg', 'm2a.jpg','Designed by Innova for fading midrange drives'),
('Innova', 'Shark', 'Midrange', '9.99', 'Red', 'm3.jpg', 'm3a.jpg', 'Designed by Innova for a straightforward midrange approach'),
('Latitude', 'Fuse Opto', 'Midrange', '9.99', 'Yellow', 'm4.jpg', 'm4a.jpg', 'Designed by Latitude 64 for a stable midrange approach'),
('Innova', 'Aviar', 'Hybrid', '9.99', 'Blue', 'h1.jpg', 'h1a.jpg', 'Designed by Innova for longer putts'),
('Innova', 'Aviar', 'Hybrid', '9.99', 'Yellow', 'h6.jpg', 'h6a.jpg','Designed by Innova for longer putts that require a fade'),
('Innova', 'XT Nova', 'Hybrid', '9.99', 'Purple', 'h3.jpg', 'h3a.jpg','Designed by Innova for faster straighter putting');


