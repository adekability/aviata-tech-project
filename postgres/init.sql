GRANT ALL PRIVILEGES ON DATABASE aviata TO postgres;

CREATE TABLE currency_rates(id SERIAL PRIMARY KEY,
                            created_at timestamp DEFAULT NOW(),
                            updated_at timestamp DEFAULT NOW(),
                            fullname varchar,
                            title varchar,
                            description double precision,
                            date date);
CREATE TABLE search_results(id SERIAL PRIMARY KEY,
                            created_at timestamp DEFAULT NOW(),
                            updated_at timestamp DEFAULT NOW(),
                            search_id varchar,
                            status varchar,
                            items json);
