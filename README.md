// This is a gerenal beginners tutorial for start to finish of a simple app creation, deployment, setup of pipelines, argoCD and manifest files for deployment through Kubernetes and use of docker images for image repositories.

1. Create a project in python
2. Push to GitHub by creating a repo there
3. Dockerize by creating a docker file to install requirements and expose the ports
>> Push to docker images to build images. 
>> docker login ghcr.io —Github actions — login using GitHub username and token	
>>docker build
>> docker tag python-gitops-app:v1 ghcr.io/YOUR_USERNAME/python-gitops-app:v1 >> This builds the github action package for CI/CD
>> docker push ghcr.io/YOUR_USERNAME/python-gitops-app:v1
4. Create K8 manifest files 
>>deployment.yaml
>>service.yaml
>>kustomization.yaml
5. Ensure K8 and argoCD are installed
>> kubectl create namespace argocd
>> kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
6. Expose the UI for argoCD Server:
>> kubectl port-forward svc/argocd-server -n argocd 8080:443 
7. Create argocd yaml manifest
>> In the GitHub project, confirm where your manifest folder location is to update on the path secion in the argo-manifest
>> kubectl apply -f argocd-app.yaml
>> argo-cd manifest file should have the correct path to GitHub project manifests
8. Access the App
>> kubectl port-forward svc/python-gitops-app 8000:80
>> Ensure package visibility in GitHub is set to public to ensure deployment succeeds and pod starts correctly.
