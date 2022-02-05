from environs import Env

env = Env()
env.read_env(".env")
# connect link in database
mongo_conn = env.str('MONGO')

MAX_CONNECTIONS_COUNT = env.int("MAX_CONNECTIONS_COUNT")
MIN_CONNECTIONS_COUNT = env.int("MIN_CONNECTIONS_COUNT")