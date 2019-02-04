import datetime
from api.models.database import DatabaseConnection


class Record:

    """
    This class uses the database to store data persistently
    """
    db = DatabaseConnection()

    def __init__(
        self, record_type=None, record_title=None, 
        record_geolocation=None, status=None, 
        user_id=None, record_no=None,
        body=None, upload=None
        ):
        self.record_no = None
        self.user_id = user_id
        self.record_title = record_title
        self.record_geolocation = record_geolocation
        self.record_type = record_type
        self.status = 'Pending'
        self.body = None
        self.upload = None

    def post_record(
                    self, record_type=None, record_title=None, 
                    record_geolocation=None, user_id=None,
                    body=None, upload=None
                    ):
        """
        post new intervention record
        """
        record_placed = self.db.post_record(
             record_geolocation, record_title,
             record_type, user_id,
             body, upload
            )

        return record_placed
