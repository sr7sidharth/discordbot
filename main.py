#contains the main function to run the bot
import discord, os
from dotenv import load_dotenv
import mysql.connector

if __name__ == "__main__":
    # Get bot token and database credentials
    load_dotenv()
    token = os.getenv("discord_token")
    username = os.getenv("user")
    password = os.getenv("password"),
    database_name = os.getenv("database_name")

    # Set up database
    db = mysql.connector.connect(
        host = "localhost",
        user = username,
        password = password,
    )

    cursor = db.cursor()

    query_string = "CREATE DATABASE IF NOT EXISTS " + database_name

    cursor.execute(query_string)
    db.commit()

    # Create tables

    #cursor.execute('CREATE TABLE IF NOT EXISTS HOT_TOYS_SCRAPER')

    cursor.close()
    db.close()

    # Connect to database 
    db = mysql.connector.connect(
        host = "localhost",
        user = username,
        password = password,
        database = database_name
    )

    cursor = db.cursor()

    # Activate bot
    client = Discord.Client()
    client.run(token)
