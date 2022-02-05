from environs import Env

env = Env()
env.read_env(".env")
# connect link in database
mongo_conn = env.str('MONGO')
