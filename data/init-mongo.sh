echo "Initializing MongoDB with data..."


mongosh --host mongodb -u "$MONGODB_USERNAME" -p "$MONGODB_PASSWORD" --authenticationDatabase admin <<EOF
use admin
db.auth("$MONGODB_USERNAME", "$MONGODB_PASSWORD")
EOF

mongosh --host mongodb -u "$MONGODB_USERNAME" -p "$MONGODB_PASSWORD" --authenticationDatabase admin <<EOF
db.auth("$MONGODB_USERNAME", "$MONGODB_PASSWORD")
use dofusdb
EOF

if mongosh --host mongodb -u "$MONGODB_USERNAME" -p "$MONGODB_PASSWORD" --authenticationDatabase admin --quiet --eval "db.getMongo().getDBNames().includes('$MONGODB_DATABASE')" | grep -q true; then
    echo "Database '$MONGODB_DATABASE' already exists. Skipping initialization."
    exit 0
fi

for file in /docker-entrypoint-initdb.d/*.json; do
    collection=$(basename "$file" .json)
    echo "Importing data from file: $file"
    echo "Importing data into collection: $collection"
    mongoimport --host mongodb --db dofusdb --collection "$collection" --type json --file "$file" --jsonArray --username "$MONGODB_USERNAME" --password "$MONGODB_PASSWORD" --authenticationDatabase admin
done