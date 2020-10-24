import logging

from connectors.database import db
from repository.queries.parser import FilterDictParser

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class BaseQueries(object):
    """
    Encapsulates all the IMDB model related queries here.
    """
    model = None

    @staticmethod
    def rollback():
        db.session.rollback()

    @staticmethod
    def commit_changes(instance=None):
        """
        Method which finally commits changes to database for create and update
        """
        db.session.commit()
        return instance

    def create(self, create_dict, auto_commit=True):
        """
        This method can be used to create new object in database
        """
        instance = self.model(**create_dict)
        db.session.add(instance)
        db.session.flush()
        if auto_commit:
            instance = BaseQueries.commit_changes(instance)
        return instance

    def sorted_select(self, filter_dict, select_params={}):
        """
        This method can be used to sort and select or filter out the Client Fulfillment Center Mappings based on passed values
        :param order_by:
        :param select_params:
        :param filter_dict: <Dictionary> Filters for organisation to be fetched
        :param page_number: <Integer> Page number used for pagination
        :return:
        """
        filter_by = FilterDictParser(filter_dict, self.model).parse()
        logger.info(filter_by)
        select_model = select_params.pop('select_model', True)

        select_columns = select_params.pop('select_columns', [])
        if select_model:
            query = db.session.query(self.model, *select_columns)
        else:
            query = db.session.query(*select_columns)
        query = query.filter(*filter_by).order_by(self.model.updated_at.desc())
        logger.info('select_query: {}'.format(query))

        instances = query.all()
        return instances

    def fetch_first(self, filter_dict, select_params={}):
        """
        Fetch the exact entity if it exists
        """

        filter_by = FilterDictParser(filter_dict, self.model).parse()
        select_model = select_params.pop('select_model', True)
        select_columns = select_params.pop('select_columns', [])
        if select_model:
            query = db.session.query(self.model, *select_columns)
        else:
            query = db.session.query(*select_columns)
        query = query.filter(*filter_by)
        logger.info('select_query: {}'.format(query))
        result = query.first()

        return result

    def update(self, db_id, update_dict, auto_commit=True):
        """
        This method can be used to update the values of few rows, filtered by the dictionary passed in.
        """
        response = self.model.query.filter_by(id=db_id).update(
            update_dict, update_args={'filter_dict': {'id': db_id}})
        if auto_commit:
            BaseQueries.commit_changes()
        return response

    def delete(self, db_id):
        """
        This method can be used to delete the object from the DB.
        :param db_id: db id needs to be deleted
        """
        self.model.query.filter_by(id=db_id).delete()
        BaseQueries.commit_changes()
