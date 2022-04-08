from bottle import route, run, template, static_file, redirect, error, BaseTemplate
import bottle
import whatismyip
from ip2geotools.databases.noncommercial import DbIpCity
from mongoengine import *
from datetime import datetime
import datetime
from passlib.hash import pbkdf2_sha256
import random
from pyicloud import PyiCloudService
import sys

app = bottle.default_app()
BaseTemplate.defaults['get_url'] = app.get_url 
hash = pbkdf2_sha256.hash('A SECRET HERE') 
pycloud_api = PyiCloudService('icloud info')

if pycloud_api.requires_2fa:
    print("Two-factor authentication required.")
    code = input("Enter the code you received of one of your approved devices: ")
    result = pycloud_api.validate_2fa_code(code)
    print("Code validation result: %s" % result)

    if not result:
        print("Failed to verify security code")
        sys.exit(1)

    if not pycloud_api.is_trusted_session:
        print("Session is not trusted. Requesting trust...")
        result = pycloud_api.trust_session()
        print("Session trust result %s" % result)

        if not result:
            print("Failed to request trust. You will likely be prompted for the code again in the coming weeks")
elif pycloud_api.requires_2sa:
    import click
    print("Two-step authentication required. Your trusted devices are:")

    devices = pycloud_api.trusted_devices
    for i, device in enumerate(devices):
        print(
            "  %s: %s" % (i, device.get('deviceName',
            "SMS to %s" % device.get('phoneNumber')))
        )

    device = click.prompt('Which device would you like to use?', default=0)
    device = devices[device]
    if not pycloud_api.send_verification_code(device):
        print("Failed to send verification code")
        sys.exit(1)

    code = click.prompt('Please enter validation code')
    if not pycloud_api.validate_verification_code(device, code):
        print("Failed to verify verification code")
        sys.exit(1)



posts = [
    {'title' : 'Chiquis at Danny\'s house', 'date' : datetime.datetime.today().strftime('%d.%m.%Y'), 'image' : '1ab65fa0-fc5a-4d79-9a2b-fa7bab8f2b8b.jpeg'}
]

videos = [
    {'title' : 'Chiquis first day home', 'date' : datetime.datetime.today().strftime('%d.%m.%Y'), 'video' : 'IMG_5947.mov'},
    {'title' : 'Chiquis first day home', 'date' : datetime.datetime.today().strftime('%d.%m.%Y'), 'video' : 'IMG_6067.mov'},
    {'title' : 'Chiquis first day home', 'date' : datetime.datetime.today().strftime('%d.%m.%Y'), 'video' : 'IMG_6228.mov'},
]

images = [
   '/static/images/uploads/IMG_0782.jpeg',
   '/static/images/uploads/IMG_1948.jpeg', 
   '/static/images/uploads/IMG_5926.jpeg', 
   '/static/images/uploads/IMG_5927.jpeg', 
   '/static/images/uploads/IMG_5928.jpeg', 
   '/static/images/uploads/IMG_5960.jpeg', 
   '/static/images/uploads/IMG_5976.jpeg', 
]

video_list = [
  '/static/images/uploads/videos/IMG_5947.mov', 
  '/static/images/uploads/videos/IMG_6067.mov', 
  '/static/images/uploads/videos/IMG_6228.mov', 
]



connect(host='')

class Admin(Document):
    name = StringField(required=True)
    password = StringField(required=True)
    image = ImageField()

class User(Document):
   name = StringField(required=True)
   image = ImageField()

class Comment(EmbeddedDocument):
    comment = StringField(required=True)
    comment_date = DateTimeField(default=datetime.datetime.utcnow)
    user = ReferenceField(User)

class Post(Document):
    title = StringField(max_length=150, required=True)
    comment = ListField(EmbeddedDocumentField(Comment))
    tags = ListField(StringField(max_length=35))
    media = FileField()
    likes = IntField()

    def add_post(post):
        post.save()

    def get_all_posts():
        return [post.title for post in Post.objects]
    
    def filter_by_tag(tag):
        return [post.title for post in Post.objects(tags=f'{tag}')]

    def get_post(id):
        return [post.title for post in Post.objects(_id=f'{id}')]
        
    def remove_post(post):
        post.delete()

@route('/static/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='static/css')

@route('/static/js/<filename:re:.*\.js>')
def send_js(filename):
    return static_file(filename, root='static/js')

@route('/static/images/<filename:re:.*\.png>')
def send_images(filename):
    return static_file(filename, root='static/images')

@route('/static/images/uploads/<filename:re:.*\.jpeg>')
def send_uploads(filename):
    return static_file(filename, root='static/images/uploads')

@route('/static/images/uploads/videos/<filename:re:.*\.mov>')
def send_video_uploads(filename):
    return static_file(filename, root='static/images/uploads/videos')






@route('/icloud')
def icloud_photos():
    icloud_drive_photos = pycloud_api.drive['chiquis']['images'].dir()
    icloud_drive_videos = pycloud_api.drive['chiquis']['videos'].dir()
    for video in icloud_drive_videos:
        print(video)
    #icloud_photos = pycloud_api.photos.all
    return icloud_drive_photos


@route('/')
def index():
    if ip_address := whatismyip.whatismyip():
        response = DbIpCity.get(ip_address, api_key='free')
    if 'CO' in response.country:
        return redirect('/es')
    return redirect('/en')

@route('/en', name='en_index')
def en_index():
    return template('en/index', posts=zip(posts, videos))

@route('/en/photos', name='en_photos')
def en_photos():
    return template('en/photos')  

@route('/en/videos', name='en_videos')
def en_videos():
    return template('en/videos')  

@route('/api/en', name='en_api')
def api():
    return template('en/api')


@error(404)
def error_404(error):
    return 'Nothing....'



@route('/api/en/latest/photos/<count>')
def latest_photo_count():
    return dict()


@route('/api/en/photo/random/')
def random_photo():
    data = random.choice(images)
    return dict(data=data)

@route('/api/en/latest/photos/')
def latest_photos():
    pass

@route('/api/en/latest/videos/<count>')
def latest_video_count():
    pass

@route('/api/en/latest/videos/')
def latest_videos():
    pass

@route('/api/en/oldest/photos/<count>')
def oldest_photo_count():
    pass

@route('/api/en/oldest/photos')
def oldest_photos():
    pass

@route('/api/en/oldest/videos/<count>')
def oldest_video_count():
    pass

@route('/api/en/oldest/videos/')
def oldest_videos():
    pass


@route('/api/en/video/random/')
def random_video():
    data = random.choice(video_list)
    return dict(data=data)



@route('/es', name='es_index')
def es_index():
    return template('es/index', posts=zip(posts, videos))

@route('/es/docs', name='es_docs')
def es_docs():
    return template('es/docs')    

@route('/api/es', name='es_api')
def api_es():
    return template('es/api')





@route('/api/es/latest/photos/<count>')
def latest_es_photo_count():
    pass

@route('/api/es/latest/photos/')
def latest_es_photos():
    pass

@route('/api/es/latest/videos/<count>')
def latest_es_video_count():
    pass

@route('/api/es/latest/videos/')
def latest_es_videos():
    pass

@route('/api/ens/oldest/photos/<count>')
def oldest_es_photo_count():
    pass

@route('/api/es/oldest/photos')
def oldest_es_photos():
    pass

@route('/api/es/oldest/videos/<count>')
def oldest_es_video_count():
    pass

@route('/api/es/oldest/videos/')
def oldest_es_videos():
    pass

@error(404)
def error_404():
    pass








app.run(host='localhost', port=9988)



