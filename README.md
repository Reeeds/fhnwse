This application is about the algorythm recognizing an image from the defined classes Aeroplane, Automobile, Bird, Cat, Deer, Dog, Frog, Horse, Ship or Truckman.

The app consists of the algorythm, an API and the user interface.

1. The algorythm is trained using the CIFAR 10 dataset with a CNN model.

2. The API is controlled by the templates index.html, layout.html, template.html and upload.html.

3. The user interface displays the prediction of the desired image. To launch the user interface, the following must be done.
Start Flask App:
    1. run api/app.py in Visual Code (conda)
    2. app runs on http://127.0.0.1:5000/
    3. select image (Example Images in Folder fhnwse/tests/pictures)
    4. hit predict button




Additional information
1. Our project is availlable on Github: https://github.com/Reeeds/fhnwse
2. For project- and issue management, we used Github's issue tool. See https://github.com/Reeeds/fhnwse/issues
3. While developping we used the following packages:
    - black
    - autoflake
    - flake8
4. To run the four testcases in test_app_helper_model.py, execute the command pytest in the console.
5. To deploy the app we would use Heroku. Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud. We simply push our Git Repo with the prod / dev branch to Heroku and it works. More informations: https://devcenter.heroku.com/articles/git
6. To restrict the access to our app we could use cloudflare for restricting ip-adresses, limit volumes or traffic
7. To monitor, troubleshoot and tune our app we would use a Heroku Addon: New relic https://elements.heroku.com/addons/newrelic


Projekt (Software Engineering für Data Scientists)
Data Science Weiterbildung, FHNW

Roman Hasler, Reto Schürmann
14.01.2021
