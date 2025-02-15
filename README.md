# Intent_email_generator
This Project checks the user activity and sends an email according to the intention of the user and requirements.

# Intent Database(Please Create the DB for getting the case studies from the company domain for generating refral links and projects of company)

This repository contains the SQL scripts for setting up and inserting dummy data into the `intent_assignment` database using PostgreSQL.

## Database Setup

### 1. Create the Database
```sql
psql -U postgres
CREATE DATABASE intent_assignment;
```

### 2. Connect to the Database
```sql
psql -U postgres -d intent_assignment
```

### 3. Set Password for PostgreSQL User
```sql
ALTER USER postgres WITH PASSWORD '12345';
```

## Table Creation

Create a table named `case_studies` to store case study data.
```sql
CREATE TABLE case_studies (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    category TEXT NOT NULL,
    content TEXT NOT NULL,
    source_url TEXT UNIQUE NOT NULL
);
```

## Insert Dummy Data

Insert some reference data into the `case_studies` table.
```sql
INSERT INTO case_studies (title, description, category, content, source_url) VALUES
('Golang API Development', 'Built a scalable API using Go. This project involved building a high-performance API using Go. Here are some of our related portfolios: https://dribbble.com/mindinventory, https://www.behance.net/mindinventory, https://www.mindinventory.com/all-portfolios.php', 'Golang', 'This project involved building a high-performance API using Go.', 'https://www.mindinventory.com/golang-api-development-new.php'),

('AI Chatbot for Healthcare', 'Developed an AI chatbot for patient interactions. We built a chatbot to assist patients with medical queries using NLP. Here are some of our related projects in the Healthcare & Wellness domain: Airofit - https://airofit.in/, Biped AI - https://biped.ai/, Shoorah - https://shoorah.io/, Biostrap - https://biostrap.com/, Shmoody - https://www.shmoody.com/, Rx Longevity - https://rx-longevity.com/, Spiritual Me - https://spiritualme.com/, HeadHelp - https://www.headhelp.io/', 'AI/ML, Healthcare', 'We built a chatbot to assist patients with medical queries using NLP.', 'https://www.mindinventory.com/healthcare-solutions-new.php');
```

## Update Case Study Descriptions

Update the `description` field with more detailed information.
```sql
UPDATE case_studies SET description = CASE
    WHEN title = 'Golang API Development'
    THEN 'Built a scalable API using Go. Portfolio: dribbble.com/mindinventory, behance.net/mindinventory, mindinventory.com/all-portfolios.php. Healthcare & Wellness Projects: Airofit (airofit.in) - breath training app, Biped AI (biped.ai) - mobility vest for blind, Shoorah (shoorah.io) - mental health app, Biostrap (biostrap.com), Shmoody (shmoody.com) - mood tracker, Rx Longevity (rx-longevity.com) - health optimization, Spiritual Me (spiritualme.com) - meditation app, HeadHelp (headhelp.io) - self care app. All apps available on iOS and Android.'
    WHEN title = 'AI Chatbot for Healthcare'
    THEN 'Developed an AI chatbot for patient interactions. Portfolio: dribbble.com/mindinventory, behance.net/mindinventory, mindinventory.com/all-portfolios.php. Healthcare & Wellness Projects: Airofit (airofit.in) - breath training app, Biped AI (biped.ai) - mobility vest for blind, Shoorah (shoorah.io) - mental health app, Biostrap (biostrap.com), Shmoody (shmoody.com) - mood tracker, Rx Longevity (rx-longevity.com) - health optimization, Spiritual Me (spiritualme.com) - meditation app, HeadHelp (headhelp.io) - self care app. All apps available on iOS and Android.'
    ELSE description
END;
```





## Use Grooq api with llama70b model
I have not pushed the api key along with the code but you can generate for free from this link : https://console.groq.com/keys




## Two ways to run after completing the above setup:

## First:
## Ater downlaoding the Repo
## 1. Run the requirements.txt file (Python version- 3.10)
## 2. Run the main.py file 
## Go to http://127.0.0.1:8000/
## Fill the form and Submit it will generate an email


## Second:

## 1. Go inside the cd Intent_email_generator
## 2. Run docker build -t intent_email_generator .
## 3. Run docker run -p 8000:8000 intent_email_generator

