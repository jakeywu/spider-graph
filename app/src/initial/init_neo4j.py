from neo4j import GraphDatabase

# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
URI = "neo4j+s://5c370243.databases.neo4j.io"
AUTH = ("neo4j", "iWpYpGnwC20l_YAKVe9OwQ85-mXh7EOEyfdj4TPXy28")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()
