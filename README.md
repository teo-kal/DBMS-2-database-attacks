# DBMS-2-database-attacks
[MSc curriculum] Database Management Systems project on database attacks: SQL Injection, NoSQL Injection, and Timing Attacks

## Structure
- `project/` - Contains SQLi and NoSQLi subfolders with mini playgrounds
- `presentation/` - .pptx and relevant files
- `documentation/` - .docx and relevant files

## Project-specific info
### 1. `1-sqli`
- Docker + Database init files: `docker-compose.yml`, `init.sql`
- Example payloads: `payloads.txt`

#### Running the Playground
1. Create the virtual environment within the `project` folder. It will be used for both projects
```bash
python3 -m venv venv
pip install -r ./1-sqli/requirements.txt
pip install -r ./2-nosqli/requirements.txt
```
2. `cd` to specific project folder (either `1-sqli` or `2-nosqli`)
3. `docker compose up -d` or `docker-compose up -d`, depending on docker version
4. Activate venv
`source ../venv/bin/activate/`
5. Run app: `python app.py`

**NOTE:**
- Use this if you modify the database init file (`init.sql`) to reload the database:
```bash
docker-compose down
docker-compose down -v
docker-compose up -d
```

### 2. `2-nosqli`
- Server: `server.js`

#### Running the Playground
1. Start MongoDB: `docker run -d -p 27017:27017 --name mongodb-demo mongo:latest`
2. Install dependencies: `npm install`
3. Run the server: `node server.js`
4. Navigate to http://localhost:3000
