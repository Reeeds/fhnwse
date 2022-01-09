This application is about the algorythm recognizing an image from the defined classes Aeroplane, Automobile, Bird, Cat, Deer, Dog, Frog, Horse, Ship or Truckman.

The app consists of the algorythm, an API and the user interface.

1. The algorythm is trained using the CIFAR 10 dataset with a CNN model.

2. The API is controlled by the templates index.html, layout.html, template.html and upload.html.

3. The user interface displays the prediction of the desired image. To launch the user interface, the following must be done.
Start Flask App:
    1. run api/app.py in Visual Code.
    2. app runs on http://127.0.0.1:5000/
    3. select image (Example Images in Folder fhnwse/tests/pictures)
    4. hit predict button


