# To set up
- Use Python 3.11
- Create venv
  - for Windows
    ```shell
    python -m venv venv
    venv\Scripts\activate
    ```
  - for Linux and macOS
    ```shell
    python3 -m venv venv
    source venv/bin/activate
    ```
- Install dependencies:
  - for Windows
      ```sh
      pip install -r requirement.txt
      ```
  - for Linux and macOS
      ```sh
      pip3 install -r requirement.txt
      ```
- Add env variable or create .env file:
  - required
      ```env
      DB_PASSWORD=postgres-password
      OPEN_WEATHER_API_KEY=your-api-key 
      ```
  - optional
      ```env
      DB_USERNAME=postgres
      DB_HOST=localhost
      DB_NAME=postgres-database
      RANGE_START=2024-08-20
      RANGE_END=2024-08-28
      ```
    ## Nb: specify **RANGE_START** and **RANGE_END** to set a range of date to fetch data with the format: **HH-mm-dd**
- Run the code:
  - for Windows
      ```sh
      python main
      ```
  - for Linux and macOS
      ```sh
      python3 main
      ```

# NB
- the migration is automatic, just create the database
- the actual code get pollution of Paris and London 

# To use with airflow
- create folder **/weather** in **/dags**
- create **__init__.py** in **/dags/weather** folder
- copy **exctract_air_pollution.py**, **transform.py** and **utils.py** to **/dags/weather**