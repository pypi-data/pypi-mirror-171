'''Responsible for communicating with target or system.
Author: Sekgobela Kevin
Date: June 2022
Languages: Python 3
'''

from typing import List, Set

from . import util


class Attempt():
    '''
    Attempts to log into system with data. System can be
    anything that requires certain credentials to access.
    This can include website or file requiring username and
    password to access.'''
    unraised_exceptions_classes: Set[BaseException] = set()

    def __init__(self, target, data:dict, retries=1) -> None:
        '''
        target - system to send data to e.g url
        data - data to send to target'''
        self._target = target
        self._data = data

        # session to share with other attack object
        self._session = None
        # Error message from responce
        self._responce_msg = None
        # represents our responce
        self._responce = None

    def get_responce_message(self):
        return self._responce_msg

    def get_target(self):
        # Returns target to be used for attack
        return self._target

    def get_data(self):
        # Returns data to be used for attack
        return self._data

    @classmethod
    def add_unraised_exception(cls, exception):
        # Adds exception not to be raised on .request(self)
        cls.unraised_exceptions_classes.add(exception)

    def remove_unraised_exception(cls, exception):
        # Removes exception not to be raised on .request(self)
        cls.unraised_exceptions_classes.discard(exception)

    @classmethod
    def _should_raise_exception(cls, exception):
        # Returns True if exception should be raised on .request(self)
        if isinstance(exception, BaseException):
            for unraised_exception in cls.unraised_exceptions_classes:
                if isinstance(exception, unraised_exception):
                    return False
            return True
        else:
            err_msg = "exception needs to be BaseException not" +\
            " " + str(type(exception))
            raise TypeError(err_msg)

    def validate_data(self, data):
        '''Checks if data is in valid for request'''
        # if not isinstance(data, dict):
        #     #err_msg = "data needs to be in dictionary form"
        #     #raise TypeError(err_msg)
        #     return False
        return True

    @classmethod
    def create_session(cls):
        # Creates session object to use with request
        raise NotImplementedError
       

    def close_session(self):
        '''Closes session object'''
        if self.session_exists():
            util.try_close(self._session)

    def close_responce(self):
        "Closes responce object"
        if self._responce:
            util.try_close(self._responce)
    
    def session_exists(self) -> bool:
        '''Returns True if session exists'''
        return self._session != None

    def set_session(self, session):
        '''Sets session object structure to use with .request().
        session can be anything that be reused with request.'''
        self._session = session

    def get_session(self):
        '''Returns session if exists else None'''
        return self._session

    def get_responce(self):
        '''Returns responce from target'''
        return self._responce
        

    def request(self):
        "Sends data to target to be tested, returns responce"
        # use our target and data to return responce
        # None or False should be returned if it fails
        # Also set fail_msg if error is encountered or it fails
        err_msg = "request() method not implemented"
        raise NotImplementedError(err_msg)

    def before_request(self):
        # Called im,edeiately when start() is called
        if not self.validate_data(self._data):
            err_msg = "Data({}) is not valid".format(self.data)
            err_msg2 = "check if the data is in right format"
            raise ValueError(err_msg, err_msg2)

    def after_request(self):
        # Called after start() completes
        pass

    def _start(self):
        try:
            self._responce =  self.request()
        except Exception as e:
            if self._should_raise_exception(e):
                raise e
            else:
                self._responce = e
                self._responce_msg = str(e)
        if self._responce == None:
            err_msg = "responce cant be None"
            raise Exception(err_msg)

    def start(self, retries=1):
        '''Start a request and update internal attributes based on
        returned responce'''
        self.before_request()
        self._start()
        self.after_request()

    def close(self):
        #self.close_session()
        if self._responce:
            self.close_responce()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()




class AttemptAsync(Attempt):
    '''Asyncio version of Attempt class'''
    def __init__(self, target, data: dict, retries=1) -> None:
        super().__init__(target, data, retries)

    @classmethod
    async def create_session(cls):
        # Creates session object to use with request
        raise NotImplementedError

    async def close_session(self):
        '''Closes session object'''
        if self.session_exists():
            await util.try_close_async(self._session)

    async def close_responce(self):
        "Closes responce object"
        if self._responce:
            await util.try_close_async(self._responce)

    async def before_request(self):
        super().before_request()

    async def after_request(self):
        super().after_request()

    async def request(self):
        # Strictly should be async with await
        # Responce should be returned else None if request failed
        err_msg = "request() method not implemented"
        raise NotImplementedError(err_msg)

    async def _start(self):
        try:
            self._responce =  await self.request()
        except Exception as e:
            if self._should_raise_exception(e):
                raise e
            else:
                self._responce = e
                self._responce_msg = str(e)
        if self._responce == None:
            err_msg = "responce cant be None"
            raise Exception(err_msg)


    async def start(self, retries=1):
        '''Start a request and update internal attributes based on
        returned responce'''
        await self.before_request()
        await self._start()
        await self.after_request()

    async def close(self):
        #self.close_session()
        if self._responce:
            await self.close_responce()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    


if __name__ == "__main__":
    import requests

    class WebLogAttempt(Attempt):
        def __init__(self, target, data: dict, retries=1) -> None:
            super().__init__(target, data, retries)
            self.request: requests.Request

        def request(self):
            return requests.post(self._target, params=self._data)

        @property
        def text(self):
            if self.target_reached:
                return self._responce.text


    url = 'https://httpbin.org/get'
    data = {'key1': 'value1', 'key2': 'value2'}
    attempt_obj = WebLogAttempt(url, data)
    attempt_obj.start()
    print(attempt_obj.request_failed)
    print(attempt_obj.request_failed_msg)
    print(type(attempt_obj.text))

