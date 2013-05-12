from key import User
from key import AesEncryption
from key import AESDecryptionWrapper
from persist import shelveWrapper
from Queue import Queue
from mythread import My_thread
import shelve

QUEUE_SIZE = 10


def writeQ(queue, dbObj, userName):
    if queue.full():
        block = True
    else:
        block = False
    if isinstance(dbObj, AesEncryption):
        if dbObj.Id == userName:
            queue.put(dbObj, block=1)
        else:
            return
    else:
        return
    if block:
        pass


def readQ(queue, searchKey, searchString, RESULT_LIST):
    if queue.empty():
        block = True
    else:
        block = False
    if block:
        pass
    else:
        CheckObj = queue.get(block=1)
        if searchKey == 'name':
            if searchString in CheckObj.name:
                RESULT_LIST.append(CheckObj)
        if searchKey == 'phrase':
            if searchString in CheckObj.phrase:
                RESULT_LIST.append(CheckObj)


def writer(queue, loops, KeyList, dbHandle, userName, searchKey,
           searchString, RESULT_LIST):
    for keys in KeyList:
        writeQ(queue, dbHandle[keys], userName)


def reader(queue, loops, KeyList, dbHandle, userName, searchKey,
           searchString, RESULT_LIST):
    for i in range(loops):
        i
        readQ(queue, searchKey, searchString, RESULT_LIST)


def doSearch(store_db, userName, passwd, searchKey, searchString):
    RESULT_LIST = []
    funcs = [writer, reader]
    nfuncs = range(len(funcs))
    swrap = shelveWrapper(store_db)
    user = swrap.retriveUser(userName, passwd)
    if not isinstance(user, User):
        if user == 'User Data not found':
            return "{'error': ' invalid user info passed'}"
    else:
        dbHandle = shelve.open(swrap.shelveDB)
        KeyList = dbHandle.keys()
        nloops = len(KeyList)
        q = Queue(QUEUE_SIZE)

        threads = []
        for i in nfuncs:
            t = My_thread(funcs[i], (q, nloops, KeyList, dbHandle,
                                     userName, searchKey, searchString,
                                     RESULT_LIST), funcs[i].__name__)
            threads.append(t)

        for i in nfuncs:
            threads[i].start()

        for i in nfuncs:
            threads[i].join()

        if len(RESULT_LIST) == 0:
            return"{'result: 'No passwords found after search'}"
        else:
            return_data = []
            for data in RESULT_LIST:
                passwd = AESDecryptionWrapper(user.key,
                                              data.chiperText)
                resDict = {'name': data.name, 'password': passwd,
                           'phrase': data.phrase}
                return_data.append(resDict)
            return return_data
