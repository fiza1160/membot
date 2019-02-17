import redis
import sys
from initialization import get_redis_host as redis_host
from initialization import get_redis_port as redis_port

# TODO add func to change priority
# TODO add func to delete one doing

try:
    base = redis.StrictRedis(host=redis_host(), port=redis_port(), db=0)
except ValueError as err:
    print(err.args[0])
    sys.exit(1)


def user_tasks_key(user_id):
    key = 'membot_user_tasks:{id}'.format(id=user_id)
    return key


def add(user, value):
    base.rpush(user_tasks_key(user), str(value))


def get_all(user):
    # TODO add sort by priority
    task_list = base.lrange(user_tasks_key(user), 0, -1)
    if len(task_list) == 0:
        text = '''\
            There is nothing in list yet. You can simply add a new task, \
just send me a message and I will remember it for you.
            '''
        return text
    text = get_task_list_by_string(task_list)
    return text


def get_task_list_by_string(task_list):
    text = ''
    for ind, task in enumerate(task_list):
        text += str(ind + 1) + '. ' + task.decode() + '\n'
    return text


def delete_all(user):
    base.delete(user_tasks_key(user))
