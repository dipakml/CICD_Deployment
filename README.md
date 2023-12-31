AZURE-CICD-Deployment-with-Github-Actions

Login server: cicd121.azurecr.io
password- EVMpo4js/kS49Cl11K3YmnVyCPizLb8v016P+ZfvpQ+ACRDrT3sU

Run from terminal:
docker build -t cicd121.azurecr.io/cicd121:latest .

docker login cicd121.azurecr.io

docker push cicd121.azurecr.io/cicd121:latest

Deployment Steps:
1. Build the Docker image of the Source Code
2. Push the Docker image to Container Registry
3. Launch the Web App Server in Azure
4. Pull the Docker image from the container registry to Web App server and run