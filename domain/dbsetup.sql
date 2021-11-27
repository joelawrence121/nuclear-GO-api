create schema if not exists nuclear;
use nuclear;

create table nuclear.Item
(
    id          int auto_increment,
    name        varchar(256) null,
    description int          null
);


