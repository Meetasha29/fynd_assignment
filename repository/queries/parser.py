from sqlalchemy.sql import operators


class FilterDictParser(object):
    default_operator = operators.eq
    _operator_map = {
        "lte": operators.le,
        "gte": operators.ge,
        "in": operators.in_op,
        'between': operators.between_op
    }

    def __init__(self, filter_dict, model):
        self.filter_dict = FilterDictParser._clean_filter_dict(filter_dict)
        self.model = model

    def parse(self):
        filter_fields_list = []
        for key, value in self.filter_dict.items():
            try:
                _key_splited_list = key.split('__')
                db_field = _key_splited_list[0]
                _mapper_key = _key_splited_list[1]
                filter_fields_list.append(self._operator_map[_mapper_key](getattr(self.model, db_field), value))
            except IndexError:
                filter_fields_list.append(self.default_operator(getattr(self.model, key), value))
        return filter_fields_list

    @staticmethod
    def _clean_filter_dict(filter_dict):
        cleaned_filter_dict = {}
        for key, value in filter_dict.items():
            if value is not None:
                if isinstance(value, list):
                    key = '{}__in'.format(key)
                cleaned_filter_dict.update({key: value})
        return cleaned_filter_dict
