# dotenv.load_dotenv()
  charger les variable d'environement
# Database().create_url()
  creer un url pour creer la connection à une base
  de données PostgreSQL à partir des variables d'environement dans le **README.md**
# exctract_air_pollution.main()
  save_hourly_pollution_of_many_to_csv(), pour chaque ville sité dans le Geographic_Data.csv:
  - donne la localisation de cette ville
  - prend l'historique de pollution à partire des coordonnées obtenus
  - ajoute une colone "city_name" pour sauvegarder le nom de la ville visée
  - utilise la connection à la base de données pour inserer les données obtenus dans "pollution_lake"
# transform.main()
  - stocke demographic et geographic dans la base de données
  - prend les pollutions dans le "pollution_lake", ajoute une colonne "aqi" qui sera calculer par une framework python à partir de PM10 dans la pollution