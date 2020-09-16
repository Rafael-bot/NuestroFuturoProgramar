def image_upload_location(instance,filename):
    return 'media/index/images/%s.png' % (instance.id)