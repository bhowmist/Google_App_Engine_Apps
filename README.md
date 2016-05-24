# Google_App_Engine_Apps
Takes a string and generates the longest substring in alphabetical order with login, memcache and acknowledgement mail:

It takes a string(eg: 'I am a good boy!!') as input and generates the longest substring in alphabetical order as output(eg: 'goo').

At first it asks for gmail account credentials to verify the user and permits to use the service.

Memcache is used to store recently calcuated data so as to fetch it if frequently used.

At end the service sends an acknowledgement to the user's gmail address.

Step to run this service:

1) Open a new tab in the browser. 2) Type "imagecin.appspot.com" in URL 3) Press Login to enter and provide GMAIL ID and password to enter 4) Provide a string and press submit. 5) See the result on web browser and check for email in GMAIL account
