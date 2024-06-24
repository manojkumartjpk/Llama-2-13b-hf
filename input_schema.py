INPUT_SCHEMA = {
    "message": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["How to make a omellete ?"]
    },
    'chat_history': {
        'datatype': 'STRING',
        'required': False,
        'shape': [-1,2],
        'example': [["How to make a omellete ?", "How to make a omellete ?"]]
    }
}
