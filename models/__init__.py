#!/usr/bin/python3
# initializartion for storage module
"""This is the init file for the models package"""


from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
