
debugMode = True

APP_SECRET_KEY = 'ironmanJjangJjang'
ADMIN_PASSWORD = 'ironsilvergold'

CSRF_LENGTH = 10
IMAGE_EXTENSIONS = ('jpg', 'jpeg', 'png')
VIDEO_EXTENSIONS = ('mp4', 'avi')

HOME_PATH = '/home/smilu/iron/'

FILE_PATH_PREFIX = 'static/files/'
IMAGE_FOLDER_BEFORE = FILE_PATH_PREFIX + 'images_before/'
IMAGE_FOLDER_AFTER = FILE_PATH_PREFIX + 'images_after/'
VIDEO_FOLDER = FILE_PATH_PREFIX + 'videos/'

MYSQL_DATABASE_NAME 	= 'iron'
MYSQL_DATABASE_USER		= 'root'
MYSQL_DATABASE_PASSWORD	= '123456'
MYSQL_DATABASE_HOST		= 'mysql://%s:%s@localhost/%s' % (MYSQL_DATABASE_USER, \
	MYSQL_DATABASE_PASSWORD, MYSQL_DATABASE_NAME)
MYSQL_DATABASE_PORT		= 3306
MYSQL_DATABASE_DB		= 'iron'

NLTK_DATA_PATH = '/home/smilu/nltk_data/'