from flask_restplus import fields
from skf.api.restplus import api


checklist = api.model('checklist', {
    'kb_item_title': fields.String(attribute='kb_items.title', required=True, description='Knowledge base title'),
    'kb_items_content': fields.String(attribute='kb_items.content', required=True, description='Knowledge base content'),
    'checklist_items_checklistID': fields.String(attribute='checklist_items.checklistID', required=True, description='The unique identifier of a checklist item'),
    'checklist_items_content': fields.String(attribute='checklist_items.content', required=True, description='Checklist content'),
    'checklist_items_level': fields.Integer(attribute='checklist_items.level', required=True, description='Checklist level'),
    'checklist_items_type': fields.Integer(attribute='checklist_items.checklist_type', required=True, description='Checklist type'),
})

checklist_items = api.inherit('List of checklist items', {
    'items': fields.List(fields.Nested(checklist))
})

checklist_update = api.model('checklist_update', {
    'content': fields.String(required=True, description='Checklist content'),
    'level': fields.Integer(required=True, description='The level of the checklist item'),
    'kbID': fields.Integer(required=False, description='The unique identifier of a kb item for this checklist item'),
    'include_always': fields.Boolean(required=True, description='Always include this checklist item'),
    'include_first': fields.Boolean(required=True, description='Only include this checklist item first time'),
    'question_sprint_ID': fields.Integer(required=True, description='The sprint question unique identifier this checklist belongs to'),
    'question_pre_ID': fields.Integer(required=True, description='The pre question unique identifier this checklist belongs to'),
})

checklist_type = api.model('checklist_type_create', {
    'checklist_name': fields.String(required=True, description='Name of the new checklist'),
})

checklist_types = api.model('checklist_types', {
    'checklist_type': fields.Integer(readOnly=True, description='The unique identifier of the checklist type'),
    'checklist_name': fields.String(required=True, description='Name of the checklist type'),
})

checklist_type_items = api.inherit('List of checklist types', {
    'items': fields.List(fields.Nested(checklist_types))
})

message = api.model('Response message', {
    'message': fields.String(required=True, description='Response message'),
})
