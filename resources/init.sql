create table if not exists keys (
    public_key TEXT, 
    address TEXT);

create table if not exists transactions (
    type TEXT, 
    sender TEXT, 
    recepient TEXT, 
    hash TEXT, 
    amount INTEGER, 
    fee INTEGER);

create table if not exists unconfirmed_transactions (
    type TEXT, 
    sender TEXT, 
    recepient TEXT, 
    hash TEXT, 
    amount INTEGER, 
    fee INTEGER);

create table if not exists mnemonic_public_key (
    xpub_key TEXT);