# Django photography site
   This  is simple photography site which can be used showcase image collections in an creative manner

# Features
	* Clean HTML Design - Responsive and Beautifully HTML design
	* Django CMS integrated - Easily manage and upload photos in backend
	* Social Share - Facebook, Instagram, Twitter and Google Plus
	* database - default django sqllite

#Installation
	* 	Install server level prerequisites
			*	sudo apt-get update
			*	sudo apt-get install build-essential
			* 	sudo apt-get install python-dev
			*	sudo apt-get install libjpeg8-dev
	
	* 	Clone code from GIT and Move to cloned directory
			* 	git clone https://github.com/muhilvarnan/django-photography-site.git
			*	cd django-photography-site 

	*	Activate virutal Env and install required pip modules
			* 	source /PATHTO/Env/bin/activate
			*	pip install - r requirements.txt

	*	Install solr thumbnail 
			*	pip install git+git://github.com/mariocesar/sorl-thumbnail@v12.3

	*	Makemigrations and Migrate
			*	python manage.py makemigrations
			*	python manage.py migrate

	* 	Create a super user
			*	python manage.py createsuperuser
	
	*	Runserver 
			* 	python manage.py runserver

#configuration - settings.py
	* Following configuration can be changed in settings.py file in the base app
		*	WEBSITE_TITLE - Website title 
		* 	BASE_BACKGROUND_IMAGE_STATIC_PATH - Background image in the home page, django static file path

# References and sources
	* http://tympanus.net/codrops/
	* https://jquery.com
	* http://tutorial.djangogirls.org

[Issues](https://github.com/muhilvarnan/django-photography-site/issues	)