# Getting Started

    Practical GitHub Actions - by Ray Villalobos
    Learning objectives
        Define what GitHub Actions are and explain their purpose.
        Demonstrate how to build and publish custom GitHub Actions.
        Use GitHub marketplace to find and integrate community-created actions.
        Outline the setup for hosting static websites using GitHub Pages.
        Create and configure a GitHub repository for automating tasks.
        Design a GitHub Action workflow that triggers on repository events.
        Create entry point scripts for Docker containers and manage execution permissions.
        Develop a modular setup for reusable actions across different repositories.
        Explain the role of Docker in running actions in the cloud.
        Formulate a Dockerfile to set up an environment for running Python scripts.

## Q & A

### 1. You have created a new repository named 'podcast-generator' in GitHub. To ensure that other repositories can use the Python script 'feed.py' from this new repository, which mechanism would you use?
Ans: Create a Dockerfile and an entry point file in the podcast-generator repository.
Creating a Dockerfile and an entry point file ensures that the feed.py script can be executed within a standardized environment, making it easy for other repositories to call the script as an action.

### 2. You have created a GitHub action to generate podcast feeds but see that the workflow is failing with 'entrypoint.sh: permission denied: unknown' error. Which action should you take to resolve this issue?
Ans: Run the command chmod -R 775 entrypoint.sh to change the permissions of the entrypoint.sh file.

### 3. You are tasked with setting up a new GitHub Actions workflow in your repository. Part of this action requires pulling data from another repository, processing it using a Docker image you previously built, and then pushing the results back. How would you describe the correct steps to accomplish this using the provided script?
Ans: Define an action YAML file that specifies using Docker as the runner, set up the Docker file for processing, and ensure the entry point script handles the workflow execution.
This approach correctly follows the steps outlined: specifying the action YAML file, using Docker for processing, and ensuring the entry point script can handle the workflow execution.

### 4. You are collaborating with a team on a project that involves processing a YAML file to generate an XML file for an RSS feed. One team member suggests everyone should work locally and install the necessary tools themselves. What could be a more efficient approach to ensure everyone has a consistent environment with all needed tools already installed?
Ans: Use GitHub Codespaces to create a virtual environment with all necessary tools pre-installed.

### 5. Your team is setting up a new podcast repository on GitHub and wants to ensure that it is visible to the public through GitHub Pages. Which steps should you take after creating the repository and adding the required files?
Ans: Enable GitHub Pages in the repository settings and choose the main branch as the source.

### 6. You have a podcast and want to create an RSS feed for it using YAML for easy content writing and then convert it to XML. Which approach achieves this efficiently using GitHub tools?
Ans: Use a GitHub Action with Python to parse YAML into XML and host the feed using GitHub Pages.
This approach leverages GitHub Actions for automation, Python for parsing, and GitHub Pages for hosting, making the process seamless and efficient.


**What we are creating?**
> Podcast Feed Generator
> Technically Podcast feed is an **XML file** in specific format called **RSS** [RSS Feeds] 
[eg: https://gist.github.com/rodydavis/d0cb7a53d8deb42e92ae803a9dd48dbc]
> We are using **GitHub Actions** to generate **Feed** [since XML and RSS are difficult to create]
> YAML is super easy format to write

**Tech stack:**
> We are using GitHub Pages to host podcast feed
> Python - we are using to parse yaml into XML
> Docker - to publish into github market place
> Bash Scripting

* [Original source repo](https://github.com/LinkedInLearning/github-practical-actions-4412872)
  Switch to branch: 01_02b [download zip file and keep it handy]

**Steps**
> Create new repo: githubactions-podcast-test
> Upload audio,images,feed.yaml and ReadMe-feed.md file from above source repo
> Go to Settings - Pages - [Deploy from branch] select master branch and save
    Note: creating github page(s) will automatically create/initiate github actions
> It will take a while to generate URL
      https://mahanteshtalikoti-git.github.io/githubactions-podcast-test/
      https://mahanteshtalikoti-git.github.io/githubactions-podcast-test/images/artwork.jpg
> **Go to Code tab - Code button - Codespaces**
> This will create a virtual box with Python/Pip/PyYaml module pre-installed

### Reference URL(s)
* [Sample Apple iTunes feed](https://help.apple.com/itc/podcasts_connect/en.lproj/itcbaf351599.html)
OR
* [Alternative](https://gist.github.com/rodydavis/d0cb7a53d8deb42e92ae803a9dd48dbc)

> GitHub pages link:
https://mahanteshtalikoti-git.github.io/githubactions-podcast-test/
https://mahanteshtalikoti-git.github.io/githubactions-podcast-test/podcast.xml

### Concluding remarks w.r.t githubactions-podcast-test repo
So far as part of "githubactions-podcast-test" project we built a RSS feed generator, next step is to automate it.

git add [all the files to master branch] && 
git commit -m "Implemented feed.py to generate podcast.xml file"
git push

## 2nd Goal:
If somebody modifies the feed.yaml file [add of additional episode] or drop an additional audio file; we need to automatically
run feed.py, generate podcast.xml and push things on to server [GitHub pages]
To achive: we need to create an Action.

Navigate to Actions - New Workflow
create main.yml with respective wf steps
```
  [

      On branch master
    Your branch is up to date with 'origin/master'.

    nothing to commit, working tree clean
    Error: Process completed with exit code 1.
  ]
  Resolution: Settings - Actions - General - Workflow permissions
  Change to - Read and write permissions
  Caveat: above permission will not be pushed to master branch auto; hence make some code changes in feed.yaml or any file and push
```

## 3rd Goal [New Repo]:
> Create a new repo that will act as podcast generator that will create podcast(s) calling same action feed.py
  **githubactions-podcast-generator**
  with ReadMe.md and License = MIT License
  copy the same feed.py from "githubactions-podcast-test" into this new repo
> Launch CodeSpace and create Dockerfile
> chmod -R 775 entrypoint.sh

### Key file(s) in this repo:
a] Dockerfile
b] entrypoint.sh
c] feed.py from the prev repo
d] action.yml
  Think of an action.yml file as the instruction manual or manifest for a CUSTOM GitHub Action.
  While standard GitHub workflow files (located in .github/workflows/) tell GitHub when and where to run tasks, 
  the action.yml file defines what a specific, reusable action actually does and what it needs to work.

**Core Functions of custom workflow via action.yml :**
  If you are creating a custom action (whether it's Docker-based, JavaScript, or a Composite action), the action.yml file is mandatory 
  and serves three main purposes:
  Defines Inputs: Lists the parameters the action needs from the user (e.g., an API key or a target directory).
  Defines Outputs: Lists the data the action will send back to the rest of the workflow (e.g., a status code or a generated file path).
  Specifies Execution: Tells GitHub how to run the code—for example, by pointing to a specific script file or a Docker image.  

**Key Components of the File**
  A typical action.yml includes several standard sections:
  name: The name of your action as it appears in the GitHub Marketplace.
  description: A short summary of what the action does.
  inputs: A map of parameters that the action accepts.
  outputs: A map of results the action produces.
  runs: The most critical part. It defines if the action is "javascript", "docker", or "composite" 
      and specifies the entry point (like main: 'index.js').  
