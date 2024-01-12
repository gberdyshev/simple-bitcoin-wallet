create table if not exists keys (
    public_key TEXT, 
    address TEXT);

create table if not exists transactions (
    type TEXT, 
    sender TEXT, 
    recipient TEXT, 
    hash TEXT, 
    amount INTEGER, 
    fee INTEGER);

create table if not exists contacts (
    address TEXT,
    name TEXT

)