import datetime
from api.models.database import DatabaseConnection


class Record:

    """
    Class to handle records creation
    """
    db = DatabaseConnection()

    def __init__(
        self, record_type=None, record_title=None, 
        record_geolocation=None, status=None, 
        user_id=None,record_no=None
        ):
        self.record_no = None
        self.user_id = user_id
        self.record_title = record_title
        self.record_geolocation = record_geolocation
        self.record_type = record_type
        self.status = 'Under Investigation'
        self.record_placement_date = datetime.datetime.now().strftime\
        ("%Y-%m-%d %H:%M:%S")


    def post_record(
        self,record_type=None, record_title=None, 
        record_geolocation=None, user_id=None
        ):
        """
        User can be able to post a new record
        """
        record_placed = self.db.post_record(
            record_type, record_title, record_geolocation, user_id
            )
        return record_placed