# To set up
- Install dependencies:
    ```sh
    pip install -r requirement.txt
    ```
- Add env variable or create .env file:
    ```env
    DB_USERNAME=postgres
    DB_PASSWORD=postgres-password
    DB_NAME=postgres-database
    OPEN_WEATHER_API_KEY=your-api-key 
    ```

# NB
- the migration is automatic, just create the database
- the actual code get the Paris' pollution