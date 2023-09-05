# DevOps-02: 🐳 Dockerizing Your App and Hosting It on an AWS Container Registry 🚀
## Step-by-Step Guide 📝

### Step 1: Application Setup 🏗️

- Ensure your application code is organized within the "your-app-folder" directory.
- Create a [Dockerfile](app/Dockerfile) within this folder to define how your application should be packaged into a Docker image. 🐳
- Test creating a image `docker build --tag devops-02-image .`
- Create a container `docker run --name devops-02-container -p 8080:80 devops-02-image`

### Step 2: Packer Configuration ⚙️

- In the "packer" directory, create a Packer template (e.g., packer-template.pck.hcl) to specify how Packer should build the Docker image.
- Define the necessary builders, provisioners, and other configuration settings in the Packer template. 🛠️

### Step 3: GitHub Actions Workflow 🤖

- Create a GitHub Actions workflow file (e.g., docker-build.yml) within the ".github/workflows" directory.
- Define the workflow steps to trigger Packer, build the Docker image, and push it to AWS. 🚀

### Step 4: AWS Integration ☁️

- Ensure you have an AWS account with the necessary IAM permissions to interact with Amazon ECR (Elastic Container Registry).
- Configure your AWS credentials securely, either as GitHub Secrets or using AWS IAM roles, within your GitHub repository. 🔐

### Step 5: Workflow Testing and Execution 🧪

- Commit and push your project files to your GitHub repository.
- GitHub Actions will automatically trigger the workflow defined in "docker-build.yml" whenever changes are pushed to the repository. 🔄

## Next Steps 🚀

With your project set up, you're now ready to:

- Refine your Dockerfile to ensure your application is properly configured. 🛠️
- Adjust your Packer template for optimal image creation. 🖼️
- Fine-tune your GitHub Actions workflow as needed. 🤓
- Monitor your workflow runs and Docker image uploads in the GitHub Actions tab of your repository. 📊
- Explore AWS to manage and deploy your Docker images. ☁️

Happy coding and automating! 🎉

