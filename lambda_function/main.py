import psycopg2
from flask_restx import Namespace, Resource
from flask import jsonify

api = Namespace("calculate_data", description="")


@api.route("/")
class CalculateData(Resource):
    # Function to calculate metrics (total bookings per destination)
    def get(self):
        # Connect to PostgreSQL database
        conn = psycopg2.connect(
            dbname="travel_data",
            user="postgres",
            password="ramramram",
            host="database-1.c3r4rsuoso6r.ap-south-1.rds.amazonaws.com",
            port="5432",
        )
        cursor = conn.cursor()

        # Query to calculate total bookings per destination
        cursor.execute(
            """
            SELECT
                d.destination,
                SUM(b.total_booking_value) AS total_bookings
            FROM
                destinations d
            JOIN
                bookings b ON d.destination_id = b.destination_id
            GROUP BY
                d.destination_id, d.destination;
            """
        )
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(results)
