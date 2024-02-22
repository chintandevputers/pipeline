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
            dbname="your_db",
            user="your_user",
            password="your_password",
            host="host_url",
            port="your_port",
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
