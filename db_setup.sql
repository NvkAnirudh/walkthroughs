create database auth_db;

create table users (
	id serial primary key,
	username varchar(255) unique not null,
	email varchar(255) unique not null,
	password_hash text not null,
	join_date timestamp with time zone not null default current_timestamp, --used to check the time when the user has officially joined the application after verification
	email_verified boolean default FALSE,
	verification_token text,
	last_login timestamp with time zone,
	created_at timestamp with time zone not null default current_timestamp, --used to check when the user has signed up
	updated_at timestamp with time zone not null default current_timestamp
);

