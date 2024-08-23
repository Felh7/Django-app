-- Create a new role
CREATE ROLE djangouser WITH PASSWORD 'greatpass' LOGIN;

-- Create a new database
ALTER DATABASE djangodb OWNER TO djangouser;