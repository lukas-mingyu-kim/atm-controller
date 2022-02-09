# Setup
(Assuming Docker is installed in the system,)
1. Create docker image
   
    ```$ docker build -t atm-controller .```


2. Run dockeer container

    ```$ docker run -d -p 8000:8000 --name atm-controller atm-controller```