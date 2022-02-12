# ATM Controller

## Setup
(Assuming Docker is installed in the system,)
1. Create docker image
   
    ```$ docker build -t atm-controller .```
   - It will run tests & setup dummy data.
   - It will create a docker image named 'atm-controller'.


2. Run dockeer container

    ```$ docker run -d -p 8000:8000 --name atm-controller atm-controller```
   - It will run a docker container named 'atm-controller', which function as an API server.
   - The server will be listening on the port 8000.
   
## APIs
(Click to see details.)

* [Sign In](doc/points/list.md) : `[POST] /auth/signin`
* [List Accounts](doc/points/get.md) : `[GET] /api/accounts`
* [Get an Account](doc/points/post.md) : `[GET] /api/accounts/<account_id>`
* [Deposit to an Account](doc/points/patch.md) : `[PATCH] /api/accounts/<account_id>/deposit`
* [Withdraw from an Account](doc/points/delete.md) : `[PATCH] /api/accounts/<account_id>/withdraw`

## Clean Up
1. Stop docker container
   
   ```$ docker stop atm-controller```

2. Remove docker container
   
   ```$ docker rm atm-controller```

3. Remove docker image

   ```$ docker rmi atm-controller```
